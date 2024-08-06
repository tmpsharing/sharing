import requests

def save_url_content_as_http(url: str, filename: str):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Ensure we notice bad responses
        with open(filename, 'w') as file:
            file.write(response.text)
        print(f"Content saved to {filename}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve URL content: {e}")

if __name__ == "__main__":
    url = "https://chatgpt.com/share/150ac33a-4d3d-4b3b-93f8-9b1775424dcc"
    filename = "output.http"
    save_url_content_as_http(url, filename)
