import requests
import os

def download_file(url, filename):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        return True
    return False

def main():
    # Sample video URL (a short video from Pexels)
    url = "https://www.pexels.com/download/video/855564/"
    filename = "samples/sample.mp4"
    
    os.makedirs("samples", exist_ok=True)
    print("Downloading sample video...")
    if download_file(url, filename):
        print(f"Successfully downloaded to {filename}")
    else:
        print("Failed to download video")

if __name__ == "__main__":
    main()
