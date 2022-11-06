from django.conf import settings
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill, Thumbnail
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
# like_users는 추후에 업로드할 예정입니다!


class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = ProcessedImageField(
        upload_to="articles/",
        blank=True,
        processors=[ResizeToFill(1200, 960)],
        format="JPEG",
        options={"quality": 80},
        null=True,
    )

    thumbnail = ProcessedImageField(
        upload_to="images/",
        blank=True,
        processors=[Thumbnail(200, 300)],
        format="JPEG",
        options={"quality": 80},
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="like_articles"
    )


class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Notice(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = ProcessedImageField(
        upload_to="images/%Y/%m/%d",
        blank=True,
        processors=[ResizeToFill(600, 600)],
        format="JPEG",
        options={"quality": 80},
        null=True,
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Review(models.Model):
    country = models.CharField(max_length=10)
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = ProcessedImageField(
        upload_to="images/%Y/%m/%d",
        blank=True,
        processors=[ResizeToFill(600, 600)],
        format="JPEG",
        options={"quality": 80},
        null=True,
    )
    # image = models.ImageField(upload_to="images/%Y/%m/%d")
    thumbnail = ProcessedImageField(
        upload_to="images/",
        blank=True,
        processors=[Thumbnail(400, 300)],
        format="JPEG",
        options={"quality": 80},
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="like_reviews"
    )
    grade = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="like_review"
    )


class ReviewComment(models.Model):
    content = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Product(models.Model):
    title = models.CharField(max_length=100)
    image = ProcessedImageField(
        upload_to="reviews/",
        blank=True,
        processors=[Thumbnail(400, 300)],
        format="JPEG",
        options={"quality": 80},
        null=True,
    )
    def __str__(self):
        return self.title


class Faq(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = ProcessedImageField(
        upload_to="images/%Y/%m/%d",
        blank=True,
        processors=[ResizeToFill(600, 600)],
        format="JPEG",
        options={"quality": 80},
        null=True,
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Qna(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = ProcessedImageField(
        upload_to="images/%Y/%m/%d",
        blank=True,
        processors=[ResizeToFill(600, 600)],
        format="JPEG",
        options={"quality": 80},
        null=True,
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class QnaComment(models.Model):
    content = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    qna = models.ForeignKey(Qna, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
