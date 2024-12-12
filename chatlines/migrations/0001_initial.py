# Generated by Django 5.1.4 on 2024-12-11 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chatlines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_id', models.IntegerField()),
                ('role', models.CharField(max_length=100)),
                ('csv_file_path', models.CharField(max_length=1000)),
                ('chat_text_backend', models.CharField(max_length=10000)),
                ('tokens', models.IntegerField()),
                ('type', models.CharField(max_length=100)),
                ('function_name_called', models.CharField(max_length=1000)),
                ('response_status', models.CharField(max_length=100)),
                ('creation_tms', models.DateTimeField(editable=False)),
                ('last_update_tms', models.DateTimeField()),
            ],
        ),
    ]
