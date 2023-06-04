# Generated by Django 4.2.1 on 2023-05-29 14:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clothes', '0001_initial'),
        ('souvenirs', '__first__'),
        ('food', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tours', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clothing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clothes.clothing')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.food')),
                ('souvenir', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='souvenirs.souvenir')),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tours.tour')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
