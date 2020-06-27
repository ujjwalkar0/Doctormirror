from django.contrib import admin
from .models import users,problems,nurses,doctors,patient,ambulances,hospital

admin.site.register(users)
admin.site.register(problems)
admin.site.register(doctors)
admin.site.register(nurses)
admin.site.register(patient)
admin.site.register(ambulances)
admin.site.register(hospital)

# Register your models here.


