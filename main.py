from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from routers.movie import movie_router
from routers.user import user_router

app= FastAPI()
app.title = "Mi aplicacion con fastAPI"

app.middleware(ErrorHandler)
app.include_router(movie_router)
app.include_router(user_router)

Base.metadata.create_all(bind=engine)



movies =  [
    {
        'id': 1,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'    
    }, 
    {
        'id': 2,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'    
    } 
]

@app.get('/', tags=['Home'])
def message():
   # return "Burris eres el amor de mi vida"
   return HTMLResponse ("<h1>hola burris eres el amor de mi vida</h1>")


            
        

# en la terminal debo escribir uvicorn main:app --reload esto me hace referencia al archivo y al nombre que le di del FastAPI() y que se cargue solo si hay modificacion
#si le quiero agregar yo el puerto local uso adicional --port 5000 en este caso le asigne el puerto 5000
# si quiero que no sea local si no q se pueda ver desde cualquier computador o celular colgado a esta misma red uso --host 0.0.0.0
