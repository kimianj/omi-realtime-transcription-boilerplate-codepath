# 🚀 Stripe Checkout with Promotion Codes - Setup Guide

## 📋 What We Implemented

✅ **Promotion code input field** - Users can enter promo codes during checkout  
✅ **Automatic discount application** - Valid codes automatically apply discounts  
✅ **Discounted pricing reflection** - Checkout shows updated pricing  
✅ **Success/cancel handling** - Proper callback endpoints  

## 🔧 Setup Steps

### 1. Install Dependencies
```bash
uv sync
```

### 2. Get Your Stripe Keys
1. Go to [Stripe Dashboard](https://dashboard.stripe.com/apikeys)
2. Copy your **Secret Key** (starts with `sk_test_`)
3. Copy your **Publishable Key** (starts with `pk_test_`)

### 3. Set Environment Variables
Create a `.env` file in your project root:
```env
STRIPE_SECRET_KEY=sk_test_your_actual_secret_key_here
STRIPE_PUBLISHABLE_KEY=pk_test_your_actual_publishable_key_here
DOMAIN=http://localhost:8000
```

**OR** set them directly in your terminal:
```bash
# Windows PowerShell
$env:STRIPE_SECRET_KEY="sk_test_your_actual_secret_key_here"

# Windows CMD
set STRIPE_SECRET_KEY=sk_test_your_actual_secret_key_here

# Mac/Linux
export STRIPE_SECRET_KEY=sk_test_your_actual_secret_key_here
```

### 4. Create Test Promotion Codes in Stripe
1. Go to [Stripe Dashboard > Products](https://dashboard.stripe.com/products)
2. Click **"Coupons"** in the left sidebar
3. Click **"Create coupon"**
4. Set up a test coupon (e.g., 20% off)
5. Go to **"Promotion codes"** 
6. Click **"Create promotion code"**
7. Link it to your coupon and set a code like `SAVE20`

## 🚀 Running the Application

```bash
uv run main.py
```

Visit: http://localhost:8000

## 🧪 Testing the Feature

1. **Open the test page**: Go to http://localhost:8000
2. **Click "Start Checkout"** 
3. **Look for the promotion code field** in the Stripe checkout
4. **Enter your test code** (e.g., `SAVE20`)
5. **Verify discount is applied** - pricing should update automatically
6. **Complete or cancel** the checkout to test callbacks

## 🔑 Key Implementation Detail

The magic happens in **ONE PARAMETER**:

```python
checkout_session = stripe.checkout.Session.create(
    # ... other parameters ...
    allow_promotion_codes=True,  # 🎉 THIS ENABLES PROMOTION CODES!
    # ... other parameters ...
)
```

## 📱 API Endpoints

- **GET /** - Test page with checkout button
- **POST /create-checkout-session** - Creates Stripe checkout with promo codes
- **GET /success** - Handles successful payments (shows discount info)
- **GET /cancel** - Handles cancelled payments
- **POST /webhook** - Your existing OMI webhook (unchanged)

## 🎯 Before vs After

### Before ❌
- No promotion code field in checkout
- Users cannot apply discounts
- All payments at full price

### After ✅  
- Promotion code input field appears
- Users can enter valid codes
- Discounts automatically applied
- Checkout reflects discounted pricing
- Success page shows discount details

## 🔍 Troubleshooting

**No promotion code field showing?**
- Ensure `allow_promotion_codes=True` is set
- Check that you have active promotion codes in Stripe Dashboard
- Verify you're using the correct Stripe keys

**Promotion codes not working?**
- Check the code is active in Stripe Dashboard
- Verify the coupon is properly linked
- Ensure the coupon applies to your product type (subscription vs one-time)

## 🎉 You're Done!

Your Stripe checkout now supports promotion codes with just that single parameter change: `allow_promotion_codes=True`!

