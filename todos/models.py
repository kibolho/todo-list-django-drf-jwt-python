from django.db import models

class Todo(models.Model):
    title = models.TextField()
    description = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    is_completed = models.BooleanField(default=False)
    owner = models.ForeignKey(
      'users.CustomUser',
      related_name='todos',
      on_delete=models.CASCADE,
    )

    def __str__(self):
      return f"Title: {self.title} <Completed: {self.is_completed}>"