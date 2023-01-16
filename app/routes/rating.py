from fastapi import APIRouter

from schemas.rating import *
from crud.rating import *

router = APIRouter()


# RATINGS
@router.get("")
async def all_ratings(limit: int=20, offset: int=0):
    return await list_ratings(limit, offset)

@router.get("/{rating_id}")
async def get_rating(rating_id: int):
    return await retrieve_rating(rating_id)

@router.post("")
async def add_rating(rating: CreateUpdateRatingSchema):
    return await create_rating(rating)

@router.put("/{rating_id}")
async def update_rating(rating_id: int, rating: CreateUpdateRatingSchema):
    return await put_rating(rating_id, rating)

@router.delete("/{rating_id}")
async def remove_rating(rating_id: int):
    return await delete_rating(rating_id)

