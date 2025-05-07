from fastapi import Depends, FastAPI

from vpn_backend.configs.env import get_environment_variables

# from models.BaseModel import init
from vpn_backend.routers.user_router import UserRouter

env = get_environment_variables()

app = FastAPI(
    title="VPN Backend API",
    version="1.0.0",
)

app.include_router(UserRouter)

# init()
