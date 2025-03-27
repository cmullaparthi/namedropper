from fastapi import FastAPI
from pydantic import BaseModel
from name_extraction_pipeline.dispatcher import extract_first_name

app = FastAPI()

class NameRequest(BaseModel):
    full_name: str

@app.post("/extract_first_name")
def extract(req: NameRequest):
    return extract_first_name(req.full_name)
