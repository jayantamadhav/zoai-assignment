from pydantic import BaseModel


class BaseBookingSchema(BaseModel):
    booking_start_date: int
    booking_end_date: int
    booking_status: str
    checks_complete: bool
    total_price: float
    
    class Config:
        orm_mode=True


class CreateBookingSchema(BaseBookingSchema):
    customer_id: int
    room_id: int

    class Config:
        orm_mode=True


class BasePaymentSchema(BaseModel):
    amount: float
    email: str
    status: str
    notes: str
    
    class Config:
        orm_mode=True


class CreateUpdatePaymentSchema(BasePaymentSchema):
    booking_id: int
    
    class Config:
        orm_mode=True       

     