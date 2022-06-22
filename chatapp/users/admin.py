from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm
from .models import User, Friend
# Register your models here.

class UserAdmin(UserAdmin):
      add_form=CustomUserCreationForm
      model = User
      list_display = ( 'first_name', 'username', "date_joined",  'is_staff', "is_verified", 'web', )
      fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': (  "bio", "pic", "is_verified",  'web', )}),
      )
      add_fieldsets = UserAdmin.add_fieldsets + (
        (None,{'fields':( "bio", "pic", "is_verified",  'web', )}),
      )



admin.site.register(User, UserAdmin)
admin.site.register(Friend)
                    
                
                                                   