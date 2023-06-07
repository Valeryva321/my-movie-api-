from pydantic import BaseModel, Field
from typing import Optional, List


#este codigo es para validación de datos
class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=5, max_length=15)
    overview: str = Field(min_length=15, max_length=50)
    year: int = Field(le=2023)
    rating: float = Field( ge=1, le=10)
    category: str = Field(min_length=5, max_length=15)
    
    class Config:
         schema_extra= {
            "example": {
                "id": 1,
                "title": "Mi pelicula",
                "overview": "Descripción de la pelicula",
                "year": 2023,
                "rating": 9.5,
                "category": "Animación"
            }
        }
# hasta aqui es validación de datos