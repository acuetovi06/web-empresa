# Generated by Django 5.2 on 2025-05-15 16:00

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="page",
            name="content",
            field=ckeditor.fields.RichTextField(verbose_name="Contenido"),
        ),
    ]
