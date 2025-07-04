# Generated by Django 4.2.17 on 2025-05-25 05:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reservation_app', '0005_reservation_date_reservation_guests_reservation_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='post',
        ),
        migrations.AddField(
            model_name='feedback',
            name='reservation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='feedbacks', to='reservation_app.reservation'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='patron',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='feedbacks', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='guests',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.IntegerField(choices=[(0, 'Requested'), (1, 'Confirmed')], default=0),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
