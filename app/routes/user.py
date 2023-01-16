from fastapi import APIRouter
from typing import List

from crud.user import *
from schemas.user import *


router = APIRouter()


@router.get("")
async def all_users(limit: int = 20, offset: int = 0):
    return await list_users(limit, offset)

@router.get("/{user_id}")
async def get_user(user_id: int):
    user = await retrieve("user", user_id)
    return user if user else {}


@router.get("/customer")
async def all_customers(limit: int = 20, offset: int = 0):
    return await list_customers(limit, offset)

@router.post("/customer")
async def add_customer(customer: CreateCustomerSchema):
    new_user = await create("customer", **customer.dict())
    return new_user

@router.get("/customer/{customer_id}")
async def get_customer(customer_id: int):
    user = await retrieve("customer", customer_id)
    return user if user else {}

@router.post("/admin")
async def add_admin(admin: CreateAdminSchema):
    new_user = await create("admin", **admin.dict())
    return new_user

@router.get("/admin")
async def all_admins(limit: int = 20, offset: int = 0):
    return await list_admins(limit, offset)

@router.get("/admin/{admin_id}")
async def get_admin(admin_id: int):
    user = await retrieve("admin", admin_id)
    return user if user else {}

@router.post("/staff")
async def add_staff(staff: CreateStaffSchema):
    new_user = await create("staff", **staff.dict())
    return new_user

@router.get("/staff")
async def all_staffs(limit: int = 20, offset: int = 0):
    return await list_staffs(limit, offset)

@router.get("/staff/{staff_id}")
async def get_staff(staff_id: int):
    user = await retrieve("staff", staff_id)
    return user if user else {}