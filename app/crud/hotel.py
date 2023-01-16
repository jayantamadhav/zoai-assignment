from datetime import datetime
from typing import List, Dict

from models.hotel import *
from schemas.hotel import *


# HOTEL
async def list_hotels(limit: int, offset: int) -> List:
    return await Hotel.all().limit(limit).offset(offset)

async def retrieve_hotel(hotel_id: int) -> Dict:
    return await Hotel.get_or_none(id=hotel_id)

async def create_hotel(hotel: HotelSchema) -> Dict:
    _hotel = await Hotel.create(
        name=hotel.name,
        location=hotel.location,
        state=hotel.state,
        hotel_image=hotel.hotel_image,
        gym_available=hotel.gym_available,
        food_available=hotel.food_available,
        allow_booking=hotel.allow_booking
    )
    await _hotel.save()
    return _hotel

async def put_hotel(hotel_id: int, hotel_data: HotelSchema) -> Dict:
    _hotel = await Hotel.get_or_none(id=hotel_id)
    if _hotel is None:
        return { "message" : "Hotel Not Found"}
    _hotel.name=hotel_data.name
    _hotel.location=hotel_data.location
    _hotel.state=hotel_data.state
    _hotel.hotel_image=hotel_data.hotel_image
    _hotel.gym_available=hotel_data.gym_available
    _hotel.food_available=hotel_data.food_available
    _hotel.allow_booking=hotel_data.allow_booking
    await _hotel.save()
    return _hotel

async def delete_hotel(hotel_id: int):
    hotel = await Hotel.get_or_none(id=hotel_id)
    if hotel is None:
        return { "message": "Hotel Not Found" }
    await hotel.delete()
    return {"message": f"Hotel {hotel_id} deleted successfully"}

# ROOM
async def list_hotel_rooms(hotel_id: int, limit: int, offset: int) -> List:
    return await Room.filter(hotel_id=hotel_id).limit(limit).offset(offset)

async def retrieve_room(room_id: int):
    return await Room.get_or_none(id=room_id)

async def create_room(room: RoomSchema):
    _hotel = await Hotel.get_or_none(id=room.hotel_id)
    if _hotel is None:
        return { "message": "Hotel not found" }
    _room = await Room.create(
        hotel = _hotel,
        room_no = room.room_no,
        room_type = room.room_type,
        room_price = room.room_price,
        rating = room.rating,
        image_link = room.image_link
    )
    await _room.save()
    return _room

async def put_room(room_id: int, room: UpdateRoomSchema):
    _room = await Room.get_or_none(id=room_id)
    if _room is None:
        return { "message": "Room not found" }
    _room.room_no = room.room_no
    _room.room_type = room.room_type
    _room.room_price = room.room_price
    _room.rating = room.rating
    _room.image_link = room.image_link
    await _room.save()
    return _room

async def delete_room(room_id: int):
    room = await Room.get_or_none(id=room_id)
    if room is None:
        return { "message": "Room Not Found" }
    await room.delete()
    return {"message": f"Room {room_id} deleted successfully"}
    