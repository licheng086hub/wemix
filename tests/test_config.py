import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from config import get_settings


def test_default_settings(monkeypatch):
    monkeypatch.delenv("WEMIX_RPC_URL", raising=False)
    monkeypatch.delenv("DB_PATH", raising=False)
    settings = get_settings()
    assert settings.rpc_url == ""
    assert settings.db_path == "data.sqlite"
