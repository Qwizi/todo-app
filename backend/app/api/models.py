from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=50)
    completed = models.BooleanField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'
