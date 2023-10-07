from django.contrib import admin

from .models import *

admin.site.site_header = "Portfolio Admin"
admin.site.register(Project)
admin.site.register(Technology)
admin.site.register(About)
admin.site.register(Contact)
admin.site.register(Learning)
