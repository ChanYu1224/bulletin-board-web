# Generated by Django 3.2.12 on 2022-03-08 05:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.UUID('e6a0ac38-6009-4be3-aaca-c0821fafdf38'), primary_key=True, serialize=False),
        ),
    ]
