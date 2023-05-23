# Generated by Django 4.2.1 on 2023-05-23 17:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0004_alter_product_options_alter_comment_text'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.RemoveField(
            model_name='order',
            name='ordered',
        ),
        migrations.AlterField(
            model_name='category',
            name='categoryName',
            field=models.CharField(max_length=50, unique=True, verbose_name='Категории'),
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(max_length=255, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.CharField(max_length=255, verbose_name='Почта'),
        ),
        migrations.AlterField(
            model_name='order',
            name='first_name',
            field=models.CharField(max_length=255, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(max_length=255, verbose_name='Номер тел'),
        ),
        migrations.AlterField(
            model_name='order',
            name='place',
            field=models.CharField(max_length=255, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('ordered', 'Ordered'), ('shipped', 'Shipped')], default='ordered', max_length=20, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='order',
            name='zipcode',
            field=models.CharField(max_length=255, verbose_name='Почтовый индекс'),
        ),
    ]
