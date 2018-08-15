from django.db import models


# builing of the class model
class Blog(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=300)
    pub_date = models.DateTimeField(auto_now=False, auto_now_add=False, )
    body = models.TextField()

    # function to return the selected object and his title
    def __str__(self):
        return self.title

    # returns the content of body up to 100 characters
    def summary(self):
        return self.body[:100]

    # function to display the date without the publication hour on template
    def pub_date_noHour(self):
        return self.pub_date.strftime('%b %e %Y')


from django.db import models

# Create your models here.
