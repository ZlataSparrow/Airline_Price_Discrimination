import gdown
import os

# Make sure the "data" folder exists
os.makedirs("data", exist_ok=True)

# File ID from your Google Drive link
file_id = "1Dp6wkFBORO3D4W2sy5fQsTktVDChlRuH"
url = f"https://drive.google.com/uc?id={file_id}"

# Output path where the file will be saved
output_path = "data/Airlines_tickets_data_ready.pkl"

# Download the file
gdown.download(url, output_path, quiet=False)