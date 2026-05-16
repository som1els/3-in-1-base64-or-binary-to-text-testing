#!/usr/bin/env python3
import base64
import sys

# ANSI Colors for a nice CLI experience on Linux/Termux
BLUE = "\033[1;34m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
RED = "\033[1;31m"
RESET = "\033[0m"

def clear_screen():
    # Clears the terminal screen smoothly
    print("\033[H\033[2J", end="")

def text_to_base64():
    text = input(f"\nEnter text to encode to Base64: ")
    encoded = base64.b64encode(text.encode('utf-8')).decode('utf-8')
    print(f"{GREEN}Result (Base64):{RESET} {encoded}")

def base64_to_text():
    b64_string = input(f"\nEnter Base64 string to decode: ")
    try:
        decoded = base64.b64decode(b64_string.encode('utf-8')).decode('utf-8')
        print(f"{GREEN}Result (Text):{RESET} {decoded}")
    except Exception:
        print(f"{RED}Error: Invalid Base64 string.{RESET}")

def text_to_binary():
    text = input(f"\nEnter text to convert to Binary: ")
    binary = ' '.join(format(ord(char), '08b') for char in text)
    print(f"{GREEN}Result (Binary):{RESET}\n{binary}")

def binary_to_text():
    binary_string = input(f"\nEnter Binary string (space-separated 8-bit bytes): ")
    try:
        # Removes spaces if they paste a raw block, but works best with spaces
        binary_values = binary_string.split()
        text = "".join([chr(int(b, 2)) for b in binary_values])
        print(f"{GREEN}Result (Text):{RESET} {text}")
    except Exception:
        print(f"{RED}Error: Invalid binary format. Ensure it consists of 0s and 1s.{RESET}")

def main():
    while True:
        print(f"\n{BLUE}=== 2-in-1 Developer Converter ==={RESET}")
        print(f"{YELLOW}1.{RESET} Text to Base64")
        print(f"{YELLOW}2.{RESET} Base64 to Text")
        print(f"{YELLOW}3.{RESET} Text to Binary")
        print(f"{YELLOW}4.{RESET} Binary to Text")
        print(f"{YELLOW}5.{RESET} Exit")
        
        choice = input(f"\nChoose an option (1-5): ").strip()
        
        if choice == '1':
            text_to_base64()
        elif choice == '2':
            base64_to_text()
        elif choice == '3':
            text_to_binary()
        elif choice == '4':
            binary_to_text()
        elif choice == '5':
            print(f"\n{BLUE}Goodbye!{RESET}")
            sys.exit()
        else:
            print(f"{RED}Invalid choice. Please select 1-5.{RESET}")
        
        print(f"\n{BLUE}--------------------------------{RESET}")

if __name__ == "__main__":
    try:
        clear_screen()
        main()
    except KeyboardInterrupt:
        print(f"\n\n{BLUE}Program interrupted. Goodbye!{RESET}")
        sys.exit()