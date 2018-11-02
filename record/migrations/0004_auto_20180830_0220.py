# Generated by Django 2.0.3 on 2018-08-29 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0003_auto_20180823_0027'),
    ]

    operations = [
        migrations.CreateModel(
            name='Signature',
            fields=[
                ('id', models.AutoField(max_length=10, primary_key=True, serialize=False)),
                ('file', models.ImageField(upload_to='signatures/%Y/%m/%d')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'signature',
                'verbose_name_plural': 'signatures',
            },
        ),
        migrations.AddField(
            model_name='dailyrecord',
            name='signature',
            field=models.ManyToManyField(blank=True, to='record.Signature'),
        ),
    ]