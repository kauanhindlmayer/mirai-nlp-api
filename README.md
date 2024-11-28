# Mirai Embedding API

This project is a FastAPI-based application that generates text embeddings using a pre-trained language model.

## Getting Started

To get started, clone this repository to your local machine.

## Installing

1. **Create a virtual environment:**

```bash
python -m venv venv
```

2. Activate the virtual environment:

```bash
source venv/bin/activate
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

4. Set the environment variables:

Copy the .env.example file to .env:

```bash
cp .env.example .env
```

Then, update the .env file with your own values, such as the API key.

## Running the Application

To run the application, execute the following command:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```
