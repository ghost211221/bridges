from django.contrib import admin
from productsapp.models import MaterialCategory, \
    MeasureTypes, Material, MaterialImage, TechnicalSolutions


class MaterialCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name', )

    class Meta:
        model = MaterialCategory


admin.site.register(MaterialCategory, MaterialCategoryAdmin)


class MeasureTypesAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)

    class Meta:
        model = MeasureTypes


admin.site.register(MeasureTypes, MeasureTypesAdmin)


class MaterialAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'measure',)
    list_display_links = ('name',)
    search_fields = ('name',)

    class Meta:
        model = Material


admin.site.register(Material, MaterialAdmin)


class MaterialImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'alt_desc', 'image',)
    list_display_links = ('id', 'alt_desc', 'image',)
    search_fields = ('alt_desc',)

    class Meta:
        model = MaterialImage


admin.site.register(MaterialImage, MaterialImageAdmin)


class TechnicalSolutionsAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_display_links = ('name',)
    search_fields = ('name',)

    class Meta:
        model = TechnicalSolutions


admin.site.register(TechnicalSolutions, TechnicalSolutionsAdmin)

