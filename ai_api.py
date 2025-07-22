from fastapi import FastAPI, Request
from pydantic import BaseModel
from transformers import pipeline
import uvicorn

app = FastAPI()

# Load a small model for demonstration (distilgpt2)
generator = pipeline('text-generation', model='distilgpt2')

class GenerationRequest(BaseModel):
    prompt: str
    max_length: int = 50
    num_return_sequences: int = 1

@app.post('/generate')
def generate_text(request: GenerationRequest):
    results = generator(
        request.prompt,
        max_length=request.max_length,
        num_return_sequences=request.num_return_sequences
    )
    return {"results": [r['generated_text'] for r in results]}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)