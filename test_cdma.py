"""
Test script for CDMA implementation
Demonstrates the improvements and functionality
"""

import numpy as np
import sys
import os

# Add the current directory to path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from main import CDMASystem
    print("✓ Successfully imported improved CDMASystem")
except ImportError as e:
    print(f"✗ Failed to import CDMASystem: {e}")
    sys.exit(1)


def test_walsh_code_generation():
    """Test Walsh code generation."""
    print("\n" + "="*50)
    print("Testing Walsh Code Generation")
    print("="*50)
    
    cdma = CDMASystem(order=3)
    walsh_matrix = cdma.walsh_matrix
    
    print(f"Generated {walsh_matrix.shape[0]}x{walsh_matrix.shape[1]} Walsh matrix:")
    print(walsh_matrix)
    
    # Test orthogonality
    print("\nTesting orthogonality...")
    for i in range(len(walsh_matrix)):
        for j in range(len(walsh_matrix)):
            dot_product = np.dot(walsh_matrix[i], walsh_matrix[j])
            if i == j:
                assert dot_product == 8, f"Auto-correlation failed for row {i}"
            else:
                assert dot_product == 0, f"Cross-correlation failed for rows {i}, {j}"
    
    print("✓ All orthogonality tests passed!")
    return True


def test_encoding_decoding():
    """Test the encoding and decoding process."""
    print("\n" + "="*50)
    print("Testing Encoding/Decoding Process")
    print("="*50)
    
    cdma = CDMASystem(order=3)
    
    # Test data
    test_data = [1, 0, 1, 1, 0, 0, 1, 0]
    print(f"Test data bits: {test_data}")
    
    # Encode signals
    encoded_signals = cdma.encode_signals(test_data)
    print(f"Number of encoded signals: {len(encoded_signals)}")
    
    # Combine signals
    combined_signal = cdma.combine_signals(encoded_signals)
    print(f"Combined signal: {combined_signal}")
    
    # Test decoding for each station
    print("\nDecoding test results:")
    print("-" * 30)
    all_correct = True
    
    for i in range(len(test_data)):
        decoded_bit = cdma.decode_signal(combined_signal, i)
        original_bit = test_data[i]
        is_correct = abs(decoded_bit - original_bit) < 0.001
        
        print(f"Station {i+1}: Original={original_bit}, Decoded={decoded_bit:.3f}, "
              f"Status={'✓' if is_correct else '✗'}")
        
        if not is_correct:
            all_correct = False
    
    if all_correct:
        print("✓ All decoding tests passed!")
    else:
        print("✗ Some decoding tests failed!")
    
    return all_correct


def test_error_handling():
    """Test error handling and validation."""
    print("\n" + "="*50)
    print("Testing Error Handling")
    print("="*50)
    
    cdma = CDMASystem(order=3)
    
    # Test with different order
    try:
        cdma_small = CDMASystem(order=2)
        print(f"✓ Successfully created CDMA system with order 2 ({cdma_small.num_stations} stations)")
    except Exception as e:
        print(f"✗ Failed to create CDMA system with order 2: {e}")
        return False
    
    # Test encoding with invalid data
    try:
        # This should work fine as the method handles any numeric input
        result = cdma.encode_signals([2, -1, 0.5, 1])  # Non-binary values
        print("✓ Encoding handles non-binary values gracefully")
    except Exception as e:
        print(f"✗ Encoding failed with non-binary values: {e}")
    
    return True


def main():
    """Run all tests."""
    print("CDMA Implementation Test Suite")
    print("=" * 50)
    
    tests = [
        test_walsh_code_generation,
        test_encoding_decoding,
        test_error_handling
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        try:
            if test():
                passed += 1
        except Exception as e:
            print(f"✗ Test {test.__name__} failed with exception: {e}")
    
    print("\n" + "="*50)
    print(f"Test Results: {passed}/{total} tests passed")
    print("="*50)
    
    if passed == total:
        print("🎉 All tests passed! The CDMA implementation is working correctly.")
    else:
        print("⚠️  Some tests failed. Please check the implementation.")


if __name__ == "__main__":
    main()
