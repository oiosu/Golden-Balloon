from django import forms
from .models import Article, Comment, Notice


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "content", "image", "thumbnail"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "content",
        ]
        widgets = {
            "content": forms.Textarea(
                attrs={
                    "placeholder": "",
                    "style": "height: 40px; resize: none; width: 100%;",
                }
            ),
        }
        labels = {
            "content": "댓글",
        }


class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ["title", "content", "image"]
