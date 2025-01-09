import json
import os

# Define weights for inbound and outbound MOS scores
INBOUND_WEIGHT = 0.6  # Adjust as needed
OUTBOUND_WEIGHT = 0.4  # Adjust as needed

def calculate_call_quality_score(file_path):
    try:
        # Check if the file exists
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        # Load the JSON data from the file
        with open(file_path, "r") as file:
            data = json.load(file)

        # Extract MOS scores
        inbound_mos_avg = data["detail"]["webRTCSession"]["metrics"]["inbound"]["mos"]["avg"]
        outbound_mos_avg = data["detail"]["webRTCSession"]["metrics"]["outbound"]["mos"]["avg"]

        # Calculate weighted average
        call_quality_score = (inbound_mos_avg * INBOUND_WEIGHT) + (outbound_mos_avg * OUTBOUND_WEIGHT)

        # Print the result
        print(f"Call Quality Score: {call_quality_score:.2f}")

    except FileNotFoundError as e:
        print(e)
    except json.JSONDecodeError as e:
        print(f"Error reading JSON file: {e}")
    except KeyError as e:
        print(f"Missing key in JSON data: {e}")

# Path to the input JSON file
file_path = "operata_event.json"

# Calculate and print the Call Quality Score
calculate_call_quality_score(file_path)
