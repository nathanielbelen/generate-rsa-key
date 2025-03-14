# RSA Key Generator

this is a quick python script I used for generating an RSA key pair with user-defined parameters.

- generates a **public and private key** (`.pem` format).
- logs the last generation timestamp in `last_generation.txt`.

## usage
1. **install dependencies**:
   ```sh
   pip install rsa

1. **run the script**:
   ```sh
   python main.py

important resources:
https://www.keylength.com/en/4/
https://crypto.stackexchange.com/questions/3110/impacts-of-not-using-rsa-exponent-of-65537