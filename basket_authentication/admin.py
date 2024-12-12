from django.contrib import admin
from .models import BasketInfoModel
from .forms import BasketCustomForm, BasketCustomChangeForm
from django.contrib.auth.admin import UserAdmin


class BasketCustomAdmin(UserAdmin):
    form = BasketCustomChangeForm
    add_form = BasketCustomForm
    model = BasketInfoModel
    list_display = ('basket_id', 'basket_version', 'basket_health', 'customer_company_name', 'customer_company_email')

    # Removing 'first_name', 'last_name' from custom fieldsets since they are already in UserAdmin.fieldsets
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('basket_id', 'basket_name', 'basket_health', 'basket_version', 'customer_company_name', 'customer_company_id', 'customer_company_email', 'customer_company_number','date','goods_name','goods_id','goods_features')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': (
        'basket_id', 'basket_name', 'basket_health', 'basket_version', 'customer_company_name', 'customer_company_id',
        'customer_company_email', 'customer_company_number', 'date', 'goods_name', 'goods_id', 'goods_features')}),

    )
    list_filter = ('basket_id', 'customer_company_id',)
    search_fields = ('basket_id', 'customer_company_id')


admin.site.register(BasketInfoModel, BasketCustomAdmin)
