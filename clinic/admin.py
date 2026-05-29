from django.contrib import admin
from .models import Owner, Pet, PetType, Specialty, Vet, Visit

admin.site.site_header = "Sasi's Pet Clinic"
admin.site.site_title = "Sasi's Pet Clinic"
admin.site.index_title = "Site Administration"
admin.site.site_url = ""


class PetInline(admin.TabularInline):
    model = Pet
    extra = 1


class VisitInline(admin.TabularInline):
    model = Visit
    extra = 1


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'city', 'telephone']
    search_fields = ['first_name', 'last_name', 'city']
    inlines = [PetInline]


@admin.register(PetType)
class PetTypeAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ['name', 'pet_type', 'owner', 'birth_date']
    search_fields = ['name', 'owner__first_name', 'owner__last_name']
    inlines = [VisitInline]


@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Vet)
class VetAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'get_specialties']
    filter_horizontal = ['specialties']

    def get_specialties(self, obj):
        return ', '.join([s.name for s in obj.specialties.all()])
    get_specialties.short_description = 'Specialties'


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ['visit_date', 'pet', 'vet', 'description']
    list_filter = ['visit_date', 'vet']
    search_fields = ['pet__name', 'vet__first_name', 'vet__last_name']
