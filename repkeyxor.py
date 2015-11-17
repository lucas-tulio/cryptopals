def encrypt(message, key):
  """
  Uses a repeating-key XOR to encrypt a message
  """
  
  key_index = 0
  encrypted_message = ""

  # Encrypt!
  for char in message:
    
    char_num = ord(char)
    char_num = char_num ^ ord(key[key_index])
    encrypted_message += hex(char_num)[2:].zfill(2)
    
    # Loop the key
    key_index += 1
    if key_index >= len(key):
      key_index = 0

  return encrypted_message
