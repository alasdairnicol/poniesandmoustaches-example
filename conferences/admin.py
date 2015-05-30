from django.contrib import admin
from .models import Conference

class ConferenceAdmin(admin.ModelAdmin):
    list_display = ['location', 'country', 'year']

admin.site.register(Conference, ConferenceAdmin)
