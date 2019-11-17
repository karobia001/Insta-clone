from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from pyuploadcare.dj.models import ImageField
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    email = models.EmailField()
    phone_number = PhoneNumberField(max_length=10, blank=True)
    location = models.CharField(max_length=30, blank=True)
    profile_pic = models.ImageField(upload_to = 'photos/',blank=True)
    
    
    User.profile = property(lambda u: Profile.objects.get_or_create(user=u)[0])

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:

        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):

    instance.profile.save()

@classmethod
def get_other_userprofiles(cls,user_id):
    profiles = Profile.objects.all()
    other_userprofiles = []
    for profile in profiles:
        if profile.user_id !=user_id:
             other_userprofiles.append(profile)
    return other_userprofiles


def generate_id():
        n = 10
        random = str.ascii_uppercase + str.ascii_lowercase + str.digits
        return ''.join(choice(random) for _ in range(n))


class Posts(VoteModel,models.Model):
    image = models.ImageField(upload_to = 'photos/',blank=True)
    post_date = models.DateTimeField(auto_now_add = True)
    description = models.TextField(max_length=500, blank=True)
    user = models.ForeignKey(User)
    location = models.CharField(max_length=30, blank=True)
    slug = models.SlugField(max_length=10,unique=True, default=generate_id)
    upvote_count = models.PositiveIntegerField(default=0)
    downvote_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.description

    class Meta:
        ordering = ['-post_date']

    def get_absolute_url(self):
        return reverse('posts:view', kwargs={'slug': self.slug})

    @classmethod
    def get_posts(cls):
        post = Posts.objects.all()

        return post
    @classmethod
    def get_single_post(cls, pk):
        post = cls.objects.get(pk=pk)
        return post

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url