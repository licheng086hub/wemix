"""Monitor latest blocks on the WEMIX chain and store them in a database."""
import datetime
from web3 import Web3
from config import get_settings
from db import Block, get_engine, init_db, get_session


def main():
    settings = get_settings()
    if not settings.rpc_url:
        raise RuntimeError("WEMIX_RPC_URL is not configured")

    web3 = Web3(Web3.HTTPProvider(settings.rpc_url))
    engine = get_engine(settings.db_path)
    init_db(engine)
    session = get_session(engine)

    latest = web3.eth.get_block("latest")
    block = Block(
        number=latest.number,
        hash=latest.hash.hex(),
        timestamp=datetime.datetime.fromtimestamp(latest.timestamp),
    )
    exists = session.query(Block).filter_by(number=block.number).first()
    if not exists:
        session.add(block)
        session.commit()
    print(f"Saved block {block.number}")


if __name__ == "__main__":
    main()
