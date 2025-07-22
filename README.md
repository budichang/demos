# Simple AI API

This is a simple AI API built with FastAPI and Hugging Face Transformers. It exposes a `/generate` endpoint for text generation using a small language model.

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the API:**
   ```bash
   python ai_api.py
   ```

The API will be available at `http://localhost:8000`.

## Usage

Send a POST request to `/generate` with a JSON body:

```
POST /generate
Content-Type: application/json

{
  "prompt": "Once upon a time,",
  "max_length": 50,
  "num_return_sequences": 1
}
```

**Response:**
```
{
  "results": [
    "Once upon a time, ..."
  ]
}
```

You can test the API using [httpie](https://httpie.io/) or `curl`:

```
curl -X POST http://localhost:8000/generate \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Hello, AI!", "max_length": 30}'
```