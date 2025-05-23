from fastapi import Depends, FastAPI

from vpn_backend.configs.database.engine import async_init_db
from vpn_backend.routers.user_router import UserRouter
from vpn_backend.routers.subscription_router import SubscriptionRouter
from vpn_backend.routers.route_profile_router import RouteProfileRouter
from vpn_backend.routers.route_rule_router import RouteRuleRouter
from vpn_backend.routers.notification_router import NotificationRouter
from vpn_backend.routers.payment_router import PaymentRouter
from vpn_backend.routers.user_settings_router import UserSettingsRouter
from vpn_backend.routers.vpn_key_router import VPNKeyRouter
from vpn_backend.routers.vpn_session_router import VPNSessionRouter
from vpn_backend.configs.env import get_environment_variables

env = get_environment_variables()

app = FastAPI(
    title="VPN Backend API",
    version="1.0.0",
)

app.include_router(UserRouter)
app.include_router(SubscriptionRouter)
app.include_router(RouteProfileRouter)
app.include_router(RouteRuleRouter)
app.include_router(NotificationRouter)
app.include_router(PaymentRouter)
app.include_router(UserSettingsRouter)
app.include_router(VPNKeyRouter)
app.include_router(VPNSessionRouter)

@app.on_event("startup")
async def on_startup():
    await async_init_db()