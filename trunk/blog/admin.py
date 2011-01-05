from django.contrib import admin
from models import Category, Comments, Links,Post, Tags
class TagsAdmin(admin.ModelAdmin):
    list_display = ('name','slug','reference_count')
    search_fields = ['name']
    
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','get_cat_str','pubdate','hits')
    search_fields = ['title']
    list_filter =('post_type','category')
    fieldsets = (
    (None, {
        'fields': ('title', 'post_name','category',
                   'content','post_status','menu_order','comment_status',)
    }),
    ('Advanced options', {
        'classes': ('collapse',),
        'fields': ('post_parent', 'tags')
    }),
    )
    class Media:
        js = (
                '/media/js/tiny_mce/tiny_mce.js',
                '/media/js/admin_textarea.js',
            )

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','desc')
    search_fields = ['name']

class CommentsAdmin(admin.ModelAdmin):
    list_filter =('comment_approved',)
    list_display = ('comment_author','comment_author_email',
                    'comment_date','comment_approved')
    search_fields = ['comment_author']
    
class LinksAdmin(admin.ModelAdmin):
    list_display = ('link_title','link_url')
    fieldsets = (
        (None, {
            'fields': ('link_title','link_url','link_order')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('link_desc', 'link_image')
        }),
    )
admin.site.register(Tags,TagsAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Comments,CommentsAdmin)
admin.site.register(Links,LinksAdmin)
admin.site.register(Post,PostAdmin)   
