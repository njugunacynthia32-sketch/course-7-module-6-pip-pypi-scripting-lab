from datetime import datetime


def generate_log(log_data):
    if not isinstance(log_data, list):
        raise ValueError("Input must be a list")

    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"


    with open(filename, "w") as file:
        for item in log_data:
            file.write(f"{item}\n")

    return filename
    
