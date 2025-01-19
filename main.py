from typing import Optional

from fastapi import FastAPI
from gradio_client import Client

app = FastAPI()


@app.get("/")
async def root():
    client = Client("wasmdashai/RunTasking")
    result = client.predict(
    		text="السلام عليكم كيف الحال",
    		name_model="wasmdashai/vits-ar-sa-huba-v2",
    		speaking_rate=0.8,
    		api_name="/predict"
    )
    return {"message": result}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
