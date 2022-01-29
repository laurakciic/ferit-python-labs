from django.db import models
from django.db.models import constraints
from django.utils import timezone
from django.contrib.auth.models import User
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
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def comments_count(self):
        return image.comment_set.count()

    def vote_score(self):
        upvotes = self.vote_set.filter(upvote=True).count()
        downvotes = self.vote_set.filter(upvote=False).count()
        return upvotes - downvotes

    def vote_by(self,user):
        if user.is_authenticated:
            return Vote.objects.filter(user=user, image=self).first()
        else:
            return None

class Comment(TimeStamped):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    text = models.TextField(blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    approved = models.BooleanField(null=False, default=False)
    likecount = models.IntegerField(default=0)

    def __str__(self):
        return self.text[:80]

    def author(self):
        return self.user.username

    def is_approved(self):
        return self.approved

    def approve(self):
        self.approved=True
        self.save()

    def like_score(self):
        likes = self.like_set.filter(likecomment = True).count()
        dislikes = self.like_set.filter(likecomment = False).count()
        return likes-dislikes

class Vote(TimeStamped):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    upvote = models.BooleanField(null=False, default=True)
    
    class Meta:
        constraints= [
            models.UniqueConstraint(name='user_vote', fields=['image','user'])
        ]
    def __str__(self) :
        return f"{self.user.username} voted on {self.image.title}"
    def downvote(self):
        return not self.upvote

class Like(TimeStamped):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likecomment = models.BooleanField(null = False, default=False)
    class Meta:
        constraints=[
            models.UniqueConstraint(name='user_like', fields=['user','comment'])
        ]
    