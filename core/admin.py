from django.contrib import admin
from .models import Tool, AdminProfile

# 1. Dono models ko register karein
admin.site.register(Tool)
admin.site.register(AdminProfile)

# 2. Django Administration ko "Shadow Administration" mein badalne ke liye
admin.site.site_header = "Shadow Administration"
admin.site.site_title = "Shadow Admin Portal"
admin.site.index_title = "Welcome to Shadow Control Panel"