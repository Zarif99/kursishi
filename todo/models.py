from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

type_choice = {
    ('red', 'bug'),
    ('blue', 'task'),
    ('green', 'story'),
}

priority_type = {
    ('red', 'hard'),
    ('orange', 'medium'),
    ('green', 'easy'),
}

status_choice = {
    ('DONE', 'DONE'),
    ('TO DO', 'TO DO'),
    ('IN PROGRESS', 'IN PROGRESS'),
}
User = get_user_model()


class Todo(models.Model):
    type = models.CharField(_('Type of the task'), max_length=50, choices=type_choice)
    key = models.CharField(_('Name of the task'), max_length=255, unique=True)
    summary = models.TextField(_('Body of the task'))
    assignee = models.ForeignKey(User, on_delete=models.CASCADE, related_name=_('assignee'),
                                 help_text=_('Assigner of the task'))
    reporter = models.ForeignKey(User, on_delete=models.CASCADE, related_name=_('reporter'),
                                 help_text=_('Reporter of the task'), default=_('admin'))
    priority = models.CharField(_('Priority of the task'), max_length=100, choices=priority_type)
    status = models.CharField(_('Status'), max_length=100, choices=status_choice)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(
        _('URL'),
        max_length=255,
        unique=True,
        help_text=_('Human-readable URLs'),
        error_messages={
            'unique': _('A task with that slug already exists.'),
        }
    )

    def __str__(self):
        return self.key

    def save(self, *args, **kwargs):
        """
        Generating a slug for the object before saving
        """
        if not self.id:
            # We use name as a slug
            self.slug = slugify(self.key.lower())
        # Calling the parent method
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """
        Telling Django how to compute the canonical URL to get detail about the Todo object.
        For callers, this method should return a string that can be used to refer to the object over HTTP.
        """

        return reverse('todo_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        """
        Telling Django how to compute the canonical URL to get update about the Todo object.
        For callers, this method should return a string that can be used to refer to the object over HTTP.
        """
        return reverse('todo_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        """
        Telling Django how to compute the canonical URL to get delete about the Todo object.
        For callers, this method should return a string that can be used to refer to the object over HTTP.
        """
        return reverse('todo_delete_url', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Todo'
        verbose_name_plural = 'Todo'
        ordering = ['-created']
