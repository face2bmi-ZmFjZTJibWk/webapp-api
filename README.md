# webapp-api
Code API for WebApp

---

## Setup

### Creating a virtual environment

On macOS and Linux:

`python3 -m venv env`

On Windows:

`py -m venv env`

### Activating a virtual environment

On macOS and Linux:

`source env/bin/activate`

On Windows:

`.\env\Scripts\activate`

### Leaving the virtual environment

`deactivate`

### Installing Dependencies

`pip install -r requirements.txt`

---

## Run

### Dev

`uvicorn app:app --reload`

### Prod

`uvicorn app:app --host=0.0.0.0 --port=${PORT:-5000}`
