from django.contrib import admin
from . import models

admin.site.register(models.Product)
# admin.site.register(models.Category)
admin.site.register(models.Cart)
admin.site.register(models.Order)
admin.site.register(models.OrderProduct)
admin.site.register(models.PaymentLog)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['title']

    #this class helps us to add good features of classification in django
    #as an example I simulated it for category model

    def delete_queryset(self, request, queryset):
        for category in queryset:
            category.delete()

admin.site.register(models.Category, CategoryAdmin)
