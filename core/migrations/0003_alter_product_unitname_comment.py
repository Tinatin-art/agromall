# Generated by Django 4.2.1 on 2023-05-18 18:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_order_ordered_orderitem_ordered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='unitName',
            field=models.CharField(choices=[('гр', 'грамм'), ('кг', 'килограмм'), ('литр', 'литр'), ('шт', 'штук')], default='гр', max_length=50),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Отзыв')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=False)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='core.product')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Комментария',
                'verbose_name_plural': 'Комментарии',
                'ordering': ['-created_on'],
                'indexes': [models.Index(fields=['created_on'], name='core_commen_created_6224c6_idx')],
            },
        ),
    ]
