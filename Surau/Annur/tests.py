





from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile
from .models import User
from .models import Item
from .models import Employee
from .models import Booking

#Unregister group
admin.site.unregister(Group)

#Mix profile info into User info
class ProfileInline(admin.StackedInline):
    model = Profile

#Extend user model
class UserAdmin(admin.ModelAdmin):
    model = User
    #Just display username fields on admin page
    fields = ["username"]
    inlines = [ProfileInline]

#Ungregister initial user
admin.site.unregister(User)
#Reregister user and Profile
admin.site.register(User, UserAdmin)
#admin.site.register(Profile)

# Register your models here.
admin.site.register(CusUsers)
admin.site.register(Item)
admin.site.register(Employee)
admin.site.register(Booking)


