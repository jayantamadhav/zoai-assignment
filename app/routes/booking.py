from fastapi import APIRouter

from schemas.booking import *
from crud.booking import *

router = APIRouter()


# BOOKINGS

@router.get("")
async def all_bookings(limit: int=20, offset: int=0):
    return await list_bookings(limit, offset)

@router.get("/{booking_id}")
async def get_booking(booking_id: int):
    return await retrieve_booking(booking_id)

@router.post("")
async def add_booking(booking: CreateBookingSchema):
    return await create_booking(booking)

@router.put("/{booking_id}")
async def update_booking(booking_id: int, booking: BaseBookingSchema):
    return await put_booking(booking_id, booking)

@router.delete("/{booking_id}")
async def remove_booking(booking_id: int):
    return await delete_booking(booking_id)



# PAYMENT

@router.get("/payments")
async def all_payments(limit: int=20, offset: int=0):
    return await list_payments(limit, offset)

@router.get("/payments/{payment_id}")
async def get_payment(payment_id: int):
    return await retrieve_payment(payment_id)

@router.post("/payments")
async def add_payment(payment: CreateUpdatePaymentSchema):
    return await create_payment(payment)

@router.put("/payments/{payment_id}")
async def update_payment(payment_id: int, payment: BasePaymentSchema):
    return await put_payment(payment_id, payment)

@router.delete("/payments/{payment_id}")
async def remove_payment(payment_id: int):
    return await delete_payment(payment_id)