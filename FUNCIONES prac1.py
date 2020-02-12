#!/usr/bin/env python
# coding: utf-8

# # FUNCIONES 

# • T-Shirt: Elabora un función llamada make_shirt() que acepte el tamaño y el texto que se imprimira en la playera. La función debera de imprimir el tamaño y el texto que se han enviado a la función.
# 

# In[2]:


def make_shirt(talla,texto):
    print('La talla de la playera es '+talla)
    print('El exto que aparece en la playera es '+texto)
make_shirt(talla='chica',texto='GLORIA')   


# • Playeras Grandes: Modifique la función make_shirt() de tal manera que el tamaño por default sea grande y el texto predefinido sea I <3 Python. Genere una playera grande y mediana con el mensaje predeterminado, y genere una playera pequeña con un mensaje diferente.

# In[3]:


def make_shirt(tam,tamano,texto,talla='grande',tex='I <3 python'):
    print('La talla de la playera es '+talla)
    print('El texto que aparece en la playera es '+tex)
    print('Esta playera de talla '+tamano+',su texto que aparece es:'+tex)
    print('La talla de la playera es '+tam+' su texto es diferente: '+texto)
    
make_shirt(tam='pequeña',tamano='mediana',texto='GLORIA!!!')


# • Ciudades: Escriba una fución llamada describe_city() que acepte como argumentos la ciudad y el país. La función debe imprimir un enunciado sencillo como: París está en Francia. Define el parámetro para el país con un valor predeterminado. Llame la función tres veces y que por lo menos una no sea el país predeterminado.

# In[5]:


def describe_city(ciudad='Paris',pais='Francia'):
    print('la ciudad de '+ ciudad+' esta en '+pais )
    print(pais +' es un lugra muy romantico')
    print('En '+ciudad+' se encuentra la torre ifel')
describe_city()
    

