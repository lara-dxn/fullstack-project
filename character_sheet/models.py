from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    isPlayer = models.BooleanField(default=False)
    isGM = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username

class Character(models.Model):
    slug = models.SlugField(max_length=100, unique=True, blank=True, default='')
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    hp = models.IntegerField()
    character_class = models.CharField(max_length=100, default='')
    character_race = models.CharField(max_length=100, default='')

    blinded = models.BooleanField(default=False)
    charmed = models.BooleanField(default=False)
    deafened = models.BooleanField(default=False)
    frightened = models.BooleanField(default=False)
    grappled = models.BooleanField(default=False)
    incapacitated = models.BooleanField(default=False)
    invisible = models.BooleanField(default=False)
    paralyzed = models.BooleanField(default=False)
    petrified = models.BooleanField(default=False)
    poisoned = models.BooleanField(default=False)
    prone = models.BooleanField(default=False)
    restrained = models.BooleanField(default=False)
    stunned = models.BooleanField(default=False)
    unconscious = models.BooleanField(default=False)
    exhaustion = models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=0)

    class Meta:
        ordering = ['name']  # Order characters alphabetically by name
    
    def save(self, *args, **kwargs):
        # Check if slug is already set; if not, create one
        if not self.slug:
            # Generate initial slug from the character's name
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            
            # Loop to find a unique slug
            while Character.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            
            self.slug = slug
            
        super(Character, self).save(*args, **kwargs)


    def __str__(self):
        return f"{self.name} - {self.character_class}"