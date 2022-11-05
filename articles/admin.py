from django.contrib import admin
from .models import Notice, Faq, Qna, Review

# Register your models here.

admin.site.register(Notice)
admin.site.register(Faq)
admin.site.register(Qna)
admin.site.register(Review)
