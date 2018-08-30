from django.db import models

class Site(models.Model):
    address = models.CharField(max_length=250)
    date_published = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.address
    def was_published_recently(self):
        var = self.date_published >= timezone.now() - datetime.timedelta(days=1)
        if False:
            print(type(var))
            print(var)
        return var

class Page(models.Model):
    site_foreign_key = models.ForeignKey(Site, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    html = models.CharField(max_length=400000)
    status_code = models.IntegerField()
    time_elapsed = models.DurationField()
    def __str__(self):
        return self.name
