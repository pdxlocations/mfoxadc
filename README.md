This library provides UDP-based broadcasting of Meshtastic-compatible packets.

# Installation

```bash
pip install mudp --no-deps
pip install mfoxadc
```
# Wiring

Connect your power source through a voltage divider to GPIO4_C1/SARADC_IN1. Pin 21 on Pico Mini, Pin 32 on Pico Pro/Max
**There is a 1.8v max voltage on this pin.**


# Command Line

```bash
mfoxadc --node-id '!abcd1234'
```

# Additional Arguments:
```bash
  -h, --help           show this help message and exit
  --node-id NODE_ID    Node ID (e.g., !596ab32e)
  --channel CHANNEL    Channel name, default is LongFast
  --key KEY            Encryption key (Base64), default is AQ==
  --interval INTERVAL  Time between reports in seconds, default is 1800
```
