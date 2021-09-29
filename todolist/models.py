from django.db import models

# Create your models here.
class Todolist(modeLs.ModeL:
    text=models.CharField(max_Length=45)
    completed=models.BooleanField(default=False)
    def __str__(self):
        return self.text