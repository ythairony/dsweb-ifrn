# Generated by Django 4.0.6 on 2023-06-28 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('caridade', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='evento',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='caridade.evento'),
        ),
    ]
