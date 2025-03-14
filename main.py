import rsa
import os
from datetime import datetime

def get_input(prompt, default=None):
    """Get user input with an optional default value."""
    user_input = input(prompt).strip()
    return user_input if user_input else default

print("Generating an RSA key pair...")

public_exponent = get_input("What public exponent to use? (empty for 65537): ", "65537")

key_sizes = [512, 1024, 2048, 3072, 4096]
print("Select a key size.. (recommended 2048)")

for i, size in enumerate(key_sizes, 1):
    print(f"{i}. {size}")

while True:
    user_choice = get_input("Enter the number corresponding to your choice (default: 2048): ")

    if not user_choice:
        key_size = 2048
        break

    try:
        choice = int(user_choice)
        if 1 <= choice <= len(key_sizes):
            key_size = key_sizes[choice - 1]
            break
        else:
            print("Invalid selection. Please select a valid number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print(f"\nGenerating RSA keys with public exponent {public_exponent} and {key_size}...")

public_key, private_key = rsa.newkeys(key_size)

os.makedirs("./keys", exist_ok=True)

with open('./keys/public_key.pem', 'wb') as f:
    f.write(public_key.save_pkcs1('PEM'))

with open('./keys/private_key.pem', 'wb') as f:
    f.write(private_key.save_pkcs1('PEM'))

with open('./keys/last_generation.txt', 'w') as f:
    f.write(f"time: {current_time}\n")
    f.write(f"Public Exponent: {public_exponent} / Key Size: {key_size} bits\n")

print("\n RSA key pair generated and saved in 'keys' directory.")
