from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=255, verbose_name="Тақырып")
    description = models.TextField(verbose_name="Сипаттама")
    due_date = models.DateField(verbose_name="Аяқталу күні")
    status = models.BooleanField(default=False, verbose_name="Аяқталды ма?")

    def __str__(self):
        return self.title
