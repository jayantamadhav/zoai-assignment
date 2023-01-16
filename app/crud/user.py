from datetime import datetime
from typing import List, Dict

from utils import Hasher
from models.user import *
from models.hotel import *

async def list_users(limit: int, offset: int) -> List:
    return await User.all()

async def list_customers(limit: int, offset: int) -> List:
    return await Customer.all()

async def list_admins(limit: int, offset: int) -> List:
    return await Admin.all()

async def list_staffs(limit: int, offset: int) -> List:
    return await Staff.all()

model_map = {
    "user": User, 
    "customer": Customer,
    "admin": Admin,
    "staff": Staff
}

async def list_all(user_type: str, limit: int, offset: int) -> List:
    return await model_map[user_type].all().limit(limit).offset(offset)

async def retrieve(user_type: str, id: int) -> Dict:
    return await model_map[user_type].get_or_none(id=id)


async def create(model_type: str, *args, **kwargs) -> Dict:
    user_exists = await User.get_or_none(username=kwargs.get("username"))
    if user_exists:
        return { "message" : "User with username/email exists!"}
    user = await User.create(
        username=kwargs.get("username"),
        email=kwargs.get("email"),  
        password=Hasher.get_password_hash(kwargs.get("password"))  
    )
    await user.save()
    if model_type == "staff":
        hotel = await Hotel.get_or_none(id=kwargs.get("hotel_id"))
        _model_obj = await model_map[model_type].create(
            user=user,
            name=kwargs.get("name"),
            mobile_no=kwargs.get("mobile_no"),
            rating = kwargs.get("rating"),
            hotel = hotel
        )
    else:
        dob = datetime.strptime(kwargs.get("dob"), "%d/%m/%Y").date()
        _model_obj = await model_map[model_type].create(
            user=user,
            name=kwargs.get("name"),
            mobile_no=kwargs.get("mobile_no"),
            dob=dob
        )
    await _model_obj.save()
    return _model_obj