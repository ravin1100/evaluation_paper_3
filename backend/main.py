from fastapi import FastAPI, HTTPException


app = FastAPI(description="SmartFit: AI-Powered Fitness Coach")


@app.post("/health")
def health_check():
    return {"success": True}
