import requests
import pandas as pd
from datetime import datetime
import time
from IPython.display import display, HTML

# API Configuration
BASE_URL = "https://api.hypurrscan.io"
RATE_LIMIT_DELAY = 0.1  # 100ms between requests to stay under 1000/min limit

print("✓ All imports successful!")
print(f"  - requests version: {requests.__version__}")
print(f"  - pandas version: {pd.__version__}")
print(f"  - IPython available")
print(f"\nAPI Configuration:")
print(f"  - Base URL: {BASE_URL}")
print(f"  - Rate limit delay: {RATE_LIMIT_DELAY}s")
