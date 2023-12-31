from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from configs.config_manager import ConfigManager

app = FastAPI()
# Add CORS middleware to allow requests from all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to the specific origins you want to allow
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def hello():
    return "hello"

# Updated endpoint to automatically generate schema
@app.get("/schema/")
async def generate_schema():
    schema = ConfigManager.get_json_schema()
    return JSONResponse(content=schema)
    # return JSONResponse(content=json.dumps(schema))

