from django import forms
from django.core.exceptions import ValidationError

from todo.models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        exclude = ('slug',)

    def clean_slug(self):
        new_slug = self.cleaned_data.get('slug').lower()
        if new_slug == 'create':
            raise ValidationError('URL must not be "Create"')
        return new_slug
