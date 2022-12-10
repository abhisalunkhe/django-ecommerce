from django.contrib import admin
from .models import *


class admin_feature_items(admin.ModelAdmin):
    list_display = ['name', 'price', 'visible']


# Register your models here.
admin.site.register(feature_items, admin_feature_items)
admin.site.register(cate_tshirt, admin_feature_items)
admin.site.register(cate_blazer, admin_feature_items)
admin.site.register(cate_sunglass, admin_feature_items)
admin.site.register(cate_kids, admin_feature_items)
admin.site.register(cate_poloshirt, admin_feature_items)
admin.site.register(categ_nike, admin_feature_items)
admin.site.register(categ_underarmour, admin_feature_items)
admin.site.register(categ_adidas, admin_feature_items)
admin.site.register(categ_puma, admin_feature_items)
admin.site.register(categ_asics, admin_feature_items)
admin.site.register(categ_men_fendi, admin_feature_items)
admin.site.register(categ_men_guess, admin_feature_items)
admin.site.register(categ_men_valentino, admin_feature_items)
admin.site.register(categ_men_dior, admin_feature_items)
admin.site.register(categ_men_versace, admin_feature_items)
admin.site.register(categ_men_armani, admin_feature_items)
admin.site.register(categ_men_prada, admin_feature_items)
admin.site.register(categ_men_dolceandgabbana, admin_feature_items)
admin.site.register(categ_men_chanel, admin_feature_items)
admin.site.register(categ_men_gucci, admin_feature_items)
admin.site.register(categ_women_fendi, admin_feature_items)
admin.site.register(categ_women_guess, admin_feature_items)
admin.site.register(categ_women_valentino, admin_feature_items)
admin.site.register(categ_women_dior, admin_feature_items)
admin.site.register(categ_women_versace, admin_feature_items)
admin.site.register(categ_kids, admin_feature_items)
admin.site.register(categ_fashion, admin_feature_items)
admin.site.register(categ_households, admin_feature_items)
admin.site.register(categ_interiors, admin_feature_items)
admin.site.register(categ_clothing, admin_feature_items)
admin.site.register(categ_bags, admin_feature_items)
admin.site.register(categ_shoes, admin_feature_items)
