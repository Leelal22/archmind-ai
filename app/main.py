from fastapi import FastAPI

app = FastAPI(
    title="ArchMind AI",
    description="AI Native Software Architecture Generator",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {
        "message": "Welcome to ArchMind AI 🚀"
    }