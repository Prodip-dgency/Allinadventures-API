# Generated by Django 4.0.5 on 2022-07-28 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0004_rename_slag_location_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='external_link',
            new_name='booking_url',
        ),
        migrations.AddField(
            model_name='activity',
            name='card_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='activity_card_image', to='activity.gallery'),
        ),
        migrations.AddField(
            model_name='activity',
            name='cover_image_mobile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='activity_cover_image_mobile', to='activity.gallery'),
        ),
        migrations.AddField(
            model_name='activity',
            name='level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='activity.level'),
        ),
        migrations.AddField(
            model_name='activity',
            name='required_age',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='cover_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='activity_cover_image', to='activity.gallery'),
        ),
    ]
