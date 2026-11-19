from django.db import models

from .department import Department


class JobPosition(models.Model):
    department = models.ForeignKey(
        Department,
        on_delete=models.PROTECT,
        related_name="job_positions",
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    required_skills = models.JSONField(default=list, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "core_job_position"
        ordering = ["title", "id"]
        constraints = [
            models.UniqueConstraint(
                fields=["department", "title"],
                name="unique_job_position_title_per_department",
            )
        ]

    def __str__(self):
        return f"{self.title} ({self.department.name})"
