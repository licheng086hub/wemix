# Wemix Chain Monitoring Tool

A simple real-time monitoring utility for the Wemix blockchain. It connects to a Wemix node and prints basic block information as new blocks are produced.

## Requirements

- Python 3.8+
- `web3` library (install with `pip install -r requirements.txt`)

## Usage

1. Set the RPC endpoint for your Wemix node in the environment variable `WEMIX_RPC_URL`.
2. Run the monitor:

```bash
python monitor.py
```

The script will output a message whenever a new block appears. Extend `analyze_block` in `monitor.py` to implement custom analytics.


