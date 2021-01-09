from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.core.models import BaseModel

User = get_user_model()


class Todo(BaseModel):
    class StateTypes(models.IntegerChoices):
        TODO = 0, _("Todo")
        IN_PROGRESS = 1, _("In Progress")
        DONE = 2, _("DONE")

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    state = models.IntegerField(choices=StateTypes.choices)
    title = models.CharField(max_length=255)
    body = models.TextField()

    class Meta:
        ordering = ["-created_datetime"]
