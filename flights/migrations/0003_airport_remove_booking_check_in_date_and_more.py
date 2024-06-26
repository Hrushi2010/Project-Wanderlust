# Generated by Django 4.2.1 on 2024-05-23 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0002_delete_airport_remove_booking_status_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=3, unique=True)),
                ('city', models.CharField(max_length=64)),
            ],
        ),
        migrations.RemoveField(
            model_name='booking',
            name='check_in_date',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='passenger_email',
        ),
        migrations.AlterField(
            model_name='booking',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='booking',
            name='passenger_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='arrival_airport',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrivals', to='flights.airport'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='departure_airport',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departures', to='flights.airport'),
        ),
    ]
