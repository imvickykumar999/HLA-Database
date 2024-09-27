from django.db import models

class Donor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    
    # HLA Types (A, B, C, DRB1, etc.)
    hla_a = models.CharField(max_length=10)
    hla_b = models.CharField(max_length=10)
    hla_c = models.CharField(max_length=10)
    hla_drb1 = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
