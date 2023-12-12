from django.db import models

# Create your models here.

GENDER_CHOICES = [ 
    ['male', 'Male'],
    ['female', 'Female'],
]

class Customer(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    image = models.ImageField('customer/images/')
    liked_songs = models.ManyToManyField('song.Song', related_name='liked_songs', null=True, blank=True)
    liked_playlists = models.ManyToManyField('song.Playlist', related_name='liked_playlists', null=True, blank=True)
    followed_artists = models.ManyToManyField('Artist', related_name='followed_artists', null=True, blank=True)
    birth_date = models.DateField()
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    updated = models.DateField(auto_now=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class Artist(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    image = models.ImageField('artist/images/')
    cover = models.ImageField('artist/covers/', null=True, blank=True)
    verified = models.BooleanField(default=False)
    updated = models.DateField(auto_now=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username