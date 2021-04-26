from django.db import models

# Create your models here.
class Track(models.Model):
    # id is created automatically as primary key
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)  # can be Null
    url = models.URLField() # a CharField with URL validation
    created_at = models.DateTimeField(auto_now_add=True)
