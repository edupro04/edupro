from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import Group

from django import forms
User = get_user_model()

class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])


class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    list_filter = ['is_vendor','is_active','is_staff','is_superuser',]
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('city', 'phone','is_vendor','ride_count')}),
    )

admin.site.register(User, MyUserAdmin)
admin.site.unregister(Group)

#admin.site.site_header = 'Charvehi' or admin/base_site.html
