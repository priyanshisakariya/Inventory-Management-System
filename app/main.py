from fastapi import FastAPI
from app.routes.product import router
app = FastAPI()

# Register all product routes
app.include_router(router)

@app.get("/")
def home():
            return {
                    "message": "Inventory Management API"
            }
    