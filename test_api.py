import requests
import time

BASE_URL = "https://api.hypurrscan.io"

# Test API call
print("Testing API call to fetch stakedHYPE holders...")
try:
    response = requests.get(f"{BASE_URL}/holders/stakedHYPE")
    print(f"Status code: {response.status_code}")

    if response.status_code == 200:
        data = response.json()
        print(f"\nResponse keys: {data.keys()}")

        if 'addresses' in data:
            print(f"Number of holders: {len(data['addresses'])}")

            # Test with one of the whale addresses
            test_address = "0x39a3bbe71987f32e115dc807c1138b9a84f32795"
            if test_address in data['addresses']:
                balance = data['addresses'][test_address]
                balance_formatted = float(balance) / 1e18
                print(f"\nTest wallet {test_address[:10]}... has {balance_formatted:,.2f} stakedHYPE")
            else:
                print(f"\nTest wallet {test_address[:10]}... not found in holders")
                print(f"First 5 addresses: {list(data['addresses'].keys())[:5]}")
        else:
            print("'addresses' key not found in response")
            print(f"Response data: {data}")
    else:
        print(f"Error: {response.text}")

except Exception as e:
    print(f"Exception occurred: {e}")
