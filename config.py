import os
from dataclasses import dataclass

@dataclass
class Settings:
    rpc_url: str = os.getenv("WEMIX_RPC_URL", "")
    db_path: str = os.getenv("DB_PATH", "data.sqlite")


def get_settings() -> Settings:
    return Settings()
