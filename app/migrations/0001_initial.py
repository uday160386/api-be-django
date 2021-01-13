# Generated by Django 3.1.5 on 2021-01-13 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medicines',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('description', models.TextField(max_length=360)),
                ('qty', models.IntegerField(default=1)),
            ],
        ),
    ]
