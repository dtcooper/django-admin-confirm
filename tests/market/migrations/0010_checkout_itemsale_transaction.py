# Generated by Django 3.1.7 on 2021-03-10 23:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0009_auto_20210304_0355'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateField(auto_created=True)),
                ('total', models.DecimalField(decimal_places=2, editable=False, max_digits=5)),
                ('currency', models.CharField(choices=[('CAD', 'CAD'), ('USD', 'USD')], max_length=3)),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.shop')),
            ],
        ),
        migrations.CreateModel(
            name='ItemSale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, editable=False, max_digits=5)),
                ('currency', models.CharField(choices=[('CAD', 'CAD'), ('USD', 'USD')], max_length=3)),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='market.item')),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_sales', to='market.transaction')),
            ],
        ),
        migrations.CreateModel(
            name='Checkout',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('market.transaction',),
        ),
    ]
