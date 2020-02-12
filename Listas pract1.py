#!/usr/bin/env python
# coding: utf-8

# # PRACTICA 1 

# ## LISTAS 

# Ejercicio: Cual fue el resultado de la ejecución tal cual aparece en la terminal

# In[2]:


bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)


# En la lista bicycles como se mando a imprimir la lista en su totalidad, en la terminal aparecio el contenido de la lista.

# Ejercico: Escriba cual fue el resultado de la ejecución tal cual aparece en la terminal
#  

# In[3]:


bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[1])


# En la lista bicycles se mando a imprimir la posicion 1 de la lista, por lo tanto el resultado de la terminal fue cannondale 

# ### TAREA 
• Nombres: Realiza una lista con algunos nombres de tus amigos en una lista llamada names. Imprime en la pantalla el nombre de cada persona ingresando elemento por elemento.
# In[5]:


names=['Benjamin','Irving','Yaneli']
print(names[0])
print(names[1])
print(names[2])



# • Mensaje:En la lista creada anteriormente, ademas de imprimir el nombre de cada persona imprime un mensaje personalizado para cada persona.
#  

# In[13]:


names=['Benjamin','Irving','Yaneli']
print(names[0],'Eres el mejor portero de tu equipo')
print(names[1],'Eres mi enfermero personal')
print(names[2],'Eres la mejor arquitecta')


# • Tu propia lista: Piensa en una lista deseos, la lista debe de tener por lo menos 15 elementos. Imprime algunos de los deseos. Ejemplo Me gustarıa tener una moto Honda”

# In[21]:


deseos=['Me gustaria terminar mi carrera', 'Quiero viajar por el mundo','Tner una camara fotografica','Ir al espacio',
        'Me gustaria tener una moto Harley','me gustaria hablar 5 ideomas','Me gustaria ir al tomorrowland',
        'Quisiera tener un alberque para mascotas','Megustaria comer y no engordar','Quisiera aportar algo a la ciencia',
        'Quisiera ver las maravillas del mundo', 'Me gustaria explorar las piramides egipcias', 'Me gustaria ir a una isla virgen', 
        'Tener mi independencia','Quisiera comprender la energia astral']
for deceo in deseos:
    print (deceo)

