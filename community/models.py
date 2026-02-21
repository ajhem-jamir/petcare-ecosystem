from django.db import models
from django.contrib.auth import get_user_model
from pets.models import Pet

User = get_user_model()

class ForumCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Forum Categories"

    def __str__(self):
        return self.name

class ForumPost(models.Model):
    POST_TYPES = (
        ('question', 'Question'),
        ('discussion', 'Discussion'),
        ('tip', 'Tip/Advice'),
        ('lost_pet', 'Lost Pet'),
        ('found_pet', 'Found Pet'),
    )
    
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='forum_posts')
    category = models.ForeignKey(ForumCategory, on_delete=models.CASCADE, related_name='posts')
    post_type = models.CharField(max_length=15, choices=POST_TYPES, default='discussion')
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='forum_posts/', blank=True, null=True)
    is_pinned = models.BooleanField(default=False)
    is_solved = models.BooleanField(default=False)
    views_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-is_pinned', '-created_at']

    def __str__(self):
        return self.title

class ForumReply(models.Model):
    post = models.ForeignKey(ForumPost, on_delete=models.CASCADE, related_name='replies')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='forum_replies')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='child_replies')
    content = models.TextField()
    is_solution = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Forum Replies"
        ordering = ['created_at']

    def __str__(self):
        return f"Reply to {self.post.title}"
    
    @property
    def reply_depth(self):
        """Calculate the depth of nested replies (max 2 levels)"""
        if self.parent is None:
            return 0
        elif self.parent.parent is None:
            return 1
        else:
            return 2
    
    def can_reply(self):
        """Only allow replies up to 2 levels deep"""
        return self.reply_depth < 2

class LostPetReport(models.Model):
    STATUS_CHOICES = (
        ('lost', 'Lost'),
        ('found', 'Found'),
        ('reunited', 'Reunited'),
    )
    
    SIZE_CHOICES = (
        ('small', 'Small (under 25 lbs)'),
        ('medium', 'Medium (25-60 lbs)'),
        ('large', 'Large (60-100 lbs)'),
        ('extra_large', 'Extra Large (over 100 lbs)'),
    )
    
    reporter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lost_pet_reports')
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, blank=True, null=True)
    pet_name = models.CharField(max_length=100)
    species = models.CharField(max_length=50)
    breed = models.CharField(max_length=100, blank=True)
    color = models.CharField(max_length=100)
    size = models.CharField(max_length=15, choices=SIZE_CHOICES)
    age_estimate = models.CharField(max_length=50, help_text="Approximate age (e.g., 2 years, puppy, senior)")
    last_seen_location = models.TextField()
    last_seen_date = models.DateTimeField()
    description = models.TextField(help_text="Detailed description including behavior, distinctive marks, etc.")
    photo = models.ImageField(upload_to='lost_pets/', help_text="Upload a clear photo of the pet")
    additional_photos = models.TextField(blank=True, help_text="URLs or descriptions of additional photos")
    contact_phone = models.CharField(max_length=15)
    contact_email = models.EmailField(blank=True)
    reward_amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True, help_text="Reward amount in Indian Rupees (₹)")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='lost')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.pet_name} - {self.status}"