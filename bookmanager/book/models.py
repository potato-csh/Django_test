from django.db import models


# Create your models here.
# 一
class BookInfo(models.Model):
    name = models.CharField(max_length=10, verbose_name='名称')
    pub_date = models.DateField(verbose_name='发布日期', null=True)
    readcount = models.IntegerField(default=0, verbose_name='发行数量')
    commentcount = models.IntegerField(default=0, verbose_name='评论数量')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        db_table = 'bookinfo'
        verbose_name = '图书'

    def __str__(self):
        return self.name

# 多
class PersonInfo(models.Model):
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female')
    )
    name = models.CharField(max_length=10, verbose_name='名称')
    gender = models.BooleanField(choices=GENDER_CHOICES, default=0, verbose_name='性别')
    description = models.CharField(max_length=200, null=True, verbose_name='描述信息')
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name='图书')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        db_table = 'personinfo'
        verbose_name = '人物信息'

    def __str__(self):
        return self.name
