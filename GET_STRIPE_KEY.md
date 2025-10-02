# 🔑 Get Your FREE Stripe Test Key (2 minutes)

## Why You Need This

To see the **real Stripe checkout** with promotion codes (not just the demo), you need a free Stripe test key. This is completely free and takes 2 minutes.

## ⚡ Quick Setup

### Step 1: Create Free Stripe Account
1. **Go to**: [https://dashboard.stripe.com/register](https://dashboard.stripe.com/register)
2. **Sign up** with your email (no credit card required!)
3. **Verify** your email address

### Step 2: Get Your Test Key
1. **Go to**: [https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)
2. **Copy** your **"Secret key"** (starts with `sk_test_`)
3. **Keep this page open** - you'll need it in a moment

### Step 3: Set the Key
**Windows PowerShell:**
```powershell
$env:STRIPE_SECRET_KEY="sk_test_your_actual_key_here"
$env:DEMO_MODE="false"
uv run main.py
```

**Windows CMD:**
```cmd
set STRIPE_SECRET_KEY=sk_test_your_actual_key_here
set DEMO_MODE=false
uv run main.py
```

**Mac/Linux:**
```bash
export STRIPE_SECRET_KEY=sk_test_your_actual_key_here
export DEMO_MODE=false
uv run main.py
```

### Step 4: Test It! 🎉
1. **Visit**: `http://localhost:8000`
2. **Click**: "Test WITH Promotion Codes"
3. **See**: Real Stripe checkout opens in new tab
4. **Look for**: "Promotion code" link in the checkout
5. **Try**: Enter any test code to see the field

## 🎯 What You'll See

### With Promotion Codes (allow_promotion_codes=True):
- ✅ "Promotion code" link appears in Stripe checkout
- ✅ Users can enter discount codes
- ✅ Prices update automatically

### Without Promotion Codes (allow_promotion_codes=False):
- ❌ No "Promotion code" link
- ❌ Users cannot enter codes
- ❌ No discount functionality

## 🔄 Toggle Testing

Use the buttons on the demo page:
- **"Test WITH Promotion Codes"** → Shows Stripe checkout WITH promotion code field
- **"Test WITHOUT Promotion Codes"** → Shows Stripe checkout WITHOUT promotion code field

## 💡 The Magic

The difference is literally **one parameter**:
```python
allow_promotion_codes=True   # Shows promotion code field
allow_promotion_codes=False  # Hides promotion code field
```

## 🎉 That's It!

Once you have the Stripe key set up, you can:
1. **See real Stripe checkout** (not demo)
2. **Test promotion codes** with actual Stripe interface
3. **Toggle on/off** to see the difference
4. **Show OMI** exactly how the feature works

**This is exactly what OMI needs to implement!** 🚀
