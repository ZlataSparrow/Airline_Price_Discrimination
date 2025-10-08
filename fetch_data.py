import gdown
import os

os.makedirs("data", exist_ok=True)

# Google Drive file ID (from your shared link)
file_id = "1JZBrVIJ3dtp7gw4dnpz_SNyEY3p2v4k0"
url = f"https://drive.google.com/uc?id={file_id}"

# Download the file
gdown.download(url, "data/Airline_tickets_data.pkl", quiet=False)