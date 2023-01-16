from datetime import datetime
from typing import List, Dict

from models.rating import *
from models.booking import *
from schemas.rating import *


# RATING
async def list_ratings(limit: int, offset: int):
    return await Rating.all().limit(limit).offset(offset)

async def retreive_rating(rating_id: int):
    rating = await Rating.get_or_none(id=rating_id)
    if rating is None:
        return {"message": "Rating Not Found"}
    return rating

async def create_rating(rating: CreateUpdateRatingSchema) -> Dict:
    booking = await Booking.get_or_none(id=rating.customer_id)
    if booking is None:
        return {"message":"Booking not found"}
    _rating = await Rating.create(
        booking=booking,
        rating=rating.rating,
        comment=rating.comment,
    )
    await _rating.save()
    return _rating

async def put_rating(rating_id: int, rating: CreateUpdateRatingSchema) -> Dict:
    _rating = await rating.get_or_none(id=rating_id)
    if _rating is None:
        return {"message":"Rating Not Found"}
    _rating.rating=rating.rating
    _rating.comment=rating.comment
    await _rating.save()
    return _rating

async def delete_rating(rating_id: int):
    _rating = await Rating.get_or_none(id=rating_id)
    if _rating is None:
        return {"message":"Rating Not Found"}
    await _rating.delete()
    return {"message": f"Rating {rating_id} deleted successfully"}

