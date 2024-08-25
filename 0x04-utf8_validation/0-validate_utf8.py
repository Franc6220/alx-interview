#!/usr/bin/python3
"""
UTF-8 Validation
"""

def validUTF8(data):
    """
    Determine if a given data set represents a valid UTF-8 encoding.
    """
    number_of_bytes = 0

    # Masks to determine the type of byte
    for num in data:
        # Ensure num is a valid byte (0-255)
        if num > 255:
            return False

        # If we are in the middle of processing continuation bytes
        if number_of_bytes > 0:
            # Check if this is a valid continuation byte (should start with '10')
            if (num >> 6) != 0b10:
                return False
            number_of_bytes -= 1
        else:
            # Determine how many bytes the character should have
            if (num >> 5) == 0b110:
                number_of_bytes = 1
            elif (num >> 4) == 0b1110:
                number_of_bytes = 2
            elif (num >> 3) == 0b11110:
                number_of_bytes = 3
            elif (num >> 7) == 0:
                continue
            else:
                return False

    # After processing, there should be no remaining continuation bytes expected
    return number_of_bytes == 0
