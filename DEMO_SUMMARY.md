# 🎯 OMI Promotion Codes Demo - Clean & Simple

## 🚀 What You Have Now

A **focused demo** that shows exactly how promotion codes work in OMI's checkout, with the ability to toggle them on/off.

## 📱 Demo Pages

### **Main Demo** - `http://localhost:8000`
- **Automatically redirects** to `/demo-checkout?promos=1`
- **Shows checkout** with promotion codes enabled by default

### **Demo Checkout** - `http://localhost:8000/demo-checkout`
- **With Promotion Codes**: `?promos=1` (shows promotion code field)
- **Without Promotion Codes**: `?promos=0` (hides promotion code field)

## 🎛️ Test Controls

On the demo checkout page, you have two buttons:

1. **✅ Test WITH Promotion Codes** → Shows the promotion code field
2. **❌ Test WITHOUT Promotion Codes** → Hides the promotion code field

## 🎯 How to Test

### **Step 1: Start the Server**
```bash
uv run main.py
```

### **Step 2: Visit the Demo**
- **Go to**: `http://localhost:8000`
- **You'll see**: Stripe-style checkout page

### **Step 3: Test Promotion Codes**
- **Click "Add promotion code"** → Enter "SAVE20"
- **Watch**: Price drops from $69.99 to $55.99
- **Click "Test WITHOUT Promotion Codes"** → Promotion field disappears
- **Click "Test WITH Promotion Codes"** → Promotion field reappears

## 🔧 The Implementation

The key is in **one parameter**:

```python
# In create_checkout_session function
allow_promotion_codes=allow_promos  # True or False
```

**When `True`**: Promotion code field appears in Stripe checkout
**When `False`**: No promotion code field

## 🎉 What This Shows OMI

1. **Visual Difference**: Clear before/after comparison
2. **Easy Implementation**: Just one parameter change
3. **User Experience**: How customers would interact with promotion codes
4. **Toggle Testing**: Can switch between enabled/disabled instantly

## 🚀 Ready for OMI Review

This demo is **clean, focused, and ready** for OMI to review. It shows exactly how the promotion codes feature would work in their actual checkout system.

**The implementation is literally one line of code!** 🎯
