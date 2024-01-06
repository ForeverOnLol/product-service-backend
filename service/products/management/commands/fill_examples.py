from django.core.management.base import BaseCommand
from django.core.files.uploadedfile import SimpleUploadedFile
from products.models import Catalog, Product
from django.db import transaction


class Command(BaseCommand):
    help = 'Заполнить бд тестовыми даными'

    def handle(self, *args, **options):
        with transaction.atomic():
            # Section.objects.all().delete()
            # SubsectionGroup.objects.all().delete()
            # Subsection.objects.all().delete()
            # Product.objects.all().delete()
            #
            # Section(title='Каталог ножей', slug='catalog-knifes').save()
            # Section(title='Подарочные ножи', slug='podarochniye-knifes').save()
            #
            # catalog_instance = Section.objects.get(title='Каталог ножей')
            #
            # subsection_category = SubsectionGroup(title='Категория ножей', section=catalog_instance, slug='knife-category')
            # subsection_category.save()
            #
            # subsection_producing = SubsectionGroup(title='Производство ножей', section=catalog_instance, slug='knife-producing')
            # subsection_producing.save()
            #
            # subsection_1 = Subsection(title='Ножи охотничьи', description='Ножи для настоящих мужиков (охотников)',
            #                           subsection_group=subsection_category, slug='hunter-knife')
            # subsection_1.save()
            #
            # subsection_2 = Subsection(title='Ножи зик', description='Ножи для настоящих зиковцев', slug='zick-knife',
            #                           subsection_group=subsection_producing)
            # subsection_2.save()
            #
            # with open("products/management/commands/default_product_photo.jpg", "rb") as photo_file:
            #     photo_content = photo_file.read()
            # default_photo_file = SimpleUploadedFile("default_photo.jpg", photo_content, content_type="image/jpeg")
            #
            # product_1 = Product(title='Кашерный нож для кэшерных рибят', comments_counter=0,
            #                     description='Рандомное описание', price=100, slug='cacherniy-knife',
            #                     photo=default_photo_file)
            # product_1.save()
            # product_1.subsection.set([subsection_1])
            # product_2 = Product(title='Зик нож для зэк', description='Рандомное описание зика', slug='zikzik1',
            #                     price=200, comments_counter=0,
            #                     photo=default_photo_file)
            # product_2.save()
            # product_2.subsection.set([subsection_2])

            Catalog.objects.all().delete()
            Product.objects.all().delete()

            Catalog(title='Каталог ножей', slug='catalog-knifes').save()
            Catalog(title='Подарочные ножи', slug='podarochniye-knifes').save()
            catalog_zero_lvl = Catalog.objects.get(title='Каталог ножей')

            Catalog(title='Категория ножей', parent=catalog_zero_lvl, slug='knife-category').save()
            Catalog(title='Производство ножей', parent=catalog_zero_lvl, slug='knife-producing').save()
            catalog_first_lvl_1 = Catalog.objects.get(title='Категория ножей')
            catalog_first_lvl_2 = Catalog.objects.get(title='Производство ножей')

            Catalog(title='Ножи охотничьи', description='Ножи для настоящих мужиков (охотников)',
                    parent=catalog_first_lvl_1, slug='hunter-knife').save()
            Catalog(title='Ножи зик', description='Ножи для настоящих зиковцев', slug='zick-knife',
                    parent=catalog_first_lvl_2).save()
            catalog_second_lvl_1 = Catalog.objects.get(title='Ножи охотничьи')
            catalog_second_lvl_2 = Catalog.objects.get(title='Ножи охотничьи')

            with open("products/management/commands/default_product_photo.jpg", "rb") as photo_file:
                photo_content = photo_file.read()
            default_photo_file = SimpleUploadedFile("default_photo.jpg", photo_content, content_type="image/jpeg")

            product_1 = Product(title='Кашерный нож для кэшерных рибят', comments_counter=0,
                                description='Рандомное описание', price=100, slug='cacherniy-knife',
                                photo=default_photo_file)
            product_1.save()
            product_1.catalog.set([catalog_second_lvl_1])

            product_2 = Product(title='Зик нож для зэк', description='Рандомное описание зика', slug='zikzik1',
                                price=200, comments_counter=0,
                                photo=default_photo_file)
            product_2.save()
            product_2.catalog.set([catalog_second_lvl_2])


