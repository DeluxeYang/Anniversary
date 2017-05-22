from django.db import models
import datetime
# Create your models here.

class pic(models.Model):
    # 默认主键:id自增
    pic_title = models.CharField(max_length=40,null=True, blank=True)
    pic_time = models.DateTimeField(null=True, blank=True)
    pic_path = models.ImageField(upload_to='images/')
    pic_text = models.TextField(null=True, blank=True)

    def __str__(self):  # __unicode__ on Python 2
        pic_time = datetime.datetime.strftime(self.pic_time, '%Y-%m-%d')
        return self.pic_title + " " + pic_time
