from django.contrib import admin
from myapp import models

# Register your models here.
admin.site.register(models.Client)
admin.site.register(models.RegisterLocation)

admin.site.register(models.Immobile)
admin.site.register(models.ImmobileImage)
