from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from agents.GreetAgent import GreetingAgent

app = FastAPI()

# Allow CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins (for dev only)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize required agents

# Greet Agent
greetAgent = GreetingAgent()

@app.get("/greet")
def greet_user(name: str = "User"):
    message = greetAgent.greet(name)
    return {"message": message}