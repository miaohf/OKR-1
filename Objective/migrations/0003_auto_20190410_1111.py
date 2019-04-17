# Generated by Django 2.2 on 2019-04-10 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Objective', '0002_auto_20190403_2234'),
    ]

    operations = [
        migrations.AddField(
            model_name='objective',
            name='code',
            field=models.CharField(default='', max_length=20, verbose_name='编号'),
        ),
        migrations.AddField(
            model_name='objective',
            name='time_description',
            field=models.CharField(default='', max_length=20, verbose_name='年度'),
        ),
        migrations.AlterField(
            model_name='action',
            name='complete_date',
            field=models.DateField(verbose_name='完成时间'),
        ),
        migrations.AlterField(
            model_name='action',
            name='content',
            field=models.CharField(default='', max_length=500, verbose_name='行动内容'),
        ),
        migrations.AlterField(
            model_name='action',
            name='correlative_leader',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='相关部门责任人'),
        ),
        migrations.AlterField(
            model_name='action',
            name='local_leader',
            field=models.CharField(default='', max_length=100, verbose_name='本部门责任人'),
        ),
        migrations.AlterField(
            model_name='action',
            name='status',
            field=models.IntegerField(choices=[(1, 'Pending'), (2, 'Done'), (3, 'Warning')], verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='objective',
            name='department',
            field=models.CharField(max_length=20, verbose_name='部门'),
        ),
        migrations.AlterField(
            model_name='objective',
            name='key_result',
            field=models.CharField(max_length=200, verbose_name='关键结果'),
        ),
        migrations.AlterField(
            model_name='objective',
            name='leader_assessment_score',
            field=models.IntegerField(default=0, verbose_name='领导评分'),
        ),
        migrations.AlterField(
            model_name='objective',
            name='objective',
            field=models.CharField(max_length=200, verbose_name='目标'),
        ),
        migrations.AlterField(
            model_name='objective',
            name='self_assessment_score',
            field=models.IntegerField(default=0, verbose_name='部门自评'),
        ),
    ]