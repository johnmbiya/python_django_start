from django.contrib import admin
from listings.models import Band, Listing

class BandAdmin(admin.ModelAdmin):
  list_display = ('name', 'genre', 'year_formed', 'official_homepage')

class ListingAdmin(admin.ModelAdmin):
  list_display = ('title', 'type', 'band', 'year', 'sold')

admin.site.register(Band, BandAdmin)
admin.site.register(Listing, ListingAdmin)
