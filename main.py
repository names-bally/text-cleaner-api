from fastapi import FastAPI, Header, HTTPException

app = FastAPI()

# This is the "Secret Key" that RapidAPI will pass to your code
API_KEY = "my_super_secret_key_123"

@app.post("/clean-text")
def clean_text(raw_text: str, x_api_key: str = Header(...)):
    # Check if the key is correct
    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    
    # Process the text
    cleaned = " ".join(raw_text.split()).strip().title()
    return {"original": raw_text, "cleaned": cleaned}
