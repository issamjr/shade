# shade
Camera Hacking By link
# Camera Capture Penetration Testing Tool

This tool is designed for ethical penetration testing purposes. It captures images from a device's camera when a specific link is opened by the target. The captured images are then stored locally on the machine.

## Features
- Runs a simple HTTP server using **Python**.
- When a victim opens the generated link, a hidden JavaScript script attempts to access the device's camera and capture an image.
- The image is then converted into a `Base64` string and sent to the server.
- The server decodes the image and stores it locally in the `captured_images` directory.

## How It Works
1. When the script is executed, it starts a local server on `127.0.0.1:8002`.
2. The server generates a unique URL that the target needs to open.
3. Upon opening the link, the browser loads a hidden script that tries to access the device’s camera.
4. Once the camera access is granted, the script captures an image.
5. The image is encoded in `Base64` and sent to the server via a `POST` request to the `/api` endpoint.
6. The server decodes the image and saves it in the `captured_images` folder.

## Prerequisites
Before running the tool, make sure that you have the following:

- **Python 3.x** installed on your system. If not, you can download it from [here](https://www.python.org/downloads/).
- **pip** installed to handle Python dependencies.

## Installation

### 1. Clone or Download the Repository
Clone or download the repository to your local machine:

```bash
git clone [<repository_url>](https://github.com/issamjr/shade)
cd shade
pip install -r requirements.txt
python3 shade.py # or python3 shade.py -h
```

