from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register([DateTraning,
                     Pull,
                     Push,
                     Sit,
                     Jumping,
                     Entrance,
                     Press,
                     Weight,
                     Weightcategory,
                     Bars,
                     Stadium,
                     ])
