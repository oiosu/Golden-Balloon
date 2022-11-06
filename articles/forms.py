from django import forms
from .models import Article, Comment, Notice, Review, ReviewComment, Faq, Qna, Product


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
        fields = ["country", "title", "content", "grade", "image", "thumbnail"]
        labels = {
            "country": "다녀온 나라",
            "title": "후기 제목",
            "content": "후기 내용",
            "image": "사진 업로드",
            "grade": "이번 여행에 점수를 주자면? (1~5)",
            "thumbnail": "대표 사진",
        }


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
                    "style": "color: #c6c6c6; border: 1px solid #c6c6c6; height: 40px; resize: none; width: 45rem; padding: 0.4rem 0; display: inline-block;",
                }
            ),
        }
        labels = {
            "content": "댓글을 집력해주세요",
        }


class FaqForm(forms.ModelForm):
    class Meta:
        model = Faq
        fields = ["title", "content", "image"]


class QnaForm(forms.ModelForm):
    class Meta:
        model = Qna
        fields = ["title", "content", "image"]

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["title", "image"]