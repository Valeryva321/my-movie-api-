
from fastapi import APIRouter
from fastapi import Depends, Path, Query #path es validacion de parametros y Query tambien pero para str
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field # permite crear el esquema de datos, validacion de datos, 
from typing import Optional, List #para dar tipo optional int, list para responder con un listado
from config.database import Session
from models.movie import Movie as MovieModel
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from services.movie import MovieService
from schemas.movie import Movie

movie_router = APIRouter()

@movie_router.get('/movies', tags=['movies'], response_model=List[Movie], status_code=200, dependencies=[Depends(JWTBearer())])
def get_movies() -> List[Movie]:
    db = Session()
    result = MovieService(db).get_movies() #consultar los datos
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

#parametros de ruta

@movie_router.get('/movies/{id}', tags=['movies'], response_model=Movie)
def get_movie(id: int=Path(ge=1, le=2000)) -> Movie:
    db = Session()
    result = result = MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "No se encontro"} )
    
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

#parametros query filtrado por categoria 

@movie_router.get('/movies/', tags=['movies'], response_model=List[Movie]) 
def get_movies_by_category(category: str= Query(min_length=5, max_length=15)) -> List[Movie]:
    db =Session()
    result = MovieService(db).get_movies_by_category(category)
    
    if not result:
       return JSONResponse(status_code=404, content={"message": "No se encontro"} )  
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

#metodo post

@movie_router.post('/movies', tags=['movies'], response_model=dict, status_code=201)
def create_movie(movie:Movie) -> dict:
    db = Session()
    MovieService(db).create_movie(movie)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado la pelicula"})

#metodo put

@movie_router.put('/movies/{id}', tags=['movies'], response_model=dict, status_code=200)
def update_movie(id: int, movie:Movie) -> dict:
    db= Session()
    result = MovieService(db).get_movie(id)
    if not result:
       return JSONResponse(status_code=404, content={"message": "No se encontro"} ) 
    
    MovieService(db).update_movie(id, movie)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado la película"})
        
            
# metodo delete

@movie_router.delete('/movies/{id}', tags=['movies'], response_model=dict, status_code=200)
def delete_movie(id: int)-> dict:
    db = Session()
    result: MovieModel = db.query(MovieModel).filter(MovieModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={"message": "No se encontró"})
    MovieService(db).delete_movie(id)
    return JSONResponse(status_code=200, content={"message": "Se ha eliminado la película"}) 