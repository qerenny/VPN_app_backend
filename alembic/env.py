from logging.config import fileConfig
from sqlalchemy import create_engine, pool
from alembic import context
from sqlmodel import SQLModel
from vpn_backend.configs.env import get_environment_variables
from sqlalchemy.engine.url import make_url
from vpn_backend.models.user import User
from vpn_backend.models.subscription import Subscription
from vpn_backend.models.vpn_key import VPNKey
from vpn_backend.models.vpn_session import VPNSession
from vpn_backend.models.payment import Payment
from vpn_backend.models.notification import Notification
from vpn_backend.models.user_settings import UserSettings
from vpn_backend.models.route_profile import RouteProfile
from vpn_backend.models.route_rule import RouteRule

env = get_environment_variables()

db_url = make_url(env.DATABASE_URL)
sync_url = str(db_url.set(drivername="postgresql+psycopg2"))

config = context.config
fileConfig(config.config_file_name)
config.set_main_option("sqlalchemy.url", sync_url)

target_metadata = SQLModel.metadata


def run_migrations_offline():
    context.configure(
        url=sync_url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    connectable = create_engine(
        sync_url,
        poolclass=pool.NullPool,
        future=True,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
            compare_server_default=True,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
