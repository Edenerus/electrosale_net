from django.db import models


class Product(models.Model):
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    title = models.CharField(max_length=50, verbose_name='Название')
    model = models.CharField(max_length=50, verbose_name='Модель')
    date_release = models.DateTimeField(blank=True, null=True, verbose_name='Дата выхода продукта на рынок')

    def __str__(self):
        return self.title


class Provider(models.Model):
    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'

    class Types(models.IntegerChoices):
        Factory = 0, 'Завод'
        RetailNetwork = 1, 'Розничная сеть'
        IE = 2, 'Индивидуальный предприниматель'  # IE - Individual Entrepreneur

    title = models.CharField(max_length=50, unique=True, verbose_name='Название')
    type = models.PositiveSmallIntegerField(choices=Types.choices, default=0, verbose_name='Тип звена')

    # contacts
    email = models.EmailField(unique=True, verbose_name='Email')
    country = models.CharField(max_length=50, verbose_name='Страна')
    city = models.CharField(max_length=50, verbose_name='Город')
    street = models.CharField(max_length=100, verbose_name='Улица')
    # CharField т.к нам точно неизвестен Номер дома, на случай если указывается цифра с буквой, например, 2-а
    house = models.CharField(max_length=50, verbose_name='Номер дома')

    products = models.ManyToManyField(Product, blank=True, verbose_name='Продукты')
    provider = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True,
                                 verbose_name='Поставщик', related_name='supplier')
    debt = models.DecimalField(default=0, decimal_places=2, max_digits=10, verbose_name='Задолженность')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.title
