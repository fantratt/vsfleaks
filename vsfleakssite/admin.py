from django.contrib import admin
from vsfleakssite.models import *
     
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    list_filter = ['published', 'created', 'tags']
    search_fields = ['title', 'description', 'content', 'tags']
    date_hierarchy = 'created'
    save_on_top = True
    # prepopulate the slug from the title - big timesaver!
    prepopulated_fields = {"slug": ("title",)}
     
    


# Register your models here.
admin.site.register(Report)
admin.site.register(Post, PostAdmin)
