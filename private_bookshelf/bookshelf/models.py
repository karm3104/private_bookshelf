from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Bookshelf(models.Model):
    """日記モデル"""

    user = models.ForeignKey(User, verbose_name="ユーザー", on_delete= models.PROTECT)
    title = models.CharField(verbose_name="タイトル", max_length= 100)
    auther = models.CharField(verbose_name="著作者", max_length= 100)
    publisher = models.CharField(verbose_name="出版社", blank=True, null= True, max_length= 100)
    isbnum = models.CharField(verbose_name="ISBN", blank=True, null= True, max_length= 100)
    comment = models.TextField(verbose_name="コメント", blank=True, null= True)
    group = models.CharField(verbose_name="グループ", max_length= 100, default="None")
    readpage = models.CharField(verbose_name="しおり", default= "0ページ", max_length= 100)
    evaluation = models.IntegerField(verbose_name="評価", blank=True, null= True, validators=[MinValueValidator(1), MaxValueValidator(5)])
    photo = models.ImageField(verbose_name="写真", blank=True, null= True)
    created_at = models.DateTimeField(verbose_name="作成日時", auto_now_add= True)
    updated_at = models.DateTimeField(verbose_name="更新日時", auto_now= True)

    class Meta:
        verbose_name_plural = "Bookshelf"

    def __str__(self):
        return self.title