from django.db import models


class Product(models.Model):
    class Category(models.TextChoices):
        SEM_CATEGORIA = 'SEM-CAT', 'Sem Categoria'
        BONE = 'BONE', 'Boné'
        ESPMASCULINO = 'ESP-MASC', 'Esportiva - Masculino'
        ESPFEMININO = 'ESP-FEM', 'Esportiva - Feminino'
        SOCMASCULINO = 'SOC-MASC', 'Social - Masculino'
        SOCFEMININO = 'SOC-FEM', 'Social - Feminino'
        LINGERIE = 'LINGERIE', 'Lingerie'
        CASUAL = 'CASUAL', 'Casual'
        JEANS = 'JEANS', 'Jeans'
        TENISMASCULINO = 'TEN-MASC', 'Tenis - Masculino'
        TENISFEMININO = 'TEN-FEM', 'Tenis - Feminino'
        SANDALIA = 'SANDALIAS', 'Sandálias'
        ACESSORIOS = 'ACESSORIOS', 'Acessórios'
        OUTROS = 'OUTROS', 'Outros'

    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False, verbose_name='Nome')
    category = models.CharField(
        max_length=20,
        choices=Category.choices,
        default=Category.SEM_CATEGORIA,
        verbose_name='Categoria',
    )
    sale_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        blank=False,
        verbose_name='Preço de Venda',
    )
    cost_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        blank=False,
        verbose_name='Preço de Custo',
    )
    quantity = models.IntegerField(default=0, verbose_name='Quantidade')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Data de Criação'
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='Data de Atualização'
    )
    low_quantity = models.IntegerField(default=0, verbose_name='Estoque Baixo')

    is_active = models.BooleanField(default=True, verbose_name='Ativo')

    def __str__(self):
        return self.name

    def soft_delete(self):
        self.is_active = False
        self.save()
