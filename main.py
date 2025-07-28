"""
CDMA Implementation using Walsh Codes
Author: Navid Rahman
Description: A simulation of Code Division Multiple Access communication system
"""

import numpy as np
from logo_CDMA import logo


class CDMASystem:
    """
    A class to represent a CDMA communication system using Walsh codes.
    """
    
    def __init__(self, order=3):
        """
        Initialize the CDMA system with Walsh codes of given order.
        
        Args:
            order (int): Order of Walsh codes (default: 3 for 8x8 matrix)
        """
        self.order = order
        self.num_stations = 2 ** order
        self.walsh_matrix = self.generate_walsh_codes(order)
        
    def generate_walsh_codes(self, order):
        """
        Generate Walsh codes using Hadamard matrix construction.
        
        Args:
            order (int): Order of the Walsh matrix
            
        Returns:
            numpy.ndarray: Walsh code matrix
        """
        W = np.array([[1]])
        for i in range(order):
            W = np.block([[W, W], [W, -W]])
        return W
    
    def get_station_data(self):
        """
        Get data bits from all stations with input validation.
        
        Returns:
            list: List of data bits for each station
        """
        data_bits = []
        for i in range(self.num_stations):
            while True:
                try:
                    bit = int(input(f"Enter data bit for Station {i+1} (0 or 1): "))
                    if bit in [0, 1]:
                        data_bits.append(bit)
                        break
                    else:
                        print("Please enter only 0 or 1")
                except ValueError:
                    print("Please enter a valid integer (0 or 1)")
        return data_bits
    
    def encode_signals(self, data_bits):
        """
        Encode data bits using Walsh codes for each station.
        
        Args:
            data_bits (list): Data bits for each station
            
        Returns:
            list: Encoded signals for each station
        """
        encoded_signals = []
        for i, bit in enumerate(data_bits):
            encoded_signal = self.walsh_matrix[i] * bit
            encoded_signals.append(encoded_signal)
        return encoded_signals
    
    def combine_signals(self, encoded_signals):
        """
        Combine all encoded signals into a single channel.
        
        Args:
            encoded_signals (list): List of encoded signals
            
        Returns:
            numpy.ndarray: Combined channel signal
        """
        return np.sum(encoded_signals, axis=0)
    
    def select_station(self):
        """
        Get station selection from user with input validation.
        
        Returns:
            int: Selected station number (0-indexed)
        """
        while True:
            try:
                station = int(input(f"Select station to decode (1-{self.num_stations}): "))
                if 1 <= station <= self.num_stations:
                    return station - 1  # Convert to 0-indexed
                else:
                    print(f"Please enter a number between 1 and {self.num_stations}")
            except ValueError:
                print("Please enter a valid integer")
    
    def decode_signal(self, combined_signal, station_index):
        """
        Decode the signal for a specific station.
        
        Args:
            combined_signal (numpy.ndarray): Combined channel signal
            station_index (int): Index of station to decode (0-indexed)
            
        Returns:
            float: Decoded data bit
        """
        station_code = self.walsh_matrix[station_index]
        inner_product = combined_signal * station_code
        decoded_bit = np.sum(inner_product) / len(inner_product)
        return decoded_bit
    
    def run_simulation(self):
        """
        Run the complete CDMA simulation.
        """
        print(logo)
        print("=" * 50)
        print("CDMA System Simulation")
        print("=" * 50)
        
        # Display Walsh codes
        print(f"\nGenerated {self.num_stations}x{self.num_stations} Walsh Code Matrix:")
        print(self.walsh_matrix)
        print("\n" + "-" * 50)
        
        # Get data from all stations
        print(f"\nData Input Phase - Enter bits for {self.num_stations} stations:")
        data_bits = self.get_station_data()
        
        # Encode signals
        encoded_signals = self.encode_signals(data_bits)
        print(f"\nData bits: {data_bits}")
        
        # Combine signals
        combined_signal = self.combine_signals(encoded_signals)
        print(f"Combined channel signal: {combined_signal}")
        
        # Select station to decode
        print("\n" + "-" * 50)
        print("Decoding Phase:")
        station_index = self.select_station()
        
        # Decode signal
        decoded_bit = self.decode_signal(combined_signal, station_index)
        
        # Display results
        print(f"\nResults:")
        print(f"Selected Station: {station_index + 1}")
        print(f"Original data bit: {data_bits[station_index]}")
        print(f"Decoded data bit: {decoded_bit}")
        
        # Verify correctness
        if abs(decoded_bit - data_bits[station_index]) < 0.001:
            print("✓ Decoding successful!")
        else:
            print("✗ Decoding failed!")


def main():
    """
    Main function to run the CDMA simulation.
    """
    try:
        cdma_system = CDMASystem(order=3)
        cdma_system.run_simulation()
    except KeyboardInterrupt:
        print("\n\nSimulation interrupted by user.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")


if __name__ == "__main__":
    main()
