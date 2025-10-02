# 🚀 Quick Setup - Get Your Demo Running in 2 Minutes!

## The Issue You're Seeing

The "Error creating checkout session" happens because you need a **Stripe test API key**. Don't worry - this is super quick to fix!

## ⚡ Quick Fix (2 minutes)

### Step 1: Get Your FREE Stripe Test Key
1. **Go to**: [https://dashboard.stripe.com/register](https://dashboard.stripe.com/register)
2. **Sign up** for a free Stripe account (no credit card needed!)
3. **Go to**: [https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys) 
4. **Copy** your **"Secret key"** (starts with `sk_test_`)

### Step 2: Set the Key
**Windows PowerShell:**
```powershell
$env:STRIPE_SECRET_KEY="sk_test_your_actual_key_here"
uv run main.py
```

**Windows CMD:**
```cmd
set STRIPE_SECRET_KEY=sk_test_your_actual_key_here
uv run main.py
```

**Mac/Linux:**
```bash
export STRIPE_SECRET_KEY=sk_test_your_actual_key_here
uv run main.py
```

### Step 3: Test It! 🎉
1. **Visit**: `http://localhost:8000`
2. **Click**: "Order Now (Try Promotion Codes!)"
3. **See**: Real Stripe checkout with promotion code field!

## 🎯 Demo Mode (Current Behavior)

Right now, the demo runs in **"Demo Mode"** which shows:
- ✅ The OMI-styled interface
- ✅ The before/after comparison
- ✅ How the feature would look
- ❌ But can't open real Stripe checkout (needs API key)

## 🔥 With Real Stripe Key

Once you add the key, you get:
- ✅ Everything above PLUS
- ✅ Real Stripe checkout opens
- ✅ Actual promotion code field
- ✅ Live discount testing
- ✅ Complete end-to-end demo

## 💡 Alternative: Just Review the Code

If you want to skip Stripe setup and just review the implementation:

1. **Check line 353** in `main.py` - that's where `allow_promotion_codes=True` enables the feature
2. **Visit** `http://localhost:8000/api/implementation-guide` for technical details
3. **The demo interface** shows exactly how it would look in OMI

## 🎉 That's It!

The promotion codes feature is **literally one line of code**: `allow_promotion_codes=True`

Your demo is ready to show OMI how simple and powerful this feature is! 🚀

