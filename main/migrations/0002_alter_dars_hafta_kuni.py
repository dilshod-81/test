# Generated by Django 4.0.2 on 2022-02-10 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dars',
            name='hafta_kuni',
            field=models.SmallIntegerField(choices=[(1, 'Dushanba'), (2, 'Seshanba'), (3, 'Chorshanba'), (4, 'Payshanba'), (5, 'Juma'), (6, 'Shanba'), (7, 'Yakshanba')]),
        ),
    ]
