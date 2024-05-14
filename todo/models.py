from django.db import models  # 最初はこれだけ

# Create your models here.
class Todo(models.Model):
    title = models.CharField("タスク名", max_length=30)
    description = models.TextField("詳細", blank=True)
    deadline = models.DateField("締切")
    STATUS_CHOICES = (
        ('ongoing', '継続中'),
        ('completed', '完了'),
    )

    title = models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ongoing')

    def __str__(self):
        return self.title
