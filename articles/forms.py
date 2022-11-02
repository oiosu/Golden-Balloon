from django import forms
from .models import Article, Comment, Notice, Review, ReviewComment


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


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["title", "content", "image", "thumbnail"]


class ReviewCommentForm(forms.ModelForm):
    class Meta:
        model = ReviewComment
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
