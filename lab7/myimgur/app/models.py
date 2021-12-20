from django.db import models
from django.utils import timezone

# Create your models here.
class TimeStamped(models.Model):
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = timezone.now()

        self.updated_at = timezone.now()
        return super(TimeStamped, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class Image(TimeStamped):
    title = models.CharField(max_length=128, unique=True, blank=False)
    url = models.CharField(max_length=512)
    description = models.TextField(blank=True)
    pub_date = models.DateTimeField('Published at')
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def comments_count(self):
        return image.comment_set.count()

    def votes(self):
        return self.upvotes - self.downvotes

class Comment(TimeStamped):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    text = models.TextField(blank=False)
    author = models.CharField(max_length=256, blank=False)

    def __str__(self):
        return self.text[:80]

    


        
