# Generated by Django 3.2.9 on 2021-12-24 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web_lib', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'get_latest_by': 'published', 'verbose_name': 'Книга', 'verbose_name_plural': 'Книги'},
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='web_lib.author'),
            preserve_default=False,
        ),
    ]
