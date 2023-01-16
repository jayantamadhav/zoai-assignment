import os
from typing import List
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from routes.user import router as user_router
from routes.hotel import router as hotel_router
from routes.booking import router as booking_router
from routes.rating import router as rating_router
from database import init_db
from dotenv import load_dotenv
load_dotenv()


app = FastAPI(title="ZOAI Assignment",)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.on_event("startup")
async def startup_event():
    init_db(app)


app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(hotel_router, prefix="/hotels", tags=["Hotel"])
app.include_router(booking_router, prefix="/bookings", tags=["Booking"])
app.include_router(rating_router, prefix="/ratings", tags=["Rating"])
