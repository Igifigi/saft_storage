from django.contrib import admin
from .models import Tool, ToolTag, Rental, Lender, LenderTeam

# Register your models here.

admin.site.register(Tool)
admin.site.register(ToolTag)
admin.site.register(Rental)
admin.site.register(Lender)
admin.site.register(LenderTeam)
