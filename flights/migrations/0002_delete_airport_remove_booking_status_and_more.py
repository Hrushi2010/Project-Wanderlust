# Generated by Django 4.2.1 on 2024-05-23 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Airport',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='status',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='user',
        ),
        migrations.AddField(
            model_name='booking',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='booking',
            name='check_in_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='passenger_email',
            field=models.EmailField(default='default@example.com', max_length=254),
        ),
        migrations.AddField(
            model_name='booking',
            name='passenger_name',
            field=models.CharField(default='Default Name', max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='arrival_airport',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='flight',
            name='departure_airport',
            field=models.CharField(max_length=50),
        ),
    ]
