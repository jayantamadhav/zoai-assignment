from tortoise.models import Model
from tortoise import fields


class Booking(Model):
    id = fields.IntField(pk=True)
    customer = fields.ForeignKeyField("models.Customer", related_name="bookings")
    room = fields.ForeignKeyField("models.Room", related_name="booking")
    booking_start_date = fields.DatetimeField()
    booking_end_date = fields.DatetimeField()
    booking_status = fields.CharField(max_length=256)
    checks_complete = fields.BooleanField()
    total_price = fields.FloatField()


class Payment(Model):
    id = fields.IntField(pk=True)
    booking = fields.ForeignKeyField("models.Booking", related_name="payments")
    amount = fields.FloatField()
    email = fields.CharField(max_length=256)
    status = fields.CharField(max_length=64)
    notes = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)
