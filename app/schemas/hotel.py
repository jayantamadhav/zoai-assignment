from pydantic import BaseModel


class HotelSchema(BaseModel):
    name: str
    location: str
    state: str
    hotel_image: str
    gym_available: bool
    food_available: bool
    allow_booking: bool
    
    class Config:
        orm_mode=True


class RoomSchema(BaseModel):
    hotel_id: int
    room_no: int
    room_type: str
    room_price: int
    rating: int
    image_link: str
    
    class Config:
        orm_mode=True


class UpdateRoomSchema(BaseModel):
    room_no: int
    room_type: str
    room_price: int
    rating: int
    image_link: str
    
    class Config:
        orm_mode=True

