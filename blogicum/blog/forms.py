from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class UserEditForm(forms.ModelForm):
    """Форма редактирования данных профиля."""

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')