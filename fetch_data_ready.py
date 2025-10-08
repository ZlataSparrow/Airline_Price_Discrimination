import gdown
import os

os.makedirs("data", exist_ok=True)

file_id = "1Dp6wkFBORO3D4W2sy5fQsTktVDChlRuH"
url = f"https://drive.google.com/uc?id={file_id}"

output_path = "data/Airlines_ticket_data_ready.pkl"

gdown.download(url, output_path, quiet=False)