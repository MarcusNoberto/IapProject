from django.db import models


from django.db import models

class Jogo(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class IAP(models.Model):
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE, related_name='iaps')
    nome = models.CharField(max_length=255)
    iapPrices = {}
    valor_us = models.CharField(max_length=15)
    price = models.TextField()

    def trata_precos(self):  
        precos = self.price.split(';')
        for i in range(0, len(precos), 2):
            key = precos[i].strip()
            value = (float(precos[i + 1].strip())) / 1000000
            self.iapPrices[key] = value  

    def save(self, *args, **kwargs):
        self.trata_precos()
        super(IAP, self).save(*args, **kwargs)

    def __str__(self):
        return f'Name: {self.nome}'



