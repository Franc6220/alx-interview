#!/usr/bin/python3
"""
UTF-8 Validation
"""

def validUTF8(data):
    """
    Determine if a given data set represents a valid UTF-8 encoding
    """
    number_of_bytes = 0

    # Masks for checking the initial byte
    mask1 = 1 << 7
    mask2 = 1 << 6

    # Iterate over each integer in the data list
    for num in data:
        # Extract the last 8 bits
        byte = num & 0xFF

        # If this is the start of a new UTF-8 character
        if number_of_bytes == 0:
        # Determine the number of bytes in the character
        mask = 1 << 7
        while mask & byte:
            number_of_bytes += 1
            mask = mask >> 1

            # If number_of_bytes is 0, it's a 1-byte character
            if number_of_bytes == 0:
                continue

            # UTF-8 characters can only be between 2 and 4 bytes long
            if number_of_bytes == 1 or number_of_bytes > 4:
                return False
            else:
                # For multi-byte characters, check that the byte starts with "10"
                if not (byte & mask1 and not (byte & mask2)):
                    return False

                # Decrease the number of bytes left to process
                number_of_bytes -= 1

                # If all characters were successfully processed, return True
                return number_of_bytes == 0
