import sys 
if len(sys.argv) < 2:
    print("Usage: python script.py [e/d]")
    sys.exit()

mode = sys.argv[1]

if mode == "e":
    print("Encrypting file...")
    with open("test.txt", "rb") as f:
       code = f.read()

    half = len(code) // 2
    first_half = code[:half]
    second_half = code[half:]
    encrypted_file = second_half + first_half + b"\nFILE HAS BEEN ENCRYPTED"

    with open("test.txt", "wb") as f:
            f.write(encrypted_file)

elif mode == "d":
  print("Decrypting file...")
  with open("test.txt", "rb") as f:
        code1 = f.read()
  tag = b"\nFILE HAS BEEN ENCRYPTED"
  if code1.endswith(tag):
        code1 = code1[:-len(tag)]

        half = len(code1) // 2
        split_index = len(code1) - half

        first_half = code1[:split_index]
        second_half = code1[split_index:]

        decrypted_file = second_half + first_half
        with open("test.txt", "wb") as f:
         f.write(decrypted_file)