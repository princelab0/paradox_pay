# Generated by Django 4.0.2 on 2022-03-14 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('esewa', '0008_product_payment_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='ipn',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='esewa.esewa'),
        ),
    ]
