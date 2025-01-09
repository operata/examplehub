
# Call Quality Score Calculator

This repository provides a Python script to calculate the **Call Quality Score** based on the weighted average of inbound and outbound MOS (Mean Opinion Score) from a JSON input file.

## Features

- Reads call metrics from a JSON file
- Calculates Call Quality Score using customizable weights for inbound and outbound MOS
- Outputs the score in a user-friendly format

## Getting Started

### Prerequisites

- Python 3.6 or later
- Basic knowledge of Python and JSON

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/operata/examplehub.git
   ```

2. Navigate to the project directory:
   ```bash
   cd examplehub/callQualityScore
   ```

### Usage

1. Save your input data in a JSON file named `operata_event.json` in the root of the project directory.

   Example `operata_event.json`:
   ```json
   {
       "detail": {
           "webRTCSession": {
               "metrics": {
                   "inbound": {
                       "mos": {
                           "avg": 4.41
                       }
                   },
                   "outbound": {
                       "mos": {
                           "avg": 4.40
                       }
                   }
               }
           }
       }
   }
   ```

2. Open the `calculate_score.py` script and customize the weights if needed:
   ```python
   # Adjust weights as needed
   INBOUND_WEIGHT = 0.6
   OUTBOUND_WEIGHT = 0.4
   ```

3. Run the script:
   ```bash
   python calculate_score.py
   ```

4. View the output in the terminal:
   ```
   Call Quality Score: 4.41
   ```

### Customizing the Weights

You can adjust the `INBOUND_WEIGHT` and `OUTBOUND_WEIGHT` values in the `calculate_score.py` script to reflect the importance of inbound and outbound MOS in your calculations. The weights must add up to `1.0`.

### Example Calculation

For the provided example `input.json`:
- **Inbound MOS Avg:** `4.41`
- **Outbound MOS Avg:** `4.40`
- **Weights:** `INBOUND_WEIGHT = 0.6`, `OUTBOUND_WEIGHT = 0.4`

The **Call Quality Score** is calculated as:
```
Call Quality Score = (Inbound MOS Avg * Inbound Weight) + (Outbound MOS Avg * Outbound Weight)
Call Quality Score = (4.41 * 0.6) + (4.40 * 0.4)
Call Quality Score = 4.41
```

### Contributing

Contributions are welcome! Please fork this repository, make your changes, and submit a pull request.

### License

This project is licensed under the [MIT License](LICENSE).

---
