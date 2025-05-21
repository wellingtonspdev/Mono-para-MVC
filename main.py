from fastapi import FastAPI
from views.cep_routers import router  # se usou nome routers.py

app = FastAPI()
app.include_router(router)
