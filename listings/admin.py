# Imports
from django.contrib import admin
from .models import Listing

# ListingAdmin
class ListingAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
	list_display_links = ('id', 'title')
	list_filter = ('realtor',)
	list_editable = ('is_published',)
	search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
	list_per_page = 25

# Add to dashboard
admin.site.register(Listing, ListingAdmin)
