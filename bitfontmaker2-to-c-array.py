import json

# Your input JSON data from Bitfontmaker2
bitfont_data = {}
# Initialize an empty list for the C array
c_array = []

# Iterate over the possible 128 ASCII characters
for i in range(128):
    hex_values = ["0x00"] * 6  # Default 6x8 array with 0x00
    
    if str(i) in bitfont_data:
        # Take the second set of 8 rows
        char_data = bitfont_data[str(i)][8:16]
        
        # Convert rows to columns, correcting for upside-down and backwards rendering
        for col in range(6):
            column_value = sum(((char_data[row] >> (5 - col)) & 1) << row for row in range(8))
            hex_values[5 - col] = f"0x{column_value:02X}"  # Flip the column position
    
    # Generate the corresponding ASCII character or label
    if 32 <= i < 127:  # Printable characters
        char_label = f"('{chr(i)}')"
    else:
        char_label = ""
    
    # Create the line for the C array
    c_array.append(f"    {{{', '.join(hex_values)}}}, // 0x{i:02X} {char_label}")

# Print the C-style array with the labels
print("const unsigned char font6x8_ascii_j[128][6] = {")
print("\n".join(c_array))
print("};")