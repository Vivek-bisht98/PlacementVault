from django.db import models
from django.contrib.auth.models import User


class Schedule(models.Model):

    ROUND_CHOICES = [
        ('OA', 'OA'),
        ('GD', 'GD'),
        ('Technical', 'Technical'),
        ('HR', 'HR'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    company_name = models.CharField(max_length=100)

    role = models.CharField(max_length=100)

    round_type = models.CharField(
        max_length=20,
        choices=ROUND_CHOICES
    )

    date = models.DateField()

    time = models.TimeField()

    def __str__(self):
        return f"{self.company_name} - {self.role}"


class Experience(models.Model):

    ROUND_CHOICES = [
        ('OA', 'OA'),
        ('GD', 'GD'),
        ('Technical', 'Technical'),
        ('HR', 'HR'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    company_name = models.CharField(max_length=100)

    role = models.CharField(max_length=100)

    round_type = models.CharField(
        max_length=20,
        choices=ROUND_CHOICES
    )

    focus_subject = models.CharField(max_length=100)

    experience = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.company_name} - {self.role}"