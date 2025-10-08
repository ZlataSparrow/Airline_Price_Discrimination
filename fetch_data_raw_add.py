import gdown
import os

# Make sure the "data" folder exists
os.makedirs("data", exist_ok=True)

# File ID from your Google Drive link
file_id = "19OxFD4GxhGUNs8DWY7XyOE0Ak3GVcuSt"
url = f"https://drive.google.com/uc?id={file_id}"

# Output path where the file will be saved
output_path = "data/Airports_data_raw_add.pkl"

# Download the file
gdown.download(url, output_path, quiet=False)

