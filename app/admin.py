from django.contrib import admin

# Register your models here.
from .models import Author


# admin.site.empty_value_display = '(None)'
# admin.site.register(Author)

@admin.display(empty_value='unknown')
# def birth_date_v(self, obj):
#     return obj.birth_date_v
class AuthorAdmin(admin.ModelAdmin):
    list_display = (birth_date_v,)
    # empty_value_display='unknown'

    

# admin.site.register()
admin.site.register(Author, AuthorAdmin)
