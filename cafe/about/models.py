from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(verbose_name='Цена')
    create_data = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    update_data = models.DateField(auto_now=True, verbose_name='Дата изменения')
    photo = models.ImageField(upload_to='images/%Y/%m/%d', null=True, blank=True, verbose_name='Фотография блюда')
    exists = models.BooleanField(default=True, verbose_name='Добавить в меню или нет?')
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['name', '-price']
        

class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    product = models.ManyToManyField(Product)
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        

class Tag(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    desctiption = models.TextField(null=True, blank=True, verbose_name='Описание')
    product = models.ManyToManyField(Product)
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
    

class Provider(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название компании')
    name_provider = models.CharField(max_length=50, verbose_name='Имя представителя')
    lastname_provider = models.CharField(max_length=50, verbose_name='Фамилия представителя')
    surname_provider = models.CharField(max_length=50, null=True, blank=True, verbose_name='Очество представителя')
    phone = models.CharField(max_length=20, verbose_name='Телефон представителя')
    adress = models.TextField(verbose_name='Адрес')

    def __str__(self) -> str:
        return self.name + '(' + self.name_provider + ' ' + self.lastname_provider + ')' + ' | ' + self.phone

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'
        
        
class Supplies(models.Model):
    number = models.IntegerField(verbose_name='Номер поставки')
    date_supplies = models.DateField(auto_now_add=True, verbose_name='Дата поставки')
    provider = models.OneToOneField(Provider, on_delete=models.PROTECT, verbose_name='Поставщик')
        
    def __str__(self) -> str:
        return str(self.number) + ' | ' + self.provider.__str__()
    
    class Meta:
        verbose_name = 'Поставка'
        verbose_name_plural = 'Поставки'
        

class PositionSupplies(models.Model):
    product = models.OneToOneField(Product, on_delete=models.PROTECT, verbose_name='Товар')
    supplies = models.OneToOneField(Supplies, on_delete=models.PROTECT, verbose_name='Поставка')
    count = models.IntegerField(verbose_name='Кол-во товара')
    
    def __str__(self) -> str:
        return self.product.__str__() + ' | ' + str(self.count)
    
    class Meta:
        verbose_name = 'Позиция поставки'
        verbose_name_plural = 'Позиция поставок'
        

class Order(models.Model):
    number = models.IntegerField(verbose_name='Номер заказа')
    name_customer = models.CharField(max_length=50, verbose_name='Имя покупателя')
    lastname_customer = models.CharField(max_length=50, verbose_name='Фамилия покупателя')
    surname_customer = models.CharField(max_length=50, null=True, blank=True, verbose_name='Очество покупателя')
    comment = models.TextField(null=True, blank=True, verbose_name='Комментаций')
    adress = models.TextField(verbose_name='Адрес доставки')
    method_delivery = models.TextField(verbose_name='Способ доставки')
    create_data = models.DateField(auto_now_add=True, null=True, blank=True, verbose_name='Дата создания')
    end_data = models.DateField(auto_now=True, null=True, blank=True, verbose_name='Дата завершения')
    
    def __str__(self) -> str:
        return self.name_customer + ' ' + self.lastname_customer + ' | ' + self.comment
    
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        

class PositionOrder(models.Model):
    order = models.OneToOneField(Order, on_delete=models.PROTECT, verbose_name='Заказ')
    product = models.OneToOneField(Product, on_delete=models.PROTECT, verbose_name='Товар')
    count = models.IntegerField(verbose_name='Количество')
    discount = models.IntegerField(null=True, blank=True, verbose_name='Скидка')
    
    def __str__(self) -> str:
        return self.product.__str__() + ' | ' + str(self.count)
    
    class Meta:
        verbose_name = 'Позиция заказа'
        verbose_name_plural = 'Позиции заказа'
        
        
class Сharacteristic(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    characteristic = models.TextField(verbose_name='Характеристика')
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Характеристика'
        verbose_name_plural = 'Характеристики'
        

class FullCharacteristic(models.Model):
    product = models.OneToOneField(Product, on_delete=models.PROTECT, verbose_name='Товар')
    characteristic = models.OneToOneField(Сharacteristic, on_delete=models.PROTECT, null=True, verbose_name='Характеристика товара')
    meaning = models.CharField(max_length=255, verbose_name='Значение')
    
    def __str__(self) -> str:
        return f'Характеристика | {self.meaning}'
    
    class Meta:
        verbose_name = 'Характеристика товара'
        verbose_name = 'Характеристи товаров'