CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    phone_number VARCHAR(20) UNIQUE NOT NULL,
    otp_verified BOOLEAN DEFAULT FALSE
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    ticket_type VARCHAR(50),
    amount FLOAT,
    status VARCHAR(20) DEFAULT 'Pending'
);

