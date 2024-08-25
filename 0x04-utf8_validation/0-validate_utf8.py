#!/usr/bin/python3
"""
UTF-8 Validation
"""

def validUTF8(data):
    """
    Determine if a given data set represents a valid UTF-8 encoding.
    """
    number_of_bytes = 0

    # Iterate through each byte in the data list
    for num in data:
        # Ensure num is a valid byte (0-255)
        if num > 255:
            return False

        # If we are not in the middle of processing a multi-byte character
        if number_of_bytes == 0:
            # Determine how many bytes this character requires
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
        else:
            # For continuation bytes, they must start with '10'
            if (num >> 6) != 0b10:
                return False

        # Decrease the number of bytes to process
        number_of_bytes -= 1

    # If all bytes were properly processed, number_of_bytes should be 0
    return number_of_bytes == 0
