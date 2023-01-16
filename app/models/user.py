from tortoise.models import Model
from tortoise import fields


class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=255)
    email = fields.CharField(max_length=255)
    password = fields.CharField(max_length=512)
    email_verified = fields.BooleanField(default=False)

    def __str__(self):
        return self.id


class Admin(Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField("models.User", related_name="admins")
    name = fields.CharField(max_length=256)
    mobile_no = fields.BigIntField()
    mobile_verified = fields.BooleanField(default=False)
    dob = fields.DateField()
    is_active = fields.BooleanField(default=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    
    def __str__(self):
        return self.id


class Staff(Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField("models.User", related_name="staffs")
    name = fields.CharField(max_length=256)
    mobile_no = fields.BigIntField()
    mobile_verified = fields.BooleanField(default=False)
    rating = fields.IntField()
    hotel = fields.ForeignKeyField("models.Hotel", related_name="hotel")
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    
    def __str__(self):
        return self.id



class Customer(Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField("models.User", related_name="customers")
    name = fields.CharField(max_length=256)
    mobile_no = fields.BigIntField()
    mobile_verified = fields.BooleanField(default=False)
    dob = fields.DateField()
    is_active = fields.BooleanField(default=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    
    def __str__(self):
        return self.id