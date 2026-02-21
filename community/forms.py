from django import forms
from .models import ForumPost, LostPetReport, ForumReply

class ForumPostForm(forms.ModelForm):
    class Meta:
        model = ForumPost
        fields = ['category', 'post_type', 'title', 'content', 'image']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 6}),
        }

class ForumReplyForm(forms.ModelForm):
    class Meta:
        model = ForumReply
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write your reply...'}),
        }

class LostPetReportForm(forms.ModelForm):
    class Meta:
        model = LostPetReport
        fields = [
            'pet_name', 'species', 'breed', 'color', 'size', 'age_estimate',
            'last_seen_location', 'last_seen_date', 'description', 'photo',
            'contact_phone', 'contact_email', 'reward_amount', 'status'
        ]
        widgets = {
            'last_seen_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Describe the pet in detail, including any distinctive marks, behavior, or other identifying features...'}),
            'last_seen_location': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Provide specific location details (street address, landmarks, area description)...'}),
        }
        labels = {
            'reward_amount': 'Reward Amount (₹)',
        }
        help_texts = {
            'reward_amount': 'Optional reward amount in Indian Rupees (₹)',
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['photo'].required = True
        self.fields['photo'].help_text = "Upload a clear, recent photo of the pet"