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

- `main.py`: Improved main implementation with object-oriented design and input validation
- `cdma_advanced.py`: Advanced version with visualization, noise simulation, and analysis features
- `test_cdma.py`: Test suite to verify functionality and demonstrate improvements
- `logo_CDMA.py`: ASCII art logo for the application
- `requirements.txt`: Python package dependencies
- `README.md`: This documentation file

## Requirements

- Python 3.7+
- NumPy (for mathematical operations)
- Matplotlib (for advanced visualization features, optional)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Navid-Rahman/CDMA-Implementation.git
cd CDMA-Implementation
```

2. Install required dependencies:

```bash
pip install -r requirements.txt
```

Or install individually:

```bash
pip install numpy matplotlib
```

## Usage

### Basic CDMA Simulation

Run the improved main program:

```bash
python main.py
```

### Advanced Features

Run the advanced version with additional features:

```bash
python cdma_advanced.py
```

Choose from:

1. **Basic CDMA Simulation** - Interactive version with input validation
2. **Advanced Analysis** - Includes orthogonality checking and batch decoding
3. **Noise Simulation** - Tests system performance with channel noise
4. **Visualization Mode** - Visual representation of Walsh codes (requires matplotlib)

### Testing

Run the test suite to verify functionality:

```bash
python test_cdma.py
```

This will test:

- Walsh code generation and orthogonality
- Encoding and decoding processes
- Error handling capabilities

## Code Improvements

The codebase has been significantly improved with the following enhancements:

### Object-Oriented Design

- **Class-based architecture**: `CDMASystem` class encapsulates all CDMA functionality
- **Modular functions**: Each operation is separated into logical methods
- **Reusable code**: Easy to extend and modify for different configurations

### Input Validation & Error Handling

- **Robust input validation**: Ensures only valid data bits (0 or 1) are accepted
- **Error handling**: Graceful handling of invalid inputs and exceptions
- **User-friendly prompts**: Clear instructions and error messages

### Advanced Features (cdma_advanced.py)

- **Visualization**: Graphical representation of Walsh code matrix
- **Orthogonality analysis**: Mathematical verification of code properties
- **Noise simulation**: Testing system robustness against channel noise
- **Batch processing**: Simultaneous decoding of all stations
- **Performance metrics**: Bit Error Rate (BER) calculation

### Code Quality Improvements

- **Documentation**: Comprehensive docstrings and comments
- **Type hints**: Better code readability and IDE support
- **Clean structure**: Elimination of repetitive code
- **Efficient algorithms**: Optimized Walsh code generation
- **Professional formatting**: Following Python best practices

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
