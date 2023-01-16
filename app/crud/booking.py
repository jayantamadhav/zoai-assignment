from datetime import datetime
from typing import List, Dict

from models.user import Customer
from models.hotel import Room
from models.booking import *
from schemas.booking import *


# BOOKINGS
async def list_bookings(limit: int, offset: int) -> List:
    return await Booking.all().limit(limit).offset(offset)

async def retrieve_booking(booking_id: int) -> Dict:
    booking = await Booking.get_or_none(id=booking_id)
    if booking is None:
        return {"message": "Booking Not Found"}
    return booking

async def create_booking(booking: CreateBookingSchema) -> Dict:
    customer = await Customer.get_or_none(id=booking.customer_id)
    if customer is None:
        return {"message":"Customer not found"}
    room = await Room.get_or_none(id=booking.room_id)
    if room is None:
        return {"message":"Room not found"}
    _booking = await Booking.create(
        customer=customer,
        room=room,
        booking_start_date=datetime.fromtimestamp(booking.booking_start_date),
        booking_end_date=datetime.fromtimestamp(booking.booking_end_date),
        booking_status=booking.booking_status,
        checks_complete=booking.checks_complete,
        total_price=booking.total_price
    )
    await _booking.save()
    return _booking

async def put_booking(booking_id: int, booking: CreateBookingSchema) -> Dict:
    _booking = await Booking.get_or_none(id=booking_id)
    if _booking is None:
        return {"message":"Booking Not Found"}
    _booking.booking_start_date=datetime.fromtimestamp(booking.booking_start_date)
    _booking.booking_end_date=datetime.fromtimestamp(booking.booking_end_date)
    _booking.checks_complete=booking.checks_complete
    _booking.booking_status=booking.booking_status
    _booking.total_price=booking.total_price
    await _booking.save()
    return _booking

async def delete_booking(booking_id: int):
    _booking = await Booking.get_or_none(id=booking_id)
    if _booking is None:
        return {"message":"Booking Not Found"}
    await _booking.delete()
    return {"message": f"Booking {booking_id} deleted successfully"}



# PAYMENTS
async def list_payments(limit: int, offset: int) -> List:
    return await Payment.all().limit(limit).offset(offset)

async def retrieve_payment(payment_id: int) -> Dict:
    payment = await Payment.get_or_none(id=payment_id)
    if payment is None:
        return {"message":"Payment Not Found"}
    return payment

async def create_payment(payment: CreateUpdatePaymentSchema) -> Dict:
    _booking = await Booking.get_or_none(id=payment.booking_id)
    if _booking is None:
        return {"message":"Booking not found"}
    _payment = await Payment.create(
        booking=_booking,
        amount=payment.amount,
        email=payment.email,
        status=payment.status,
        notes=payment.notes
    )
    await _payment.save()
    return _payment

async def put_payment(payment_id: int, payment: CreateUpdatePaymentSchema) -> Dict:
    _payment = await Payment.get_or_none(id=payment_id)
    if _payment is None:
        return {"message":"Payment not found"}
    _payment.email=payment.email
    _payment.status=payment.status
    _payment.notes=payment.notes
    _payment.amount=payment.amount
    await _payment.save()
    print(_payment.amount)
    return _payment

async def delete_payment(payment_id: int) -> Dict:
    _payment = await Payment.get_or_none(id=payment_id)
    if _payment is None:
        return {"message":"Payment not found"}
    await _payment.delete()
    return {"message": f"Payment {payment_id} deleted successfully"}
