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
    """OMI-styled demo page showing promotion codes feature"""
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>OMI - AI Wearable Platform | Promotion Codes Demo</title>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            
            body {
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                color: #333;
            }
            
            .header {
                background: rgba(255, 255, 255, 0.95);
                backdrop-filter: blur(10px);
                padding: 1rem 2rem;
                display: flex;
                justify-content: space-between;
                align-items: center;
                box-shadow: 0 2px 20px rgba(0,0,0,0.1);
            }
            
            .logo {
                font-size: 2rem;
                font-weight: bold;
                background: linear-gradient(135deg, #667eea, #764ba2);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
            }
            
            .nav-links {
                display: flex;
                gap: 2rem;
                list-style: none;
            }
            
            .nav-links a {
                text-decoration: none;
                color: #666;
                font-weight: 500;
                transition: color 0.3s;
            }
            
            .nav-links a:hover { color: #667eea; }
            
            .container {
                max-width: 1200px;
                margin: 0 auto;
                padding: 4rem 2rem;
            }
            
            .hero {
                text-align: center;
                color: white;
                margin-bottom: 4rem;
            }
            
            .hero h1 {
                font-size: 3.5rem;
                margin-bottom: 1rem;
                font-weight: 700;
            }
            
            .hero p {
                font-size: 1.2rem;
                opacity: 0.9;
                max-width: 600px;
                margin: 0 auto 2rem;
                line-height: 1.6;
            }
            
            .demo-section {
                background: white;
                border-radius: 20px;
                padding: 3rem;
                box-shadow: 0 20px 60px rgba(0,0,0,0.1);
                margin-bottom: 3rem;
            }
            
            .comparison {
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 3rem;
                margin-bottom: 3rem;
            }
            
            .before, .after {
                padding: 2rem;
                border-radius: 15px;
                text-align: center;
            }
            
            .before {
                background: #fee;
                border: 2px solid #fcc;
            }
            
            .after {
                background: #efe;
                border: 2px solid #cfc;
            }
            
            .before h3 { color: #c33; }
            .after h3 { color: #3c3; }
            
            .feature-list {
                list-style: none;
                padding: 1rem 0;
            }
            
            .feature-list li {
                padding: 0.5rem 0;
                display: flex;
                align-items: center;
                gap: 0.5rem;
            }
            
            .product-card {
                background: linear-gradient(135deg, #667eea, #764ba2);
                color: white;
                padding: 2rem;
                border-radius: 15px;
                text-align: center;
                margin: 2rem 0;
            }
            
            .product-card h3 {
                font-size: 1.8rem;
                margin-bottom: 1rem;
            }
            
            .price {
                font-size: 2.5rem;
                font-weight: bold;
                margin: 1rem 0;
            }
            
            .btn-primary {
                background: white;
                color: #667eea;
                border: none;
                padding: 1rem 2rem;
                border-radius: 50px;
                font-size: 1.1rem;
                font-weight: 600;
                cursor: pointer;
                transition: all 0.3s;
                box-shadow: 0 4px 15px rgba(0,0,0,0.2);
            }
            
            .btn-primary:hover {
                transform: translateY(-2px);
                box-shadow: 0 8px 25px rgba(0,0,0,0.3);
            }
            
            .promo-highlight {
                background: #fff3cd;
                border: 2px solid #ffeaa7;
                border-radius: 10px;
                padding: 1.5rem;
                margin: 2rem 0;
                text-align: center;
            }
            
            .promo-highlight h4 {
                color: #856404;
                margin-bottom: 0.5rem;
            }
            
            @media (max-width: 768px) {
                .comparison { grid-template-columns: 1fr; }
                .hero h1 { font-size: 2.5rem; }
                .container { padding: 2rem 1rem; }
            }
        </style>
    </head>
    <body>
        <header class="header">
            <div class="logo">OMI</div>
            <nav>
                <ul class="nav-links">
                    <li><a href="#product">Product</a></li>
                    <li><a href="#apps">Apps</a></li>
                    <li><a href="#docs">Docs</a></li>
                    <li><a href="#discord">Discord</a></li>
                </ul>
            </nav>
        </header>
        
        <div class="container">
            <div class="hero">
                <h1>OMI AI Platform</h1>
                <p>The #1 Open Source AI wearable: Experiment with how you capture and manage conversations with real-time transcription and AI feedback.</p>
            </div>
            
            <div class="demo-section">
                <h2 style="text-align: center; margin-bottom: 2rem; color: #333;">🎉 NEW FEATURE: Promotion Codes in Checkout</h2>
                
                <div class="comparison">
                    <div class="before">
                        <h3>❌ Before (Current OMI)</h3>
                        <ul class="feature-list">
                            <li>❌ No promotion code field</li>
                            <li>❌ Users cannot apply discounts</li>
                            <li>❌ All payments at full price</li>
                            <li>❌ No marketing flexibility</li>
                        </ul>
                    </div>
                    
                    <div class="after">
                        <h3>✅ After (With Our Enhancement)</h3>
                        <ul class="feature-list">
                            <li>✅ Promotion code input field</li>
                            <li>✅ Automatic discount application</li>
                            <li>✅ Real-time price updates</li>
                            <li>✅ Marketing campaign support</li>
                        </ul>
                    </div>
                </div>
                
                <div class="promo-highlight">
                    <h4>🎯 Implementation: Just ONE line of code!</h4>
                    <code style="background: #f8f9fa; padding: 0.5rem; border-radius: 5px;">allow_promotion_codes=True</code>
                </div>
            </div>
            
            <div class="product-card">
                <h3>🎧 OMI Dev Kit 2</h3>
                <p>Real-time conversation transcription and processing with AI feedback</p>
                <div class="price">$69.99</div>
                <p style="opacity: 0.9; margin-bottom: 2rem;">
                    ✨ Speak, Transcribe, Summarize conversations<br>
                    🧠 Action items, summaries and memories<br>
                    📱 Available on iOS and Android
                </p>
                
                <button class="btn-primary" onclick="createCheckout()">
                    🛒 Order Now (Try Promotion Codes!)
                </button>
            </div>
            
            <div style="text-align: center; color: white; margin-top: 3rem;">
                <p><strong>Demo Instructions:</strong></p>
                <p>1. Click "Order Now" to see Stripe checkout with promotion code field</p>
                <p>2. Look for the "Promotion code" link in the checkout</p>
                <p>3. Try entering test codes (create them in Stripe Dashboard first)</p>
            </div>
        </div>
        
        <script>
            async function createCheckout() {
                try {
                    const response = await fetch('/create-checkout-session', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' }
                    });
                    const data = await response.json();
                    if (data.checkout_url) {
                        // Open in new tab so they can see the comparison
                        window.open(data.checkout_url, '_blank');
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
                            'name': 'OMI Dev Kit 2',
                            'description': 'Real-time conversation transcription and processing. Action items, summaries and memories. Thousands of community apps.',
                            'images': ['https://cdn.shopify.com/s/files/1/0854/1790/7844/files/omi-necklace-hero.png'],
                        },
                        'unit_amount': 6999,  # $69.99 in cents (actual OMI price)
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',  # One-time payment for hardware
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


@app.get("/api/demo-info")
def demo_info():
    """API endpoint showing the promotion codes implementation details"""
    return {
        "feature": "Stripe Promotion Codes Integration",
        "implementation": {
            "key_parameter": "allow_promotion_codes=True",
            "location": "stripe.checkout.Session.create()",
            "effort": "Single line of code change"
        },
        "benefits": [
            "Promotion code input field appears automatically",
            "Real-time discount application",
            "Improved conversion rates",
            "Marketing campaign flexibility",
            "No additional UI development needed"
        ],
        "technical_details": {
            "stripe_api_version": "Latest",
            "checkout_mode": "payment",  # For OMI hardware
            "product": {
                "name": "OMI Dev Kit 2",
                "price": "$69.99",
                "description": "Real-time conversation transcription and processing"
            }
        },
        "demo_url": "http://localhost:8000",
        "test_instructions": [
            "1. Visit the demo homepage",
            "2. Click 'Order Now' button",
            "3. Look for 'Promotion code' link in Stripe checkout",
            "4. Enter test promotion codes (create in Stripe Dashboard)",
            "5. See automatic discount application"
        ]
    }


@app.get("/api/implementation-guide", response_class=HTMLResponse)
def implementation_guide():
    """Technical implementation guide for OMI developers"""
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>OMI Promotion Codes - Implementation Guide</title>
        <style>
            body { font-family: 'Monaco', 'Menlo', monospace; max-width: 1000px; margin: 0 auto; padding: 2rem; background: #1e1e1e; color: #d4d4d4; }
            .header { background: linear-gradient(135deg, #667eea, #764ba2); color: white; padding: 2rem; border-radius: 10px; margin-bottom: 2rem; }
            .code-block { background: #2d2d2d; padding: 1.5rem; border-radius: 8px; margin: 1rem 0; border-left: 4px solid #667eea; }
            .highlight { background: #3c3c3c; padding: 0.2rem 0.5rem; border-radius: 4px; color: #9cdcfe; }
            .section { margin: 2rem 0; }
            .before-after { display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; margin: 2rem 0; }
            .before { background: #4a1a1a; padding: 1.5rem; border-radius: 8px; }
            .after { background: #1a4a1a; padding: 1.5rem; border-radius: 8px; }
        </style>
    </head>
    <body>
        <div class="header">
            <h1>🚀 OMI Promotion Codes Implementation</h1>
            <p>Complete technical guide for adding promotion codes to OMI's Stripe checkout</p>
        </div>
        
        <div class="section">
            <h2>📋 Current vs Enhanced Implementation</h2>
            <div class="before-after">
                <div class="before">
                    <h3>❌ Current OMI Code</h3>
                    <div class="code-block">
checkout_session = stripe.checkout.Session.create(
    payment_method_types=['card'],
    line_items=[...],
    mode='payment',
    success_url='...',
    cancel_url='...'
    # Missing promotion codes!
)
                    </div>
                </div>
                
                <div class="after">
                    <h3>✅ Enhanced OMI Code</h3>
                    <div class="code-block">
checkout_session = stripe.checkout.Session.create(
    payment_method_types=['card'],
    line_items=[...],
    mode='payment',
    <span class="highlight">allow_promotion_codes=True,</span>  # 🎉 ADD THIS!
    success_url='...',
    cancel_url='...'
)
                    </div>
                </div>
            </div>
        </div>
        
        <div class="section">
            <h2>🔧 Step-by-Step Implementation</h2>
            
            <h3>Step 1: Locate OMI's Checkout Code</h3>
            <p>Find the file containing your Stripe checkout session creation (likely in your payment service)</p>
            
            <h3>Step 2: Add the Parameter</h3>
            <div class="code-block">
# In your OMI backend payment handler:
checkout_session = stripe.checkout.Session.create(
    # ... existing parameters ...
    allow_promotion_codes=True,  # ← Add this single line!
    # ... rest of parameters ...
)
            </div>
            
            <h3>Step 3: Create Promotion Codes in Stripe</h3>
            <p>1. Go to Stripe Dashboard → Products → Coupons</p>
            <p>2. Create coupons (e.g., 20% off, $10 off)</p>
            <p>3. Go to Promotion Codes → Create codes</p>
            <p>4. Link codes to coupons</p>
            
            <h3>Step 4: Test & Deploy</h3>
            <p>✅ Test in Stripe test mode</p>
            <p>✅ Verify promotion code field appears</p>
            <p>✅ Test discount application</p>
            <p>✅ Deploy to production</p>
        </div>
        
        <div class="section">
            <h2>💡 Benefits for OMI</h2>
            <ul>
                <li>🎯 <strong>Marketing Flexibility:</strong> Run discount campaigns</li>
                <li>📈 <strong>Conversion Boost:</strong> Reduce cart abandonment</li>
                <li>🎉 <strong>User Experience:</strong> Customers love discounts</li>
                <li>⚡ <strong>Zero UI Work:</strong> Stripe handles the interface</li>
                <li>🔒 <strong>Secure:</strong> Stripe validates codes automatically</li>
            </ul>
        </div>
        
        <div class="section">
            <h2>🧪 Live Demo</h2>
            <p>This demo is running at <strong>http://localhost:8000</strong></p>
            <p>Click "Order Now" to see the promotion codes feature in action!</p>
        </div>
        
        <div style="text-align: center; margin-top: 3rem; padding: 2rem; background: #2d2d2d; border-radius: 10px;">
            <h3>Ready to implement? It's just ONE line of code! 🚀</h3>
            <code style="font-size: 1.2rem; color: #9cdcfe;">allow_promotion_codes=True</code>
        </div>
    </body>
    </html>
    """


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
