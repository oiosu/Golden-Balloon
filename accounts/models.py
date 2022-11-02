from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.processors import ResizeToFill
from imagekit.models import ProcessedImageField

# Create your models here.
class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    user_img = ProcessedImageField(upload_to="images/",
                                    blank=True,
                                    processors=[ResizeToFill(60, 60)],
                                    format="JPEG",
                                    options={"quality": 30},
                                    null=True,
                                    )
    @property
    def full_name(self):
        return f'{self.last_name}{self.first_name}'