from django.db import models
import datetime
from django.utils.timezone import get_default_timezone
# Create your models here.
class letter(models.Model):
    letter_title = models.CharField(max_length=40,null=True, blank=True)
    letter_time = models.DateTimeField(null=True, blank=True)
    letter_to = models.CharField(max_length=40,null=True, blank=True)
    letter_text = models.TextField(null=True, blank=True)
    letter_from = models.TextField(null=True, blank=True)

    def __str__(self):  # 数据库为UTC时间，这里要手动的根据TIME_ZONE转换回来
        letter_time = self.letter_time.astimezone(get_default_timezone()).strftime('%Y-%m-%d')
        return self.letter_title + " " + letter_time

class pic(models.Model):
    # 默认主键:id自增
    pic_title = models.CharField(max_length=40,null=True, blank=True)
    pic_time = models.DateTimeField(null=True, blank=True)
    pic_path = models.ImageField(upload_to='images/')
    pic_text = models.TextField(null=True, blank=True)

    def __str__(self):  # 数据库为UTC时间，这里要手动的根据TIME_ZONE转换回来
        pic_time = self.pic_time.astimezone(get_default_timezone()).strftime('%Y-%m-%d')
        return self.pic_title + " " + pic_time