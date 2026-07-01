import os
from b2sdk.v2 import InMemoryAccountInfo, B2Api

info = InMemoryAccountInfo()
b2_api = B2Api(info)

print("Trying login...")

b2_api.authorize_account(
    "production",
    os.environ["B2_KEY_ID"],
    os.environ["B2_APPLICATION_KEY"]
)

print("LOGIN SUCCESS ✔️")
