import os
import requests
from b2sdk.v2 import InMemoryAccountInfo, B2Api

url = os.environ["FILE_URL"]
bucket_name = os.environ["B2_BUCKET"]

info = InMemoryAccountInfo()
b2_api = B2Api(info)

b2_api.authorize_account(
    "production",
    os.environ["B2_KEY_ID"],
    os.environ["B2_APP_KEY"]
)

bucket = b2_api.get_bucket_by_name(bucket_name)

filename = url.split("/")[-1].split("?")[0]

print("Downloading file...")
r = requests.get(url, stream=True)
r.raise_for_status()

with open(filename, "wb") as f:
    for chunk in r.iter_content(chunk_size=8192):
        f.write(chunk)

print("Uploading to Backblaze...")
bucket.upload_local_file(
    local_file=filename,
    file_name=filename
)

print("Done:", filename)
