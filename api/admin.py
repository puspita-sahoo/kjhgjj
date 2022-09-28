from django.contrib import admin
from .models import UserProfile, Product
# Register your models here.



@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'user_type', 'full_name', 'phone', 'alternate_phone', 'terms_condition_privacy', 'address', 'street_name', 'zipcode', 'isactive')


@admin.register(Product)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'categories', 'image', 'reviews', 'categories', 'stock')





