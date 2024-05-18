# Generated by Django 4.2.13 on 2024-05-18 14:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            'contacts',
            '0002_contact_facebook_contact_instagram_contact_twitter',
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='facebook',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='instagram',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='twitter',
        ),
        migrations.AddField(
            model_name='contact',
            name='img_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'platform',
                    models.CharField(
                        choices=[
                            ('facebook', 'Facebook'),
                            ('instagram', 'Instagram'),
                            ('twitter', 'Twitter'),
                        ],
                        max_length=10,
                    ),
                ),
                ('username', models.CharField(max_length=100)),
                (
                    'contact',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to='contacts.contact',
                    ),
                ),
            ],
        ),
    ]
