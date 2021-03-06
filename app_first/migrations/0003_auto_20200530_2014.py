# Generated by Django 2.1 on 2020-05-30 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_first', '0002_auto_20200529_1000'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='app_first.Publisher'),
            preserve_default=False,
        ),
    ]
