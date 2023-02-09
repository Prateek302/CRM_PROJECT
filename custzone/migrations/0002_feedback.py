# Generated by Django 3.1 on 2020-08-11 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custzone', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=500)),
                ('contactno', models.CharField(max_length=15)),
                ('emailaddress', models.EmailField(max_length=254)),
                ('feedbacktext', models.CharField(max_length=100)),
                ('feedbackdate', models.CharField(max_length=20)),
            ],
        ),
    ]
