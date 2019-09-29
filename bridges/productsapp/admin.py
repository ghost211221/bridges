from django.contrib import admin
from productsapp.models import MaterialCategory, MeasureTypes, Material, TechnicalSolutions


class MaterialCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name', )

    class Meta:
        model = MaterialCategory


class MeasureTypesAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)

    class Meta:
        model = MeasureTypes


class MaterialAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'measure',)
    list_display_links = ('name',)
    search_fields = ('name',)

    class Meta:
        model = Material


class TechnicalSolutionsAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_display_links = ('name',)
    search_fields = ('name',)

    class Meta:
        model = TechnicalSolutions


admin.site.register(MaterialCategory, MaterialCategoryAdmin)
admin.site.register(MeasureTypes, MeasureTypesAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(TechnicalSolutions, TechnicalSolutionsAdmin)

