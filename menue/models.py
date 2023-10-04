from django.db import models


class Menue(models.Model):
    title = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    url = models.CharField(max_length=255)

    def __str__(self):
        return self.title +'-'+ self.url
