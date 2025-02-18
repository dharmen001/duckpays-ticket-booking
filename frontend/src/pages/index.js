import { useState } from "react";

export default function Home() {
  const [phoneNumber, setPhoneNumber] = useState("");
  const [otp, setOtp] = useState("");
  const [otpSent, setOtpSent] = useState(false);
  const [verified, setVerified] = useState(false);

  const sendOtp = async () => {
    const response = await fetch("http://localhost:8000/send-otp/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ phone_number: phoneNumber }),
    });
    const data = await response.json();
    alert(data.message);
    setOtpSent(true);
  };

  const verifyOtp = async () => {
    const response = await fetch("http://localhost:8000/verify-otp/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ phone_number: phoneNumber, otp: parseInt(otp) }),
    });
    const data = await response.json();
    if (data.message === "OTP Verified") {
      setVerified(true);
    } else {
      alert("Invalid OTP");
    }
  };

  return (
    <div>
      <h1>Welcome to DuckPays Ticket Booking</h1>
      {!verified ? (
        <div>
          <input
            type="text"
            placeholder="Enter Phone Number"
            value={phoneNumber}
            onChange={(e) => setPhoneNumber(e.target.value)}
          />
          <button onClick={sendOtp}>Send OTP</button>
          {otpSent && (
            <>
              <input
                type="text"
                placeholder="Enter OTP"
                value={otp}
                onChange={(e) => setOtp(e.target.value)}
              />
              <button onClick={verifyOtp}>Verify OTP</button>
            </>
          )}
        </div>
      ) : (
        <h2>OTP Verified! Proceed with Booking.</h2>
      )}
    </div>
  );
}
