from django.db import models

class MyEvent(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    date = models.DateField()
    start_time = models.TimeField(blank=True, null=True)  # เวลาเริ่ม
    end_time = models.TimeField(blank=True, null=True) 
         

    def __str__(self):
        return f"{self.date} - {self.title}"
    