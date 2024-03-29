# Generated by Django 4.0.5 on 2022-07-25 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0002_alter_activity_options_alter_category_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.CharField(max_length=500, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='location',
            name='card_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='location_card_image', to='activity.gallery'),
        ),
        migrations.AddField(
            model_name='location',
            name='cover_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='location_cover_image', to='activity.gallery'),
        ),
        migrations.AddField(
            model_name='location',
            name='cover_image_mobile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='location_cover_image_mobile', to='activity.gallery'),
        ),
        migrations.AddField(
            model_name='location',
            name='desciption',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='gps_data',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='slag',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
