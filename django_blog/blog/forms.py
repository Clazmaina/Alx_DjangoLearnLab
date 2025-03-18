from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Post
from .models import Comment

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

        tags = forms.CharField(required=False)

    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['tags'].initial = ', '.join(tag.name for tag in self.instance.tags.all())

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        instance.tags.set(*[tag.strip() for tag in self.cleaned_data['tags'].split(',') if tag.strip()])
        return instance

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']