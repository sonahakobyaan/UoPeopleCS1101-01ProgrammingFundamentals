
def read_dictionary(filepath):
    dictionary = {}
    try:
        with open(filepath, 'r') as fin:
            for line in fin:
                line = line.strip()
                if ':' in line:
                    key, value = line.split(':', 1)
                    dictionary[key.strip()] = value.strip()
    except FileNotFoundError:
        print(f"Error: '{filepath}' was not found. Please check the filename.")
    except IOError as e:
        print(f"File error: {e}")
    return dictionary

def invert_dictionary(original):
    inverted = {}
    for key, value in original.items():
        if value not in inverted:
            inverted[value] = [key]
        else:
            inverted[value].append(key)
    return inverted

def write_inverted_dictionary(inverted, filepath):
    try:
        with open(filepath, 'w') as fout:
            fout.write('{\n')
            for key, values in inverted.items():
                fout.write(f"    {key}: {', '.join(values)}\n")
            fout.write('}\n')
        print(f"Inverted dictionary written to '{filepath}' successfully.")
    except IOError as e:
        print(f"Could not write to file: {e}")

# --- Main Program ---
input_file  = 'original_dict.txt'
output_file = 'inverted_dict.txt'

print('--- Original Dictionary ---')
original = read_dictionary(input_file)
for k, v in original.items():
    print(f'  {k}: {v}')

inverted = invert_dictionary(original)

print('\n--- Inverted Dictionary ---')
for k, v in inverted.items():
    print(f'  {k}: {", ".join(v)}')

write_inverted_dictionary(inverted, output_file)