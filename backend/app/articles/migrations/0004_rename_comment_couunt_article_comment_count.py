# Generated by Django 4.1.5 on 2023-02-03 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0003_rename_title_article_book_author_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="article",
            old_name="comment_count",
            new_name="comment_count",
        ),
    ]