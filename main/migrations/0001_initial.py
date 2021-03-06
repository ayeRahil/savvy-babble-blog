# Generated by Django 4.0 on 2022-01-03 14:14

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('articleImage', models.ImageField(default='images/articledefault.jpg', upload_to='images/article/')),
                ('title_tag', models.CharField(default='Technology', max_length=256)),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('category', models.CharField(default='uncategorized', max_length=256)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]
