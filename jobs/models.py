from django.db import models

#Defining the job model
class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    body = models.TextField(max_length=300)
    position = models.CharField(max_length=100)
    repository = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.position

    # returns the content of body up to 100 characters
    def summary(self):
        return self.body[:100]

    def DisplayCodeSource_tags(self):
        urlify = enumerate(self, int=1)
        return [urlify(tag) for tag in self.tags.repository(', ')]