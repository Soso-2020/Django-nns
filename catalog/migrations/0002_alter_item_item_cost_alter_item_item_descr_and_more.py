# Generated by Django 4.2.5 on 2023-10-02 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_cost',
            field=models.IntegerField(default='150', verbose_name='Cost'),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_descr',
            field=models.TextField(default="It's empty, for a while, but soon some item will be here", help_text='Enter a description:', max_length=1000),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.FileField(default='blank.jpg', upload_to='catalog/static/img/'),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_name',
            field=models.CharField(default='Magic powder', max_length=50),
        ),
    ]
