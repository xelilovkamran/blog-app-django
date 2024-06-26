from django.contrib import admin
from .models import User, Category, Blog, Comment, ContactPage, AboutPage

# Register your models here.
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(Comment)


@admin.register(ContactPage)
class ContactPageAdmin(admin.ModelAdmin):
    list_display = ('email', 'location', 'phone_number')


@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
    list_display = ('company_name',)
