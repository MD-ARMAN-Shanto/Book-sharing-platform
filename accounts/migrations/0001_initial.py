# Generated by Django 2.1.7 on 2019-03-11 21:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BookList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(max_length=30)),
                ('book_author', models.CharField(max_length=30)),
                ('book_edition', models.CharField(max_length=10)),
                ('book_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('user_phn', models.CharField(max_length=15)),
                ('book_image', models.FileField(upload_to='')),
                ('user', models.ForeignKey(default=None, on_delete='models.CASCADE', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]