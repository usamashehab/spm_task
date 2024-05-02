from django.db import models
from spm_task.core.models import BaseModel


class Client(BaseModel):
    name = models.CharField(max_length=255)
    company = models.ForeignKey(
        'company.Company', on_delete=models.CASCADE, related_name='clients')

    def __str__(self) -> str:
        return self.name
