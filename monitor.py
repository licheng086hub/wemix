from web3 import Web3
import os
import time

class WemixMonitor:
    def __init__(self, rpc_url: str):
        self.w3 = Web3(Web3.WebsocketProvider(rpc_url))
        if not self.w3.isConnected():
            raise ConnectionError(f"Failed to connect to WEMIX node at {rpc_url}")

    def analyze_block(self, block):
        tx_count = len(block['transactions'])
        print(f"New block {block['number']} with {tx_count} txs")
        # TODO: implement additional analysis

    def run(self):
        block_filter = self.w3.eth.filter('latest')
        print("Listening for new blocks...")
        while True:
            for block_hash in block_filter.get_new_entries():
                block = self.w3.eth.get_block(block_hash, full_transactions=False)
                self.analyze_block(block)
            time.sleep(1)


def main():
    rpc_url = os.environ.get('WEMIX_RPC_URL')
    if not rpc_url:
        raise SystemExit('Environment variable WEMIX_RPC_URL is not set')
    monitor = WemixMonitor(rpc_url)
    monitor.run()


if __name__ == '__main__':
    main()
