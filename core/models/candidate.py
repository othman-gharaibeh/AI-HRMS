from django.db import models


class Candidate(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "core_candidate"
        ordering = ["full_name", "id"]

    def __str__(self):
        return f"{self.full_name} <{self.email}>"
