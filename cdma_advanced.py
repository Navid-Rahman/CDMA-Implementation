"""
Advanced CDMA Implementation with Additional Features
Author: Navid Rahman
Description: Enhanced CDMA simulation with visualization and analysis capabilities
"""

import numpy as np
import matplotlib.pyplot as plt
from logo_CDMA import logo


class AdvancedCDMASystem:
    """
    An advanced CDMA communication system with visualization and analysis features.
    """
    
    def __init__(self, order=3):
        """
        Initialize the advanced CDMA system.
        
        Args:
            order (int): Order of Walsh codes
        """
        self.order = order
        self.num_stations = 2 ** order
        self.walsh_matrix = self.generate_walsh_codes(order)
        
    def generate_walsh_codes(self, order):
        """Generate Walsh codes using efficient Hadamard construction."""
        W = np.array([[1]])
        for i in range(order):
            W = np.block([[W, W], [W, -W]])
        return W
    
    def visualize_walsh_codes(self):
        """Visualize the Walsh code matrix."""
        try:
            fig, ax = plt.subplots(figsize=(10, 8))
            im = ax.imshow(self.walsh_matrix, cmap='RdBu', aspect='equal')
            ax.set_title('Walsh Code Matrix Visualization')
            ax.set_xlabel('Chip Index')
            ax.set_ylabel('Station Index')
            
            # Add text annotations
            for i in range(self.num_stations):
                for j in range(self.num_stations):
                    text = ax.text(j, i, f'{self.walsh_matrix[i, j]:+d}',
                                 ha="center", va="center", color="black", fontweight='bold')
            
            plt.colorbar(im)
            plt.tight_layout()
            plt.show()
        except ImportError:
            print("Matplotlib not available. Install it with: pip install matplotlib")
    
    def check_orthogonality(self):
        """Check and display orthogonality properties of Walsh codes."""
        print("\nOrthogonality Check:")
        print("-" * 40)
        
        # Check auto-correlation
        for i in range(self.num_stations):
            auto_corr = np.dot(self.walsh_matrix[i], self.walsh_matrix[i])
            print(f"Station {i+1} auto-correlation: {auto_corr}")
        
        print("\nCross-correlation matrix (should be zero for i≠j):")
        cross_corr_matrix = np.zeros((self.num_stations, self.num_stations))
        for i in range(self.num_stations):
            for j in range(self.num_stations):
                cross_corr_matrix[i, j] = np.dot(self.walsh_matrix[i], self.walsh_matrix[j])
        
        print(cross_corr_matrix)
        
    def simulate_noise_effect(self, combined_signal, noise_power=0.1):
        """
        Simulate the effect of noise on the combined signal.
        
        Args:
            combined_signal (numpy.ndarray): Original combined signal
            noise_power (float): Power of the noise to add
            
        Returns:
            numpy.ndarray: Noisy signal
        """
        noise = np.random.normal(0, noise_power, len(combined_signal))
        return combined_signal + noise
    
    def batch_decode_all_stations(self, combined_signal):
        """
        Decode signals for all stations simultaneously.
        
        Args:
            combined_signal (numpy.ndarray): Combined channel signal
            
        Returns:
            list: Decoded bits for all stations
        """
        decoded_bits = []
        for i in range(self.num_stations):
            station_code = self.walsh_matrix[i]
            inner_product = combined_signal * station_code
            decoded_bit = np.sum(inner_product) / len(inner_product)
            decoded_bits.append(decoded_bit)
        return decoded_bits
    
    def run_advanced_simulation(self, include_noise=False, visualize=False):
        """
        Run the advanced CDMA simulation with additional features.
        
        Args:
            include_noise (bool): Whether to include noise simulation
            visualize (bool): Whether to show visualizations
        """
        print(logo)
        print("=" * 60)
        print("Advanced CDMA System Simulation")
        print("=" * 60)
        
        if visualize:
            self.visualize_walsh_codes()
        
        # Check orthogonality
        self.check_orthogonality()
        
        # Get random data for demonstration
        print(f"\nGenerating random data for {self.num_stations} stations...")
        data_bits = np.random.randint(0, 2, self.num_stations)
        print(f"Generated data bits: {data_bits}")
        
        # Encode signals
        encoded_signals = []
        for i, bit in enumerate(data_bits):
            encoded_signal = self.walsh_matrix[i] * bit
            encoded_signals.append(encoded_signal)
        
        # Combine signals
        combined_signal = np.sum(encoded_signals, axis=0)
        print(f"Combined channel signal: {combined_signal}")
        
        # Add noise if requested
        if include_noise:
            noisy_signal = self.simulate_noise_effect(combined_signal, 0.1)
            print(f"Noisy signal: {noisy_signal}")
            decode_signal = noisy_signal
        else:
            decode_signal = combined_signal
        
        # Decode all stations
        decoded_bits = self.batch_decode_all_stations(decode_signal)
        
        # Display results
        print(f"\nDecoding Results:")
        print("-" * 40)
        print(f"{'Station':<10} {'Original':<10} {'Decoded':<10} {'Error':<10}")
        print("-" * 40)
        
        total_errors = 0
        for i in range(self.num_stations):
            error = abs(decoded_bits[i] - data_bits[i])
            if error > 0.1:  # Threshold for bit error
                total_errors += 1
                status = "ERROR"
            else:
                status = "OK"
            
            print(f"{i+1:<10} {data_bits[i]:<10} {decoded_bits[i]:<10.3f} {status:<10}")
        
        print("-" * 40)
        print(f"Total bit errors: {total_errors}/{self.num_stations}")
        print(f"Bit Error Rate: {total_errors/self.num_stations:.2%}")


def main():
    """Main function with menu options."""
    print("CDMA System Options:")
    print("1. Basic CDMA Simulation")
    print("2. Advanced CDMA with Analysis")
    print("3. Advanced CDMA with Noise")
    print("4. Advanced CDMA with Visualization")
    
    try:
        choice = int(input("Select option (1-4): "))
        
        if choice == 1:
            from main import CDMASystem
            system = CDMASystem()
            system.run_simulation()
        elif choice == 2:
            system = AdvancedCDMASystem()
            system.run_advanced_simulation()
        elif choice == 3:
            system = AdvancedCDMASystem()
            system.run_advanced_simulation(include_noise=True)
        elif choice == 4:
            system = AdvancedCDMASystem()
            system.run_advanced_simulation(include_noise=True, visualize=True)
        else:
            print("Invalid choice!")
            
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
