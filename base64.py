import base64
import sys

def clear_screen():
    print("\033[H\033[2J", end="")

def text_to_base64():
    text = input("\nEnter text to encode to Base64: ")
    encoded = base64.b64encode(text.encode('utf-8')).decode('utf-8')
    print(f"Result (Base64): {encoded}")

def base64_to_text():
    b64_string = input("\nEnter Base64 string to decode: ")
    try:
        decoded = base64.b64decode(b64_string.encode('utf-8')).decode('utf-8')
        print(f"Result (Text): {decoded}")
    except Exception:
        print("Error: Invalid Base64 string.")

def text_to_binary():
    text = input("\nEnter text to convert to Binary: ")
    binary = ' '.join(format(ord(char), '08b') for char in text)
    print(f"Result (Binary):\n{binary}")

def binary_to_text():
    binary_string = input("\nEnter Binary string (space-separated 8-bit bytes): ")
    try:
        binary_values = binary_string.split()
        text = "".join([chr(int(b, 2)) for b in binary_values])
        print(f"Result (Text): {text}")
    except Exception:
        print("Error: Invalid binary format. Ensure it consists of 0s and 1s.")

def main():
    while True:
        print("\n=== 2-in-1 Developer Converter ===")
        print("1. Text to Base64")
        print("2. Base64 to Text")
        print("3. Text to Binary")
        print("4. Binary to Text")
        print("5. Exit")
        
        choice = input("\nChoose an option (1-5): ").strip()
        
        if choice == '1':
            text_to_base64()
        elif choice == '2':
            base64_to_text()
        elif choice == '3':
            text_to_binary()
        elif choice == '4':
            binary_to_text()
        elif choice == '5':
            print("\nGoodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please select 1-5.")
        
        print("\n--------------------------------")

if __name__ == "__main__":
    try:
        clear_screen()
        main()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted. Goodbye!")
        sys.exit()
