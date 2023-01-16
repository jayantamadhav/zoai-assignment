from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);
CREATE TABLE IF NOT EXISTS "hotel" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(256) NOT NULL,
    "location" VARCHAR(512) NOT NULL,
    "state" VARCHAR(256) NOT NULL,
    "hotel_image" VARCHAR(512) NOT NULL,
    "gym_available" BOOL NOT NULL,
    "food_available" BOOL NOT NULL,
    "allow_booking" BOOL NOT NULL
);
CREATE TABLE IF NOT EXISTS "room" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "room_no" INT NOT NULL,
    "room_type" VARCHAR(256) NOT NULL,
    "room_price" INT NOT NULL,
    "rating" INT NOT NULL,
    "image_link" VARCHAR(512) NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "hotel_id" INT NOT NULL REFERENCES "hotel" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "user" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "username" VARCHAR(255) NOT NULL,
    "email" VARCHAR(255) NOT NULL,
    "password" VARCHAR(512) NOT NULL,
    "email_verified" BOOL NOT NULL  DEFAULT False
);
CREATE TABLE IF NOT EXISTS "admin" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(256) NOT NULL,
    "mobile_no" BIGINT NOT NULL,
    "mobile_verified" BOOL NOT NULL  DEFAULT False,
    "dob" DATE NOT NULL,
    "is_active" BOOL NOT NULL  DEFAULT True,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "user_id" INT NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "customer" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(256) NOT NULL,
    "mobile_no" BIGINT NOT NULL,
    "mobile_verified" BOOL NOT NULL  DEFAULT False,
    "dob" DATE NOT NULL,
    "is_active" BOOL NOT NULL  DEFAULT True,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "user_id" INT NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "booking" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "booking_start_date" TIMESTAMPTZ NOT NULL,
    "booking_end_date" TIMESTAMPTZ NOT NULL,
    "booking_status" VARCHAR(256) NOT NULL,
    "checks_complete" BOOL NOT NULL,
    "total_price" DOUBLE PRECISION NOT NULL,
    "customer_id" INT NOT NULL REFERENCES "customer" ("id") ON DELETE CASCADE,
    "room_id" INT NOT NULL REFERENCES "room" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "payment" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "amount" DOUBLE PRECISION NOT NULL,
    "email" VARCHAR(256) NOT NULL,
    "status" VARCHAR(64) NOT NULL,
    "notes" TEXT NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "booking_id" INT NOT NULL REFERENCES "booking" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "rating" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "rating" INT NOT NULL,
    "comment" VARCHAR(512) NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL,
    "booking_id" INT NOT NULL REFERENCES "booking" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "staff" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(256) NOT NULL,
    "mobile_no" BIGINT NOT NULL,
    "mobile_verified" BOOL NOT NULL  DEFAULT False,
    "rating" INT NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "hotel_id" INT NOT NULL REFERENCES "hotel" ("id") ON DELETE CASCADE,
    "user_id" INT NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
