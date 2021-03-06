# Generated by Django 2.0.2 on 2018-03-07 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formapagamento',
            name='sigla',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='order',
            name='cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Cliente', verbose_name='Cliente '),
        ),
        migrations.AlterField(
            model_name='order',
            name='formapagamento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.FormaPagamento', verbose_name='Forma de Pagamento '),
        ),
        migrations.AlterField(
            model_name='order',
            name='prazopagamento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.PrazoPagamento', verbose_name='Prazo de Pagamento '),
        ),
    ]
