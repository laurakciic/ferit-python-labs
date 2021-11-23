from django.db import models

# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length=255, unique=True, blank=False)
    url = models.CharField(max_length=512)
    description = models.TextField(blank=True)
    pub_date = models.DateTimeField('Published at')
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)

    def __str__(self):
        return "%d) %s"%(self.id, self.title)

class Comment(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    text = models.TextField(blank=False)
    nick = models.CharField(max_length=128, blank=False)
    
    def __str__(self):
        return "%d) %s"%(self.id, self.nick)
