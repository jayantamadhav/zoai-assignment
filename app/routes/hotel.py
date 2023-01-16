from fastapi import APIRouter
from typing import List

from crud.hotel import *
from schemas.hotel import *


router = APIRouter()


@router.get("")
async def all_hotels(limit: int=20, offset: int=0):
    return await list_hotels(limit, offset)

@router.post("")
async def add_hotel(hotel: HotelSchema):
    return await create_hotel(hotel)

@router.get("/{hotel_id}")
async def get_hotel(hotel_id: int):
    hotel = await retrieve_hotel(hotel_id)
    return hotel if hotel else {}

@router.put("/{hotel_id}")
async def update_hotel(hotel_id: int, hotel: HotelSchema):
    return await put_hotel(hotel_id, hotel)

@router.delete("/{hotel_id}")
async def remove_hotel(hotel_id: int):
    return await delete_hotel(hotel_id)


@router.get("/{hotel_id}/rooms")
async def all_rooms_of_hotel(hotel_id: int, limit: int=20, offset: int=0):
    return await list_hotel_rooms(hotel_id, limit, offset)

@router.post("/rooms")
async def add_room(room: RoomSchema):
    return await create_room(room)

@router.get("/rooms/{room_id}")
async def get_room(room_id: int):
    room = await retrieve_room(room_id)
    return room if room else {}

@router.put("/rooms/{room_id}")
async def update_room(room_id: int, room: UpdateRoomSchema):
    return await put_room(room_id, room)

@router.delete("/rooms/{room_id}")
async def remove_room(room_id: int):
    return await delete_room(room_id)





