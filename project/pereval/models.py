from django.db import models

class Users(models.Model):
    email = models.EmailField(unique=True, primary_key=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    fam = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    otc = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.email

class Coords(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.FloatField()

    def __str__(self):
        return f"{self.latitude}, {self.longitude}, {self.height}"

class PerevalAdded(models.Model):
    STATUS_CHOICCES = [
        ('new', 'New')
    ]
    date_added = models.DateTimeField()
    beauty_title = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255)
    other_titles = models.CharField(max_length=255, blank=True, null=True)
    connect = models.CharField(max_length=255, blank=True, null=True)
    add_time = models.DateTimeField()
    coord = models.ForeignKey(Coords, on_delete=models.CASCADE, related_name='pereval_coords')
    level_winter = models.CharField(max_length=10, blank=True, null=True)
    level_summer = models.CharField(max_length=10, blank=True, null=True)
    level_autumn = models.CharField(max_length=10, blank=True, null=True)
    level_spring = models.CharField(max_length=10, blank=True, null=True)


    def __str__(self):
        return self.title

class PerevalImage(models.Model):
    pereval = models.ForeignKey(PerevalAdded, on_delete=models.CASCADE, related_name='images')
    date_added = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class PerevalArea(models.Model):
    id_parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subareas')
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class SprActivitiesTypes(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


