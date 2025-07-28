# CDMA Implementation using Walsh Codes

A Python implementation of Code Division Multiple Access (CDMA) communication system using Walsh codes for orthogonal signal separation.

## Overview

This project demonstrates how CDMA technology works by implementing a simulation where multiple stations can transmit data simultaneously over the same channel. The system uses Walsh codes (Hadamard codes) to ensure orthogonal separation between different transmitters, allowing for interference-free communication.

## Features

- **Walsh Code Generation**: Generates orthogonal Walsh codes of order 3 (8x8 matrix)
- **Multi-Station Transmission**: Supports 8 simultaneous transmitters
- **Signal Encoding**: Encodes data bits using station-specific Walsh codes
- **Channel Simulation**: Combines all signals into a single resultant channel
- **Signal Decoding**: Recovers original data from any specific station
- **Interactive Interface**: User-friendly input system for data bits and station selection

## How It Works

1. **Walsh Code Generation**: Creates an 8x8 Walsh matrix using recursive Hadamard construction
2. **Data Input**: Each of the 8 stations inputs a data bit (0 or 1)
3. **Signal Encoding**: Each station's data bit is multiplied by its unique Walsh code
4. **Channel Combination**: All encoded signals are summed to create the resultant channel
5. **Station Selection**: User selects which station to decode
6. **Signal Decoding**: Uses inner product with the selected station's Walsh code to recover the original data

## Files

- `main.py`: Main implementation containing Walsh code generation and CDMA simulation
- `logo_CDMA.py`: ASCII art logo for the application
- `README.md`: This documentation file

## Requirements

- Python 3.x
- NumPy

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Navid-Rahman/CDMA-Implementation.git
cd CDMA-Implementation
```

2. Install required dependencies:

```bash
pip install numpy
```

## Usage

Run the main program:

```bash
python main.py
```

Follow the interactive prompts:

1. Enter data bits (0 or 1) for each of the 8 stations
2. Select which station you want to decode (1-8)
3. The program will display the recovered data bit

## Example

```
Enter D1 for Station 1: 1
Enter D2 for Station 2: 0
Enter D3 for Station 3: 1
...
Enter  the station to listen for C1=1 ,C2=2, C3=3, C4=4, C5=5, C6=6, C7=7, C8=8 : 1
Data bit that was sent: 1.0
```

## Mathematical Background

Walsh codes are binary sequences that are mutually orthogonal, meaning their inner product is zero. This orthogonality property ensures that:

- Multiple signals can be transmitted simultaneously without interference
- Each signal can be perfectly recovered using its corresponding Walsh code
- The system is robust against noise and interference

## License

This project is open source and available under the MIT License.

## Author

Navid Rahman

## Contributing

Feel free to fork this project and submit pull requests for any improvements!
