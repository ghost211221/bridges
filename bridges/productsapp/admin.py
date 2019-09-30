from django.contrib import admin
<<<<<<< HEAD
from productsapp.models import MaterialCategory, MeasureTypes, Material, TechnicalSolutions
=======
from .models import *
>>>>>>> upstream/sprint_1


class MaterialCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name', )

    class Meta:
        model = MaterialCategory


<<<<<<< HEAD
=======
admin.site.register(MaterialCategory, MaterialCategoryAdmin)


>>>>>>> upstream/sprint_1
class MeasureTypesAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)

    class Meta:
        model = MeasureTypes


<<<<<<< HEAD
=======
admin.site.register(MeasureTypes, MeasureTypesAdmin)


class MaterialImageInline(admin.TabularInline):
    model = MaterialImage
    extra = 0


>>>>>>> upstream/sprint_1
class MaterialAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'category', 'measure',)
    list_display_links = ('name',)
    search_fields = ('name',)
<<<<<<< HEAD
=======
    inlines = [MaterialImageInline]
>>>>>>> upstream/sprint_1

    class Meta:
        model = Material


<<<<<<< HEAD
=======
admin.site.register(Material, MaterialAdmin)


class MaterialImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'is_active', 'created', 'updated',)
    list_display_links = ('id', 'image',)

    class Meta:
        model = MaterialImage


admin.site.register(MaterialImage, MaterialImageAdmin)


class TechnicalSolutionsImageInline(admin.TabularInline):
    model = TechnicalSolutionsImage
    extra = 0


>>>>>>> upstream/sprint_1
class TechnicalSolutionsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', )
    list_display_links = ('name',)
    search_fields = ('name',)
<<<<<<< HEAD
=======
    inlines = [TechnicalSolutionsImageInline]
>>>>>>> upstream/sprint_1

    class Meta:
        model = TechnicalSolutions


<<<<<<< HEAD
admin.site.register(MaterialCategory, MaterialCategoryAdmin)
admin.site.register(MeasureTypes, MeasureTypesAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(TechnicalSolutions, TechnicalSolutionsAdmin)

=======
admin.site.register(TechnicalSolutions, TechnicalSolutionsAdmin)


class TechnicalSolutionsImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'is_active', 'created', 'updated',)
    list_display_links = ('id', 'image',)

    class Meta:
        model = TechnicalSolutionsImage


admin.site.register(TechnicalSolutionsImage, TechnicalSolutionsImageAdmin)
>>>>>>> upstream/sprint_1
