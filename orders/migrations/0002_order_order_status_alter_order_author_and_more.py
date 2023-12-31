# Generated by Django 4.2.2 on 2023-06-18 20:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('Waiting Offer', 'Waiting Offer'), ('Awaiting Delivery', 'Awaiting Delivery'), ('Incomplete', 'Incomplete'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], default='Waiting Offer', max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.supplier'),
        ),
    ]
