# 🎉 OMI Promotion Codes Feature Demo

## 🚀 Live Demo Running at http://localhost:8000

This is a **complete OMI-styled demo** showing how promotion codes can be added to OMI's Stripe checkout with just **ONE line of code**.

## 📱 Demo Pages Available

### 1. **Main Demo Page** - `http://localhost:8000`
- OMI-branded homepage with your exact styling
- Before/After comparison showing the feature benefits
- Live "Order Now" button that opens Stripe checkout with promotion codes
- Real OMI Dev Kit 2 product ($69.99)

### 2. **API Documentation** - `http://localhost:8000/api/demo-info`
- JSON API showing technical implementation details
- Benefits and test instructions
- Perfect for your development team review

### 3. **Implementation Guide** - `http://localhost:8000/api/implementation-guide`
- Complete technical guide for your developers
- Code examples showing exactly what to change
- Step-by-step implementation instructions

## 🔧 How to Test the Demo

### Step 1: Start the Demo Server
```bash
# Install dependencies
uv sync

# Set your Stripe test keys (optional - demo works with defaults)
export STRIPE_SECRET_KEY="sk_test_your_key_here"

# Run the server
uv run main.py
```

### Step 2: Visit the Demo
1. **Open**: `http://localhost:8000`
2. **Click**: "🛒 Order Now (Try Promotion Codes!)" button
3. **Look for**: "Promotion code" link in the Stripe checkout
4. **Test**: Enter promotion codes (create them in Stripe Dashboard first)

### Step 3: See the Magic ✨
- Promotion code field appears automatically
- Discounts apply in real-time
- No additional UI development needed
- Secure validation by Stripe

## 🎯 The Implementation (Just ONE Line!)

### Current OMI Code:
```python
checkout_session = stripe.checkout.Session.create(
    payment_method_types=['card'],
    line_items=[...],
    mode='payment',
    success_url='...',
    cancel_url='...'
    # Missing promotion codes!
)
```

### Enhanced OMI Code:
```python
checkout_session = stripe.checkout.Session.create(
    payment_method_types=['card'],
    line_items=[...],
    mode='payment',
    allow_promotion_codes=True,  # 🎉 ADD THIS SINGLE LINE!
    success_url='...',
    cancel_url='...'
)
```

## 💡 Benefits for OMI

### 🎯 **Marketing Power**
- Run discount campaigns for OMI Dev Kit 2
- Early bird pricing for new products
- Influencer discount codes
- Holiday and seasonal promotions

### 📈 **Business Impact**
- **Reduce cart abandonment** - customers love discounts
- **Increase conversion rates** - promotional pricing drives sales
- **Customer acquisition** - discount codes attract new users
- **Marketing attribution** - track which campaigns work

### ⚡ **Technical Benefits**
- **Zero UI development** - Stripe handles everything
- **Secure by default** - Stripe validates codes
- **Mobile optimized** - works perfectly on all devices
- **Maintenance-free** - no additional code to maintain

## 🧪 Demo Features Implemented

✅ **OMI-branded styling** matching your website  
✅ **Real product info** - OMI Dev Kit 2 at $69.99  
✅ **Before/After comparison** showing the improvement  
✅ **Live Stripe checkout** with promotion codes enabled  
✅ **Success/cancel handling** with discount details  
✅ **API documentation** for your development team  
✅ **Implementation guide** with code examples  

## 📋 Next Steps for OMI

### Option 1: Quick Implementation
1. **Find your Stripe checkout code** in OMI's backend
2. **Add `allow_promotion_codes=True`** parameter
3. **Create promotion codes** in your Stripe Dashboard
4. **Test and deploy** - it's that simple!

### Option 2: Review & Collaborate
1. **Review this demo** with your team
2. **Test the functionality** at `http://localhost:8000`
3. **Discuss implementation** using our technical guide
4. **We can help integrate** into your actual OMI platform

## 🔗 Demo URLs Summary

- **Main Demo**: `http://localhost:8000`
- **API Info**: `http://localhost:8000/api/demo-info`
- **Tech Guide**: `http://localhost:8000/api/implementation-guide`
- **Success Page**: `http://localhost:8000/success` (after checkout)
- **Cancel Page**: `http://localhost:8000/cancel`

## 🎉 Ready to Boost OMI Sales?

This feature can be implemented in **under 30 minutes** and will immediately enable:
- Discount marketing campaigns
- Better conversion rates  
- Enhanced user experience
- Competitive advantage

**The demo is live and ready for your review!** 🚀

---

*Built with ❤️ for the OMI team - showing how one line of code can unlock powerful marketing capabilities.*
