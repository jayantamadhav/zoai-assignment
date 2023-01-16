from tortoise.models import Model
from tortoise import fields


class Rating(Model):
    id = fields.IntField(pk=True)
    rating = fields.IntField()
    booking = fields.ForeignKeyField("models.Booking", related_name="rating")
    comment = fields.CharField(max_length=512)    
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_add=True)

    def __str__(self):
        return self.id
    