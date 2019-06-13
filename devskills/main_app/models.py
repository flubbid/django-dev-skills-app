from django.db import models
from django.contrib.auth.models import User

SKILL_LEVELS = (
    (1, 'Fundamental Awareness'),
    (2, 'Novice'),
    (3, 'Intermediate'),
    (4, 'Advanced'),
    (5, 'Expert'),
)

# Create your models here.
class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=300)
    skill_level = models.IntegerField(
        choices=SKILL_LEVELS,
        default=1
        )