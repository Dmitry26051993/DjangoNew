# Generated by Django 4.2.4 on 2023-08-13 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_book_shop', '0002_alter_book_options_book_count_likes_comment_likes_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': 'книга', 'verbose_name_plural': 'книги'},
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(db_index=True, max_length=100, verbose_name='название книги'),
        ),
    ]
