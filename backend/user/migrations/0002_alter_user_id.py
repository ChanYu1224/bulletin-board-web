# Generated by Django 3.2.12 on 2022-03-04 06:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.UUID('8a4cc451-4125-4fa9-acec-3afe23b95f62'), primary_key=True, serialize=False),
        ),
    ]