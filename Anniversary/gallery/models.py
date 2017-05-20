from django.db import models

# Create your models here.

class pic(models.Model):
    # 默认主键:id自增
    pic_title = models.CharField(max_length=40,null=True, blank=True)
    pic_time = models.DateTimeField(null=True, blank=True)
    pic_path = models.ImageField(upload_to='images/')
    pic_text = models.TextField()

    def __str__(self):  # __unicode__ on Python 2
        return self.pic_title