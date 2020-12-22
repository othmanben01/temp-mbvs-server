from django.db import models

class Auditorium(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False, null=True)
    start_date_time = models.DateTimeField(blank=False, null=True)
    end_date_time = models.DateTimeField(blank=False, null=True)


    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        self.name = self.name.strip().lower()
        return super(Auditorium, self).save(*args, **kwargs)


class Video(models.Model):
    file_source = models.FileField(upload_to='uploads/', blank=False)
    auditorium = models.ForeignKey(Auditorium, on_delete=models.CASCADE, blank=False, related_name='videos')
    
    def __str__(self):
        return f'{self.file_source}'