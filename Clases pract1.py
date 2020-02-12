#!/usr/bin/env python
# coding: utf-8

# # CLASES

# 
# • Restaurant: Declare una clase llamada Restaurant. El constructor debe de tener dos atributos, restaurant_name y cuisine_type. Desarrolle dos metodos describe_restaurant() que imprima en pantalla la información y el segundo open_restaurant() que imprima si el restaurante es abierto. Genere un objeto tipo restauratne y verifique su funcionamiento

# In[1]:


class restaurant():
    def __init__(self,restaurant_name,cuisine_type,open_close):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.open_close=open_close
    def describe_restaurant(self):
        print(self.restaurant_name+" es un lugar muy agradable")
        print('Son muy deliciosos los'+self.cuisine_type)
    def open_restaurant(self):
        print(self.open_close)
my_rest=restaurant('Antojitos',' postres','abierto')
print('Mi restaurante se llama '+my_rest.restaurant_name)
print("Su tipo de cocina son los"+my_rest.cuisine_type)
print("El restaurante esta " +my_rest.open_close+" apartir de las 10:00 am")

my_rest.describe_restaurant()


# •Tres restaurantes: Retome la clase del ejercicio anterior, genere tres restaurantes con nombres diferentes e imprima los atributos de los tres restaurantes.
# 

# In[2]:


class restaurant():
    def __init__(self,restaurant_name,cuisine_type,open_close):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.open_close=open_close
    def describe_restaurant(self):
        print(self.restaurant_name+" es un lugar muy agradable")
        print('Son muy deliciosos los'+self.cuisine_type)
    def open_restaurant(self):
        print(self.open_close)
my_rest=restaurant('ANTOJITOS',' postres','abierto')
print('Mi restaurante se llama '+my_rest.restaurant_name)
print("Su tipo de cocina son los"+my_rest.cuisine_type)
print("El restaurante esta " +my_rest.open_close+" apartir de las 10:00 am")

my_rest.describe_restaurant()
my_rest=restaurant('EXQUISITO',' postres','abierto')
print('Mi restaurante se llama '+my_rest.restaurant_name)
print("Su tipo de cocina son los"+my_rest.cuisine_type)
print("El restaurante esta " +my_rest.open_close+" apartir de las 10:00 am")

my_rest.describe_restaurant()

my_rest=restaurant("CIELITO",' postres','abierto')
print('Mi restaurante se llama '+my_rest.restaurant_name)
print("Su tipo de cocina son los"+my_rest.cuisine_type)
print("El restaurante esta " +my_rest.open_close+" apartir de las 10:00 am")

my_rest.describe_restaurant()

my_rest=restaurant('DULCE',' postres','abierto')
print('Mi restaurante se llama '+my_rest.restaurant_name)
print("Su tipo de cocina son los"+my_rest.cuisine_type)
print("El restaurante esta " +my_rest.open_close+" apartir de las 10:00 am")

my_rest.describe_restaurant()


# • Usuarios: Genere una clase llamada User con dos atributos first_name y last_name, agregue mas atributos que se utilizan para cuentas de usuario. Desarrolle un metodo describe_user() que imprima de manera ordenada y detallada la infomacion del
# usuario. Genere un segundo atributo greet_user() que imprima un saludo personalido para el usuario. Cree 10 usuarios y ejecute los dos metodos para cada usuario.
# 

# In[4]:


class usser():
    def __init__(self,first_name,last_name,mail,tipo):
        self.first_name=first_name
        self.last_name=last_name
        self.mail=mail
        self.tipo=tipo
    def describe_user(self):
        print('Usted '+self.first_name+ ' es estudiante de ingenieria')
        print('Utiliza mas la cuenta de '+self.mail)
        print('Su tipo de usuario es '+self.tipo+' ya que no es un usuario invitado')
    def greet_user(self):
        print ('Bienvenido al programa ')
my_uss=usser('Jazmin','Valdovinos','gmail','unico')
print(my_uss.first_name)
print(my_uss.last_name)
my_uss.greet_user()
my_uss.describe_user()

my_uss=usser('Yack','Diaz','gmail','unico')
print(my_uss.first_name)
print(my_uss.last_name)
my_uss.greet_user()
my_uss.describe_user()

my_uss=usser('Leydan','Hernandez','gmail','unico')
print(my_uss.first_name)
print(my_uss.last_name)
my_uss.greet_user()
my_uss.describe_user()

my_uss=usser('Abraham','Sanchez','gmail','unico')
print(my_uss.first_name)
print(my_uss.last_name)
my_uss.greet_user()
my_uss.describe_user()

my_uss=usser('Yaneli','Valdovinos','gmail','unico')
print(my_uss.first_name)
print(my_uss.last_name)
my_uss.greet_user()
my_uss.describe_user()

my_uss=usser('Diego','Garcia','gmail','unico')
print(my_uss.first_name)
print(my_uss.last_name)
my_uss.greet_user()
my_uss.describe_user()

my_uss=usser('Axel','Arrollo','gmail','unico')
print(my_uss.first_name)
print(my_uss.last_name)
my_uss.greet_user()
my_uss.describe_user()

my_uss=usser('ALma','Navarro','gmail','unico')
print(my_uss.first_name)
print(my_uss.last_name)
my_uss.greet_user()
my_uss.describe_user()

my_uss=usser('Esmeralda','Reyes','gmail','unico')
print(my_uss.first_name)
print(my_uss.last_name)
my_uss.greet_user()
my_uss.describe_user()

my_uss=usser('Lancelot','Real','gmail','unico')
print(my_uss.first_name)
print(my_uss.last_name)
my_uss.greet_user()
my_uss.describe_user()


