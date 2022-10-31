from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey

from online_store2 import settings


class Category(MPTTModel):
    """
    Category Table implimented with MPTT.
    """

    name = models.CharField(
        verbose_name=_("Category Name"),
        help_text=_("Required and unique"),
        max_length=255,
        unique=True,
    )
    slug = models.SlugField(verbose_name=_("Category safe URL"), max_length=255, unique=True)
    parent = TreeForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="children")
    is_active = models.BooleanField(default=True)

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def get_absolute_url(self):
        return reverse("store:category_list", args=[self.slug])

    def __str__(self):
        return self.name


class ProductType(models.Model):
    """
    ProductType Table will provide a list of the different types
    of products that are for sale.
    """

    name = models.CharField(verbose_name=_("Product Name"), help_text=_("Required"), max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
      # RESTRICT e pt a preveni stergerea, in caz de stergem product_types

    class Meta:
        verbose_name = _("Product Type")
        verbose_name_plural = _("Product Types")

    def __str__(self):
        return self.name


class ProductSpecification(models.Model):
    """
    The Product Specification Table contains product
    specifiction or features for the product types.
    """

    product_type = models.ForeignKey(ProductType, on_delete=models.RESTRICT)
    name = models.CharField(verbose_name=_("Name"), help_text=_("Required"), max_length=255)

    class Meta:
        verbose_name = _("Product Specification")
        verbose_name_plural = _("Product Specifications")

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    The Product table contining all product items.
    """

    product_type = models.ForeignKey(ProductType, on_delete=models.RESTRICT)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    title = models.CharField(
        verbose_name=_("title"),
        help_text=_("Required"),
        max_length=255,
    )
    description = models.TextField(verbose_name=_("description"), help_text=_("Not Required"), blank=True)
    slug = models.SlugField(max_length=255)
    regular_price = models.DecimalField(
        verbose_name=_("Regular price"),
        help_text=_("Maximum 999.99"),
        error_messages={
            "name": {
                "max_length": _("The price must be between 0 and 999.99."),
            },
        },
        max_digits=5,
        decimal_places=2,
    )
    discount_price = models.DecimalField(
        verbose_name=_("Discount price"),
        help_text=_("Maximum 999.99"),
        error_messages={
            "name": {
                "max_length": _("The price must be between 0 and 999.99."),
            },
        },
        max_digits=5,
        decimal_places=2,
    )
    is_active = models.BooleanField(
        verbose_name=_("Product visibility"),
        help_text=_("Change product visibility"),
        default=True,
    )
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)
    users_wishlist = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="user_wishlist", blank=True)


    class Meta:
        ordering = ("-created_at",)
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def get_absolute_url(self):
        return reverse("store:product_detail", args=[self.slug])

    def __str__(self):
        return self.title


class ProductSpecificationValue(models.Model):
    """
    The Product Specification Value table holds each of the
    products individual specification or bespoke features.
    """

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    specification = models.ForeignKey(ProductSpecification, on_delete=models.RESTRICT)
    value = models.CharField(
        verbose_name=_("value"),
        help_text=_("Product specification value (maximum of 255 words"),
        max_length=255,
    )

    class Meta:
        verbose_name = _("Product Specification Value")
        verbose_name_plural = _("Product Specification Values")

    def __str__(self):
        return self.value


class ProductImage(models.Model):
    """
    The Product Image table.
    """

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_image")
    image = models.ImageField(
        verbose_name=_("image"),
        help_text=_("Upload a product image"),
        upload_to="images/",
        default="images/default.png",
    )
    alt_text = models.CharField(
        verbose_name=_("Alternative text"),
        help_text=_("Please add alturnative text"),
        max_length=255,
        null=True,
        blank=True,
    )
    is_feature = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Product Image")
        verbose_name_plural = _("Product Images")




# from django.contrib.auth.models import User
# from django.db import models
#
# from django.urls import reverse
#
#
# # reverse ne va permite sa construim un url in models (acel url din fct de jos)
# # class SubcategoryManager(models.Manager):
# #     def get_queryset(self):
# #         return super(SubcategoryManager, self).get_queryset().filter(is_active=True, in_stock=True, )
# from online_store2 import settings
#
#
# class ProductManager(models.Manager):
#     def get_queryset(self):
#         return super(ProductManager, self).get_queryset().filter(is_active=True, in_stock=True, )
#
#
# class Category(models.Model):
#     name = models.CharField(max_length=255, db_index=True)
#     slug = models.SlugField(max_length=255, unique=True)
#
#     # Slug is a newspaper term.A slug is a short label
#     # for something, containing only letters, numbers, underscores or hyphens.
#     # They’re generally used in URLs.
#
#     class Meta:
#         verbose_name_plural = 'Categories'
#
#     def get_absolute_url(self):
#         return reverse('store:category_list', args=[self.slug])
#
#     # (aceasta functie creeaza legatura dintre pagina de home si cea cu categoriile->
#     # folosesc asta pt a accesa categoriile(inele, coliere etc))
#
#     def __str__(self):
#         return self.name
#
#
# # class Subcategory(models.Model):
# #     category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
# #     subcategory_name = models.CharField(max_length=150, db_index=True)
# #     slug = models.SlugField(max_length=255, unique=True)
# #     # subcategories = SubcategoryManager()
# #
# #     class Meta:
# #         ordering = ('subcategory_name',)
# #         verbose_name_plural = 'Subcategories'
# #
# #     def get_absolute_url(self):
# #         return reverse('store:subcategory_list', args=[self.slug])
# #
# #     def __str__(self):
# #         return self.subcategory_name
#
#
# class Product(models.Model):
#     category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
#     # subcategory = models.ForeignKey(Subcategory, related_name='product', on_delete=models.CASCADE)
#     created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='product_creator')
#     product_name = models.CharField(max_length=255)
#     description = models.TextField(blank=True)
#     image = models.ImageField(upload_to='images/', default='images/default.png')
#     slug = models.SlugField(max_length=255)
#     price = models.DecimalField(max_digits=4, decimal_places=2)
#     in_stock = models.BooleanField(default=True)
#     is_active = models.BooleanField(default=True)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#     objects = models.Manager()
#     products = ProductManager()
#
#     class Meta:
#         verbose_name_plural = 'Products'
#         ordering = ('-created',)
#
#     def get_absolute_url(self):
#         return reverse('store:product_detail', args=[self.slug])
#
#     #   store este aplicatia din urls care ne permite sa accesam mai usor urls urile,
#     #   product_detail este name ul din urls.py si prin store il accesam
#
#     def __str__(self):
#         return self.product_name
#
