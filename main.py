import asyncio
from deriv_api import DerivAPI

APP_ID = 33759          # Replace with your App ID
API_TOKEN = "18fcee7be475cc7c82c3099bc533c6a1284e0017751679933977a9ed8eb39702"  # Replace with your API token

async def get_my_balance():
    api = DerivAPI(app_id=APP_ID)

    await api.authorize(API_TOKEN)

    balance = await api.balance()
    print(balance)

asyncio.run(get_my_balance())


