import json

# Define weights for inbound and outbound MOS scores
INBOUND_WEIGHT = 0.6  # Adjust as needed
OUTBOUND_WEIGHT = 0.4  # Adjust as needed

def calculate_call_quality_score(file_path):
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

# Path to the input JSON file
file_path = "operata_event.json"

# Calculate and print the Call Quality Score
calculate_call_quality_score(file_path)
