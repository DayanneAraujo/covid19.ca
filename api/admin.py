from django.contrib import admin
from .models import Covid19Ca

class Covid19CaAdmin(admin.ModelAdmin):
    list_display = ('date', 'prname', 'numconf', 'numtoday')
    list_filter = ('date', 'prname')

admin.site.register(Covid19Ca, Covid19CaAdmin)