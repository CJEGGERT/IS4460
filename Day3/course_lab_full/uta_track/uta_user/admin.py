from django.contrib import admin

# Register your models here.

from .models import UtaUser,Route, FaqMain, Faq, Comment


class UtaUserAdmin(admin.ModelAdmin):
    pass
admin.site.register(UtaUser)

class RouteAdmin(admin.ModelAdmin):
    pass
admin.site.register(Route)

class FaqMainAdmin(admin.ModelAdmin):
    pass
admin.site.register(FaqMain)

class FaqAdmin(admin.ModelAdmin):
    pass
admin.site.register(Faq)

class CommentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Comment)