from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Add CORS middleware to allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)


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
