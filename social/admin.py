from django.contrib import admin

# import from app
from social.models import Stories,Posts

# Register your models here.

admin.site.register(Stories)
admin.site.register(Posts)



# python manage.py create superuser


