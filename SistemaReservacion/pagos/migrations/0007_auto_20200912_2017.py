# Generated by Django 3.0.4 on 2020-09-13 01:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pagos', '0006_cliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagar',
            name='usuario',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='cliente',
        ),
    ]