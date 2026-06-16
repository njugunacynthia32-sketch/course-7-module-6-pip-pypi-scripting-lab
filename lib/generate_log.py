from datetime import datetime
import requests


def fetch_data():
    """Fetch data from API"""
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

    if response.status_code == 200:
        return response.json()
    return {}


def write_log(log_data, filename):
    """Write log entries to a file"""
    with open(filename, "w") as file:
        for entry in log_data:
            file.write(f"{entry}\n")


def main():
    # Step 1: Log system actions
    log_data = [
        "User logged in",
        "User updated profile",
        "Report exported"
    ]

    filename = f"log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    write_log(log_data, filename)

    print(f"Log written to {filename}")

    # Step 2: Fetch API data
    post = fetch_data()
    print("Fetched Post Title:", post.get("title", "No title found"))


if __name__ == "__main__":
    main()