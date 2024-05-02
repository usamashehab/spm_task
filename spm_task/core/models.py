from django.db import models


class Approval(models.Model):
    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending"
        APPROVED = "APPROVED", "Approved"
        REJECTED = "REJECTED", "Rejected"

    status = models.CharField(
        max_length=10, choices=Status.choices, default=Status.PENDING)
    approver = models.ForeignKey("users.User", on_delete=models.CASCADE)


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=255, null=True, blank=True)
    approval = models.ForeignKey(Approval, on_delete=models.CASCADE)

    class Meta:
        abstract = True
