base64_table = {
  0 : "A",
  1 : "B",
  2 : "C",
  3 : "D",
  4 : "E",
  5 : "F",
  6 : "G",
  7 : "H",
  8 : "I",
  9 : "J",
  10: "K",
  11: "L",
  12: "M",
  13: "N",
  14: "O",
  15: "P",
  16: "Q",
  17: "R",
  18: "S",
  19: "T",
  20: "U",
  21: "V",
  22: "W",
  23: "X",
  24: "Y",
  25: "Z",
  26: "a",
  27: "b",
  28: "c",
  29: "d",
  30: "e",
  31: "f",
  32: "g",
  33: "h",
  34: "i",
  35: "j",
  36: "k",
  37: "l",
  38: "m",
  39: "n",
  40: "o",
  41: "p",
  42: "q",
  43: "r",
  44: "s",
  45: "t",
  46: "u",
  47: "v",
  48: "w",
  49: "x",
  50: "y",
  51: "z",
  52: "0",
  53: "1",
  54: "2",
  55: "3",
  56: "4",
  57: "5",
  58: "6",
  59: "7",
  60: "8",
  61: "9",
  62: "+",
  63: "/",
}

def hex_to_base64(input_string):

  bin_string = ""
  base64 = ""

  # Loop through the input string, every 2 characters
  for i in range(0, int(len(input_string)), 2):

    # Convert each pair to a base 10 int
    num_str = "0x" + input_string[i:i+2]
    num = int(num_str, 16)

    # Convert from base 10 to base 2 (8 bit)
    bin_string += bin(num)[2:].zfill(8)

  # Convert the binary to base64. One character every 6 bits
  for i in range(0, len(bin_string), 6):

    # Convert to base64
    bin_character = bin_string[i:i+6]
    char = base64_table[int(bin_character, 2)]
    base64 += char

    # Padding
    if len(bin_character) == 4:
      base64 += "="
    elif len(bin_character) == 2:
      base64 += "=="

  return base64

def hex_to_ascii(input_string):
  string = ""
  for i in range(0, int(len(input_string)), 2):
    num_str = "0x" + input_string[i:i+2]
    num = int(num_str, 16)
    string += chr(num)
  return string
