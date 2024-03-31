import requests
import csv
import os

# Google Maps Static API endpoint
MAPS_STATIC_API_URL = "https://maps.googleapis.com/maps/api/staticmap"

# Your Google Maps API key
API_KEY = "AIzaSyCf6fSrmV5D0tlC6g5aemWiK8qpw-lKDps"

# Directory to store generated images
OUTPUT_DIRECTORY = "test3"

START_ROW = 7584

def generate_static_map(location_name):
    params = {
        "center": "location_name",
        "zoom": 15,
        "size": "400x400",
        "markers": f"{location_name}|label:Hospital",
        "key": API_KEY
    }

    response = requests.get(MAPS_STATIC_API_URL, params=params)

    if response.status_code == 200:
        return response.content
    else:
        print(f"Error generating static map: {response.status_code}")
        return None


def main():
    # Create the output directory if it doesn't exist
    if not os.path.exists(OUTPUT_DIRECTORY):
        os.makedirs(OUTPUT_DIRECTORY)

    # Read CSV file
    with open('us_hospital_locations.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for _ in range(START_ROW):
            next(reader)  # Skip rows until START_ROW is reached
        for row in reader:
            if len(row) >= 5:
                hospital_name = row[4]
                filename = f"{hospital_name}_map.png"
                filepath = os.path.join(OUTPUT_DIRECTORY, filename)
                # Generate static map
                image_data = generate_static_map(hospital_name)

                # Save image to file
                if image_data:
                    with open(filepath, 'wb') as f:
                        f.write(image_data)
                    print(f"Image saved: {filename}")
                else:
                    print(f"Failed to save image: {filename}")
if __name__ == "__main__":
    main()
