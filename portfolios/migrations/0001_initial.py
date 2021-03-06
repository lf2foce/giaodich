# Generated by Django 4.0 on 2021-12-25 09:29

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=255)),
                ('action', models.CharField(max_length=255)),
                ('shares', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=4, max_digits=11)),
                ('symbol', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('canceled', 'Canceled'), ('executed', 'Executed')], default='pending', max_length=10)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trading_transactions', to='auth.user')),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
    ]
