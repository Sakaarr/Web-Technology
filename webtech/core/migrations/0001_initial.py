# Generated by Django 4.2.10 on 2024-08-05 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyFormModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('example_select', models.IntegerField()),
                ('example_textarea', models.TextField()),
            ],
        ),
    ]
