#importar las dependcencias de flask
from flask import Flask, render_template
#crear el objeto de tipo flask
app = Flask(__name__)
#Crear una primera ruta de pruaba 
@app.route("/HOlA MUNDO")
def hola():
    return 'helou world'


#ruta de paises
@app.route("/paises")
def paises():
    username="Cristian Daniel"
    #paises=["Peru","Chile","peru"]
    
    continentes = [
        {
            "nombre" : "America",
            "poblacion" : 1036900579,
            "superficie" : "42549000 km²",
            "densidad" : "22,8 km²",
            "Num paises" : 35,
            "paises":[
               {"nom":"Colombia",
               "mon":"Peso",
               "cap":"Bogotá",
               "pob":"51,52 m"
               },
               {
                "nom":"Ecuador",
                "mon":"Dólar",
                "cap":"Quito",
                "pob":"17,8 millones"
               },
                {
                "nom":"Peru",
                "mon":"Sol",
                "cap":"Lima",
                "pob":"33,72 millone"
               }
            ]
        },
        {
            "nombre" : "Europa",
            "poblacion" : 747747395,
            "superficie" :   "10530751 km²",
            "densidad" : "71 km²",
            "Num paises" : 50,
            "paises":[
                 {
                "nom":"Alemania",
                "mon":"Euro",
                "cap":"Berlin",
                "pob":"34,72 millone"
               }
            ]
        },
        {
            "nombre" : "Asia",
            "poblacion" : 4598168800,
            "superficie" : "44541138 km²",
            "densidad" : "103,2 km²", 
            "Num paises" : 51,
            "paises":[
                {
                "nom":"China",
                "mon":"Yuan Chino",
                "cap":"Pekín",
                "pob":"88,72 millone"
               },
                  
               
              
            ]
        },
        {
            "nombre" : "Africa",
            "poblacion" : 1320000000,
            "superficie" : "30221535 km²",
            "densidad" : "43,7 km²", 
            "Num paises" : 54,
            "paises":[
               {
                "nom":"Nigeria",
                "mon":"Naira",
                "cap":"Abuya",
                "pob":"22,06 millone"
               },
                 
            ]
        },
        {
            "nombre" : "Oceanía",
            "poblacion" : 41117432,
            "superficie" : "8542499 km²",
            "densidad" : "4,56 km²",
            "Num paises" : 15,
            "paises":[
                {
                "nom":"Australia",
                "mon":"Dólar Australiano",
                "cap":"Camberra",
                "pob":"26,04 millone"
                }
            ]
            
        }
    ]
    
    return  render_template("paises.html",username=username,continentes=continentes)
