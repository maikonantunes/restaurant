# Generated by Django 3.2.7 on 2021-09-22 04:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('method_of_preparation', '0001_initial'),
        ('ingredient', '0002_remove_ingredient_unit_type'),
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipes',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='image_food',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='ingredient',
            field=models.ManyToManyField(blank=True, null=True, to='ingredient.Ingredient'),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='method_preparation',
            field=models.ManyToManyField(blank=True, null=True, to='method_of_preparation.MethodPreparation'),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
