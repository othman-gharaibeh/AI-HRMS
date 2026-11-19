from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from .candidate import Candidate
from .job_position import JobPosition


class ScreeningResult(models.Model):
    class Recommendation(models.TextChoices):
        PROCEED = "proceed", "Proceed"
        HOLD = "hold", "Hold"
        REJECT = "reject", "Reject"

    candidate = models.ForeignKey(
        Candidate,
        on_delete=models.CASCADE,
        related_name="screening_results",
    )
    job_position = models.ForeignKey(
        JobPosition,
        on_delete=models.PROTECT,
        related_name="screening_results",
    )
    score = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    strengths = models.JSONField(default=list, blank=True)
    missing_skills = models.JSONField(default=list, blank=True)
    recommendation = models.CharField(max_length=10, choices=Recommendation.choices)
    summary = models.TextField(blank=True)
    raw_report = models.JSONField(default=dict, blank=True)
    generated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "core_screening_result"
        ordering = ["-generated_at", "-id"]
        constraints = [
            models.CheckConstraint(
                condition=models.Q(score__gte=0) & models.Q(score__lte=100),
                name="screening_result_score_between_0_and_100",
            )
        ]

    def __str__(self):
        return f"{self.candidate.full_name} - {self.job_position.title}: {self.score}"
