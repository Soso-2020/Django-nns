# Generated by Django 4.2.2 on 2023-09-21 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=50)),
                ('item_cost', models.IntegerField(verbose_name='Cost')),
                ('item_descr', models.TextField(help_text='Enter a description:', max_length=1000)),
                ('item_image', models.FileField(default='blank.jpg', upload_to='img/')),
            ],
        ),
    ]
