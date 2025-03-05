from django.db import models
from datetime import date

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField()
    status = models.CharField(max_length=20, default='Pending')

    def save(self, *args, **kwargs):
        if self.status != 'Completed':  
            self.status = 'Overdue' if self.due_date < date.today() else 'Pending'
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} - {self.status}"