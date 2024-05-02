from spm_task.core.models import BaseModel
from django.db import models


class Company(BaseModel):
    class Type(models.TextChoices):
        SMALL_BUSINESS = "SMALL BUSINESS", "Small Business"
        STARTUP = "STARTUP", "Startup"
        CORPORATE = "CORPORATE", "Corporate"

    type = models.CharField(
        max_length=20, choices=Type.choices, default=Type.SMALL_BUSINESS)
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class SmallBusiness(models.Model):
    company = models.OneToOneField(
        Company, on_delete=models.CASCADE, related_name='small_business')
    num_employess = models.SmallIntegerField(null=True)
    industry = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.company.name} small business profile"


class Startup(models.Model):
    company = models.OneToOneField(
        Company, on_delete=models.CASCADE, related_name='startup')
    funding_rounds = models.SmallIntegerField(null=True)
    founders = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.company.name} startup profile"


class Corporate(models.Model):
    company = models.OneToOneField(
        Company, on_delete=models.CASCADE, related_name="corporate")
    location = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.company.name} corporate profile"
