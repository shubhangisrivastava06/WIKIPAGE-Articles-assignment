from django.contrib import admin

from .models import User
from .models import Articles,Guest


admin.site.register(User)
admin.site.register(Articles)
admin.site.register(Guest)

