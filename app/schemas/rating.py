from pydantic import BaseModel

class BaseRatingModel(BaseModel):
    rating: int
    comment: str
    
    class Config:
        orm_mode=True
        
class CreateUpdateRatingSchema(BaseRatingModel):
    booking_id: int
    
    class Config:
        orm_mode=True
