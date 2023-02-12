import uuid
from django.conf import settings
from django.db import models


class Vacancy(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=120)
    description = models.TextField()
    salary = models.CharField(max_length=150)
    published = models.DateTimeField(auto_now_add=True)
    required_experience = models.CharField(max_length=40)
    publisher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    keywords = models.TextField()

    def __str__(self):
        return self.title


class VacancyResponse(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    message = models.TextField()
    resume = models.ForeignKey("resume.Resume", on_delete=models.CASCADE)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name="responses")

    def save(self, *args, **kwargs):
        in_db = VacancyResponse.objects.filter(
            resume_id=self.resume_id,
            vacancy_id=self.vacancy_id
        )
        if in_db:
            return in_db
        return super().save(*args, **kwargs)

