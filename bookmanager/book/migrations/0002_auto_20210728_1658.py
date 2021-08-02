# Generated by Django 3.2.5 on 2021-07-28 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinfo',
            options={'verbose_name': '图书'},
        ),
        migrations.AlterModelOptions(
            name='personinfo',
            options={'verbose_name': '人物信息'},
        ),
        migrations.AddField(
            model_name='bookinfo',
            name='commentcount',
            field=models.IntegerField(default=0, verbose_name='评论数量'),
        ),
        migrations.AddField(
            model_name='bookinfo',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name='逻辑删除'),
        ),
        migrations.AddField(
            model_name='bookinfo',
            name='pub_date',
            field=models.DateField(null=True, verbose_name='发布日期'),
        ),
        migrations.AddField(
            model_name='bookinfo',
            name='readcount',
            field=models.IntegerField(default=0, verbose_name='发行数量'),
        ),
        migrations.AddField(
            model_name='personinfo',
            name='description',
            field=models.CharField(max_length=200, null=True, verbose_name='描述信息'),
        ),
        migrations.AddField(
            model_name='personinfo',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name='逻辑删除'),
        ),
        migrations.AlterField(
            model_name='bookinfo',
            name='name',
            field=models.CharField(max_length=10, verbose_name='名称'),
        ),
        migrations.AlterField(
            model_name='personinfo',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.bookinfo', verbose_name='图书'),
        ),
        migrations.AlterField(
            model_name='personinfo',
            name='gender',
            field=models.BooleanField(choices=[(0, 'male'), (1, 'female')], default=0, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='personinfo',
            name='name',
            field=models.CharField(max_length=10, verbose_name='名称'),
        ),
        migrations.AlterModelTable(
            name='bookinfo',
            table='bookinfo',
        ),
        migrations.AlterModelTable(
            name='personinfo',
            table='personinfo',
        ),
    ]
