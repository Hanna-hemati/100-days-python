# def greet():
#      print("Hello")
#      print("Wellcom")
#      print("Isn't the weather nice?")
#
# greet()
#
# # functions that allows for inputs
#
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"Hello how d you do {name}?")
#
# greet_with_name("Mark")

# def greet_with(name, lastname):
#     print(f"HelloP{name}")
#     print(f"How you doing {name} {lastname}")
#
# greet_with(name="mark", lastname="Pashm")

#final project

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("type your massage:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(original_text, shifted_amount, encode_or_decode):
    output_text = ""
    for letter in original_text:

        if encode_or_decode == "decode":
            shifted_amount *= -1

        shifted_position = alphabet.index(letter) - shifted_amount
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")


caesar(original_text=text, shifted_amount=shift, encode_or_decode=direction)