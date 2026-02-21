from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import ForumCategory, ForumPost, ForumReply, LostPetReport
from .forms import ForumPostForm, LostPetReportForm, ForumReplyForm

def forum_list(request):
    categories = ForumCategory.objects.filter(is_active=True)
    recent_posts = ForumPost.objects.all()[:10]
    return render(request, 'community/forum_list.html', {
        'categories': categories,
        'recent_posts': recent_posts
    })

def category_posts(request, category_id):
    category = get_object_or_404(ForumCategory, id=category_id, is_active=True)
    posts = ForumPost.objects.filter(category=category)
    return render(request, 'community/category_posts.html', {
        'category': category,
        'posts': posts
    })

def post_detail(request, post_id):
    post = get_object_or_404(ForumPost, id=post_id)
    post.views_count += 1
    post.save()
    
    # Get top-level replies (no parent)
    replies = ForumReply.objects.filter(post=post, parent=None).prefetch_related('child_replies__child_replies')
    
    if request.method == 'POST' and request.user.is_authenticated:
        form = ForumReplyForm(request.POST)
        parent_id = request.POST.get('parent_id')
        
        if form.is_valid():
            reply = form.save(commit=False)
            reply.post = post
            reply.author = request.user
            
            if parent_id:
                parent_reply = get_object_or_404(ForumReply, id=parent_id)
                if parent_reply.can_reply():
                    reply.parent = parent_reply
                else:
                    messages.error(request, 'Maximum reply depth reached.')
                    return redirect('community:post_detail', post_id=post.id)
            
            reply.save()
            messages.success(request, 'Reply added successfully!')
            return redirect('community:post_detail', post_id=post.id)
    else:
        form = ForumReplyForm()
    
    return render(request, 'community/post_detail.html', {
        'post': post,
        'replies': replies,
        'form': form
    })

@login_required
def create_post(request):
    if request.method == 'POST':
        form = ForumPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Post created successfully!')
            return redirect('community:post_detail', post_id=post.id)
    else:
        form = ForumPostForm()
    return render(request, 'community/create_post.html', {'form': form})

def lost_pets(request):
    search_query = request.GET.get('search', '')
    status_filter = request.GET.get('status', 'lost')
    
    reports = LostPetReport.objects.filter(is_active=True)
    
    if status_filter:
        reports = reports.filter(status=status_filter)
    
    if search_query:
        reports = reports.filter(
            Q(pet_name__icontains=search_query) |
            Q(breed__icontains=search_query) |
            Q(color__icontains=search_query) |
            Q(last_seen_location__icontains=search_query)
        )
    
    return render(request, 'community/lost_pets.html', {
        'reports': reports,
        'search_query': search_query,
        'status_filter': status_filter
    })

@login_required
def report_lost_pet(request):
    if request.method == 'POST':
        form = LostPetReportForm(request.POST, request.FILES)
        if form.is_valid():
            report = form.save(commit=False)
            report.reporter = request.user
            report.save()
            messages.success(request, f'Lost pet report for {report.pet_name} has been created!')
            return redirect('community:lost_pets')
    else:
        form = LostPetReportForm()
    return render(request, 'community/report_lost_pet.html', {'form': form})

def lost_pet_detail(request, report_id):
    report = get_object_or_404(LostPetReport, id=report_id, is_active=True)
    return render(request, 'community/lost_pet_detail.html', {'report': report})