# Generated by Django 2.0.3 on 2018-04-01 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_egginfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='egginfo',
            name='breed',
            field=models.CharField(default='Some Chicken', max_length=100),
        ),
        migrations.AlterField(
            model_name='egginfo',
            name='sizeOfEgg',
            field=models.CharField(choices=[('Quail', 'Quail'), ('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large'), ('Jumbo', 'Jumbo')], default='Small', max_length=100),
        ),
        migrations.AlterField(
            model_name='egginfo',
            name='typeOfEgg',
            field=models.CharField(choices=[('Chicken', 'Chicken'), ('Turkey', 'Turkey'), ('Medium', 'Medium'), ('Large', 'Large'), ('Jumbo', 'Jumbo')], default='Chicken', max_length=100),
        ),
    ]
