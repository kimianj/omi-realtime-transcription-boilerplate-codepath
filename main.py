from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse, HTMLResponse
import stripe
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Stripe
stripe.api_key = os.getenv("STRIPE_SECRET_KEY", "sk_test_your_secret_key_here")
DOMAIN = os.getenv("DOMAIN", "http://localhost:8000")

app = FastAPI()

# Add CORS middleware to allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)


@app.get("/", response_class=HTMLResponse)
def home():
    """Simple test page for the checkout"""
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Stripe Checkout with Promotion Codes</title>
        <style>
            body { font-family: Arial, sans-serif; max-width: 600px; margin: 50px auto; padding: 20px; }
            button { background: #5469d4; color: white; padding: 12px 24px; border: none; border-radius: 4px; font-size: 16px; cursor: pointer; }
            button:hover { background: #4f63d2; }
            .info { background: #f0f9ff; padding: 15px; border-radius: 8px; margin: 20px 0; }
        </style>
    </head>
    <body>
        <h1>🛒 Stripe Checkout with Promotion Codes</h1>
        <div class="info">
            <h3>✨ Features Implemented:</h3>
            <ul>
                <li>✅ Promotion code input field in checkout</li>
                <li>✅ Automatic discount application</li>
                <li>✅ Discounted pricing reflection</li>
                <li>✅ Success/cancel handling</li>
            </ul>
        </div>
        
        <h3>Premium Subscription - $29.99/month</h3>
        <p>Click the button below to start checkout with promotion code support!</p>
        
        <button onclick="createCheckout()">Start Checkout</button>
        
        <script>
            async function createCheckout() {
                try {
                    const response = await fetch('/create-checkout-session', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' }
                    });
                    const data = await response.json();
                    if (data.checkout_url) {
                        window.location.href = data.checkout_url;
                    } else {
                        alert('Error creating checkout session');
                    }
                } catch (error) {
                    console.error('Error:', error);
                    alert('Error creating checkout session');
                }
            }
        </script>
    </body>
    </html>
    """


@app.post("/create-checkout-session")
def create_checkout_session():
    """
    Create a Stripe checkout session with promotion codes enabled.
    Enhanced version with more features from the OMI guide approach.
    """
    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': 'OMI Premium Subscription',
                            'description': 'AI wearable platform with real-time transcription',
                            'images': ['https://www.omi.me/logo.png'],  # Optional: Add product image
                        },
                        'unit_amount': 2999,  # $29.99 in cents
                        'recurring': {
                            'interval': 'month',
                        },
                    },
                    'quantity': 1,
                },
            ],
            mode='subscription',
            # 🎉 KEY FEATURE: Enable promotion codes (simpler than OMI Elements guide!)
            allow_promotion_codes=True,
            
            # Enhanced features inspired by OMI guide
            customer_creation='always',  # Always create customer record
            billing_address_collection='required',  # Collect billing address
            phone_number_collection={'enabled': True},  # Collect phone number
            
            # Custom branding
            custom_text={
                'submit': {'message': 'Complete your OMI subscription'},
            },
            
            # Callback URLs
            success_url=DOMAIN + '/success?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=DOMAIN + '/cancel',
            
            # Metadata for tracking
            metadata={
                'integration': 'omi_realtime_transcription',
                'version': '1.0'
            }
        )
        
        return {
            "checkout_url": checkout_session.url,
            "session_id": checkout_session.id
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/success")
def success(session_id: str):
    """Handle successful payment"""
    try:
        session = stripe.checkout.Session.retrieve(session_id)
        return {
            "message": "Payment successful!",
            "session_id": session_id,
            "customer_email": session.customer_details.email if session.customer_details else None,
            "amount_total": session.amount_total,
            "discount": session.total_details.amount_discount if session.total_details else None
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/cancel")
def cancel():
    """Handle cancelled payment"""
    return {"message": "Payment was cancelled"}


@app.post("/webhook")
def webhook(uid: str, transcript: dict):
    print(transcript)

    # Hint: The transcript contains segments with text data
    # Hint: Access the latest segment with transcript["segments"][-1]["text"]
    # Hint: Return a dictionary with a "message" key and the value being the notification message

    # Task: Implement keyword detection and response logic of your choice
    # example: if the word "tired" is mentioned, return a message notifying the user to take a break

    # TODO: Write your code below this line
    
    # Get the latest transcript segment
    if "segments" in transcript and len(transcript["segments"]) > 0:
        latest_segment = transcript["segments"][-1]
        latest_text = latest_segment.get("text", "").lower()
        
        # Keyword detection logic
        if "tired" in latest_text:
            return {"message": "You mentioned being tired. Consider taking a break to rest and recharge!"}
        elif "break" in latest_text:
            return {"message": "Good idea! Taking regular breaks is important for productivity and well-being."}
        elif "stressed" in latest_text or "stress" in latest_text:
            return {"message": "It sounds like you might be feeling stressed. Try some deep breathing or a short walk."}
        elif "hungry" in latest_text:
            return {"message": "Time for a snack! Make sure to fuel your body with nutritious food."}
        elif "help" in latest_text:
            return {"message": "I'm here to help! Feel free to ask if you need assistance with anything."}
        elif "thank" in latest_text:
            return {"message": "You're welcome! I'm glad I could help."}
        else:
            return {"message": f"Received transcript: '{latest_text}'"}
    else:
        return {"message": "No transcript segments found"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
