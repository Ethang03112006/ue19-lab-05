import requests

def main():
    url = "https://v2.jokeapi.dev/joke/Any"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Erreur lors de la requête : {e}")
        return

    data = response.json()

    if data.get("type") == "single":
        print("💬 Joke:", data["joke"])
    else:
        print("💬 Setup:", data["setup"])
        print("🤣 Delivery:", data["delivery"])

if __name__ == "__main__":
    main()
