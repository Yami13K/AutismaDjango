from django.contrib import admin

from .models import User,Child,Image,Game


admin.site.register(User)
admin.site.register(Child)
admin.site.register(Image)
admin.site.register(Game)

