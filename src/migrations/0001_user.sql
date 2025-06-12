SET TIME ZONE "Europe/Moscow";

CREATE TABLE IF NOT EXISTS "main"."users"(
    "id" SERIAL PRIMARY KEY,
    "username" VARCHAR(255) NOT NULL UNIQUE,
    "password_hash" bytea NOT NULL 
);