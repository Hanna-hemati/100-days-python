alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def caesar(original_text, shifted_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shifted_amount *= -1

    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) - shifted_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")


should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").upper()
    text = input("type your massage:\n").upper()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shifted_amount=shift, encode_or_decode=direction)

    restart = input("type 'yes' if you want to go again. otherwise, type 'no'.\n").upper()
    if restart == "no":
        should_continue = False
        print("بای بای")
