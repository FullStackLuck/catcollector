from django.contrib import admin
from .models import Cat
from .models import Feeding

# Register your models here.

admin.site.register(Cat)
admin.site.register(Feeding)