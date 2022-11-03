from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Article, Comment, Notice, Review, ReviewComment
from .forms import ArticleForm, CommentForm, NoticeForm, ReviewForm, ReviewCommentForm

# Create your views here.
def index(request):

    articles = Article.objects.order_by("-pk")

    context = {
        "articles": articles,
    }
    return render(request, "articles/index.html", context)


@login_required
def create(request):

    if request.method == "POST":
        article_form = ArticleForm(request.POST, request.FILES)
        if article_form.is_valid():
            article = article_form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect("articles:index")
    else:
        article_form = ArticleForm()
    context = {
        "article_form": article_form,
    }
    return render(request, "articles/create.html", context)


def detail(request, pk):

    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = article.comment_set.order_by("-pk")

    context = {
        "article": article,
        "comment_form": comment_form,
        "comments": comments,
    }

    return render(request, "articles/detail.html", context)


def delete(request, pk):

    article = Article.objects.get(pk=pk)
    article.delete()

    return redirect("articles:index")


def update(request, pk):

    article = Article.objects.get(pk=pk)

    if request.method == "POST":
        article_form = ArticleForm(request.POST, request.FILES, instance=article)
        if article_form.is_valid():
            article_form.save()
            return redirect("articles:detail", pk)
    else:
        article_form = ArticleForm(instance=article)
    context = {
        "article_form": article_form,
    }
    return render(request, "articles/update.html", context)


@login_required
def c_create(request, pk):

    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)

    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment.save()

    return redirect("articles:detail", pk)


@login_required
def c_delete(request, a_pk, c_pk):

    comment = Comment.objects.get(pk=c_pk)
    comment.delete()

    return redirect("articles:detail", a_pk)


@login_required
def like(request, pk):

    article = Article.objects.get(pk=pk)

    if request.user in article.like_users.all():
        article.like_users.remove(request.user)
    else:
        article.like_users.add(request.user)

    return redirect("articles:index")


def notice(request):

    notices = Notice.objects.order_by("-pk")

    context = {
        "notices": notices,
    }

    return render(request, "articles/notice.html", context)


@login_required
def n_create(request):

    if request.method == "POST":
        notice_form = NoticeForm(request.POST, request.FILES)
        if notice_form.is_valid():
            notice = notice_form.save(commit=False)
            notice.user = request.user
            notice.save()
            return redirect("articles:notice")
    else:
        notice_form = NoticeForm()
    context = {
        "notice_form": notice_form,
    }
    return render(request, "articles/n_create.html", context)


def n_detail(request, pk):

    notice = Notice.objects.get(pk=pk)

    context = {
        "notice": notice,
    }

    return render(request, "articles/n_detail.html", context)


def n_delete(request, pk):

    notice = Notice.objects.get(pk=pk)
    notice.delete()

    return redirect("articles:notice")


def n_update(request, pk):

    notice = Notice.objects.get(pk=pk)

    if request.method == "POST":
        notice_form = NoticeForm(request.POST, request.FILES, instance=notice)
        if notice_form.is_valid():
            notice_form.save()
            return redirect("articles:n_detail", pk)
    else:
        notice_form = NoticeForm(instance=notice)
    context = {
        "notice_form": notice_form,
    }
    return render(request, "articles/n_update.html", context)


def reviews(request):

    reviews = Review.objects.order_by("-pk")

    context = {
        "reviews": reviews,
    }

    return render(request, "articles/reviews.html", context)


@login_required
def r_create(request):

    if request.method == "POST":
        review_form = ReviewForm(request.POST, request.FILES)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect("articles:reviews")
    else:
        review_form = ReviewForm()
    context = {
        "review_form": review_form,
    }
    return render(request, "articles/r_create.html", context)


@login_required
def r_detail(request, pk):

    review = Review.objects.get(pk=pk)
    review_comment_form = ReviewCommentForm()
    comments = review.reviewcomment_set.order_by("-pk")

    context = {
        "review": review,
        "review_comment_form": review_comment_form,
        "comments": comments,
    }

    return render(request, "articles/r_detail.html", context)


@login_required
def r_delete(request, pk):

    review = Review.objects.get(pk=pk)
    review.delete()

    return redirect("articles:reviews")


@login_required
def r_update(request, pk):

    review = Review.objects.get(pk=pk)

    if request.method == "POST":
        review_form = ReviewForm(request.POST, request.FILES, instance=review)
        if review_form.is_valid():
            review_form.save()
            return redirect("articles:r_detail", pk)
    else:
        review_form = ReviewForm(instance=review)
    context = {
        "review_form": review_form,
    }
    return render(request, "articles/r_update.html", context)


@login_required
def r_c_create(request, pk):

    review = Review.objects.get(pk=pk)

    comment = request.POST.get("comment")

    if comment != "":
        user = request.user
        ReviewComment.objects.create(content=comment, user=user, review=review)

    return redirect("articles:r_detail", pk)


@login_required
def r_c_delete(request, a_pk, c_pk):

    comment = ReviewComment.objects.get(pk=c_pk)
    comment.delete()

    return redirect("articles:r_detail", a_pk)


@login_required
def r_like(request, pk):

    review = Review.objects.get(pk=pk)

    if request.user in review.like_users.all():
        review.like_users.remove(request.user)
    else:
        review.like_users.add(request.user)

    return redirect("articles:reviews")
