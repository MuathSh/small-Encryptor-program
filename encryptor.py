import sys 

if len(sys.argv) < 2:
    print("Usage: python script.py [e/d]")
    sys.exit()

mode = sys.argv[1]
tag = b"\nFILE HAS BEEN ENCRYPTED"

if mode == "e":
    print("Encrypting file...")
    with open("test.txt", "rb") as f:
       code = f.read()

    if code.endswith(tag):
        code = code[:-len(tag)]

    # Split: for length 7 ("MUATH1"), half = 3.
    # first_half = 3 chars, second_half = 4 chars.
    half = len(code) // 2
    first_half = code[:half]
    second_half = code[half:]
    encrypted_file = second_half + first_half + tag

    with open("test.txt", "wb") as f:
        f.write(encrypted_file)

elif mode == "d":
    print("Decrypting file...")
    with open("test.txt", "rb") as f:
        code1 = f.read()
  
    if code1.endswith(tag):
        code1 = code1[:-len(tag)]

        # To restore the original order when second_half was larger:
        # split at len(code1) - (len(code1) // 2)
        half = len(code1) // 2
        split_index = len(code1) - half

        first_half = code1[:split_index]
        second_half = code1[split_index:]

    else:
        half = len(code1) // 2
        split_index = len(code1) - half
        
        first_half = code1[:split_index]
        second_half = code1[split_index:]


decrypted_file = second_half + first_half
with open("test.txt", "wb") as f:
 f.write(decrypted_file)