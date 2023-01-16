from pydantic import BaseModel


class BaseUserSchema(BaseModel):
    username: str
    email: str

    class Config:
        orm_mode=True


class UserSchema(BaseUserSchema):
    email_verified: str
    
    class Config:
        orm_mode=True


class CreateUserSchema(BaseUserSchema):
    password: str
    
    class Config:
        orm_mode=True

class CreateCustomerSchema(CreateUserSchema):
    name: str
    mobile_no: int
    dob: str
    
    class Config:
        orm_mode=True

class CreateAdminSchema(CreateCustomerSchema):
    class Config:
        orm_mode=True

class CreateStaffSchema(CreateUserSchema):
    name: str
    mobile_no: int
    rating: int
    hotel_id: int

    class Config:
        orm_mode=True