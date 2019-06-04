from django.db import models


class Lote(models.Model):
    id_lote  = models.AutoField(
        primary_key=True
        )
    
    lote_numero = models.CharField(
        max_length=10,
        unique=True
        )


class Modelo_placa(models.Model):
    id_modelo = models.AutoField(
        primary_key=True, 
       
        )

    descricao = models.CharField(
        max_length=50
        )
    
    tipo = models.CharField(
        'Tipo',
        max_length=30
        )
     
class Item(models.Model):
    id_item = models.AutoField(
        'ID_Item', 
        primary_key = True
        )

class Placa(models.Model):
    id_placa = models.AutoField(
        'ID_Placa',
        primary_key = True
        )

    id_modelo = models.ForeignKey(
        Modelo_placa,  on_delete=models.CASCADE, 
        )

    id_lote = models.ForeignKey(
        Lote,  on_delete=models.CASCADE
        )

    numero_serie = models.IntegerField(
        'Número de Série',
        unique=True,

        ) 

    processo = models.CharField(
        max_length=20
        )

    revisao_lm = models.IntegerField('Revisão LM'
        )

    class Meta:
        db_table = 'PLACAS'


    
       
    

