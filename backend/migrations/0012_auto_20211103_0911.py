# Generated by Django 3.2 on 2021-11-03 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0011_auto_20211103_0902'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='eligibility',
        ),
        migrations.RemoveField(
            model_name='project',
            name='number',
        ),
        migrations.AddField(
            model_name='project',
            name='branch',
            field=models.CharField(max_length=6000, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='learnings',
            field=models.CharField(max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='year',
            field=models.CharField(max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='duration',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='project',
            name='place',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='project',
            name='stipend',
            field=models.CharField(max_length=500),
        ),
    ]