from django.contrib import admin
from .models import Category, Event, Candidate , Statistic , Nominee

# Register your models here.

admin.site.register( Category)
admin.site.register( Event)
admin.site.register ( Candidate)
admin.site.register (Statistic)
admin.site.register(Nominee)
