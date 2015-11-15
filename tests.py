from utils import hex_to_base64
from utils import fixed_xor
from utils import single_byte_xor
from utils import find_message

# 1-1. Hex to Base64

hex_input = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
b64_expected_result = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

b64_result = hex_to_base64(hex_input)
assert b64_expected_result == b64_result
print('1-1. Hex to Base64: passed')

# 1-2. Fixed XOR

xor_input = 0x1c0111001f010100061a024b53535009181c
xor_key = 0x686974207468652062756c6c277320657965
xor_expected_result = 0x746865206b696420646f6e277420706c6179

xor_result = fixed_xor(xor_input, xor_key)
assert xor_expected_result == xor_result
print('1-2. Fixed XOR: passed')

# 1-3. Single byte XOR

hex_str = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
sbx_expected_result = 'Cooking MC\'s like a pound of bacon'

sbx_result = single_byte_xor(hex_str)
assert sbx_expected_result == sbx_result
print('1-3. Single-byte XOR: passed')

# 1-4. Detect single-character XOR

input_file = './files/sc-xor-input-file.txt'
message = find_message(input_file)
expected_message = 'Now that the party is jumping\n'
assert message == expected_message
print('1-4. Detect single-character XOR: passed')

print('All tests passed')
