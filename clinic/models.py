from django.db import models


class Owner(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ['last_name', 'first_name']


class PetType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Pet(models.Model):
    name = models.CharField(max_length=50)
    birth_date = models.DateField()
    pet_type = models.ForeignKey(PetType, on_delete=models.PROTECT, related_name='pets')
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='pets')

    def __str__(self):
        return f"{self.name} ({self.owner})"

    class Meta:
        ordering = ['name']


class Specialty(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'specialties'
        ordering = ['name']


class Vet(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    specialties = models.ManyToManyField(Specialty, blank=True, related_name='vets')

    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name}"

    class Meta:
        ordering = ['last_name', 'first_name']


class Visit(models.Model):
    visit_date = models.DateField()
    description = models.TextField()
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='visits')
    vet = models.ForeignKey(Vet, on_delete=models.SET_NULL, null=True, related_name='visits')

    def __str__(self):
        return f"Visit for {self.pet} on {self.visit_date}"

    class Meta:
        ordering = ['-visit_date']
