import gdown
import os

# Make sure the "data" folder exists
os.makedirs("data", exist_ok=True)

# File ID from your Google Drive link
file_id = "1EDGkpkMm99uf8acZWVSHzNXh9ZffSpd8"
url = f"https://drive.google.com/uc?id={file_id}"

# Output path where the file will be saved
output_path = "data/Airlines_tickets_data_EDA_ready.pkl"

# Download the file
gdown.download(url, output_path, quiet=False)
