from tortoise.models import Model
from tortoise import fields


class Hotel(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=256)
    location = fields.CharField(max_length=512)
    state = fields.CharField(max_length=256)
    hotel_image = fields.CharField(max_length=512)
    gym_available = fields.BooleanField()
    food_available = fields.BooleanField()
    allow_booking = fields.BooleanField()

    def __str__(self):
        return self.id
    

class Room(Model):
    id = fields.IntField(pk=True)
    hotel = fields.ForeignKeyField("models.Hotel", related_name="room")
    room_no = fields.IntField()
    room_type = fields.CharField(max_length=256)
    room_price = fields.IntField()
    rating = fields.IntField()
    image_link = fields.CharField(max_length=512)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    
    def __str__(self):
        return self.id