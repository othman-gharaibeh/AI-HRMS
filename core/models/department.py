from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "core_department"
        ordering = ["name"]

    def __str__(self):
        return self.name
