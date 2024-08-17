import board
import busio
from adafruit_pn532.i2c import PN532_I2C

# Initialize I2C connection
i2c = busio.I2C(board.SCL, board.SDA)
reset_pin = None  # Optional reset pin
req_pin = None    # Optional request pin
pn532 = PN532_I2C(i2c, debug=False, reset=reset_pin, req=req_pin)

# Configure PN532 to communicate with MiFare cards
pn532.SAM_configuration()
print("PN532 configured for MIFARE Classic card communication.")

def authenticate_block(block_number, key_type='A', key=b'\xFF\xFF\xFF\xFF\xFF\xFF'):
    """
    Authenticate a block to enable read operations.
    Default key is the common MIFARE factory default key for key A.
    """
    print(f"Authenticating block {block_number} with key type {key_type}...")
    authenticated = pn532.mifare_classic_authenticate_block(block_number, key_number=0, key=key, key_type=key_type)
    if authenticated:
        print("Authentication successful!")
    else:
        print("Authentication failed.")
    return authenticated

def read_block(block_number):
    """
    Read a single block from the authenticated sector.
    """
    print(f"Reading block {block_number}...")
    data = pn532.mifare_classic_read_block(block_number)
    if data is not None:
        print("Read successful:", data)
    else:
        print("Failed to read block.")
    return data

def main():
    block_to_read = 4  # Change this to the block you want to read
    if authenticate_block(block_to_read):
        data = read_block(block_to_read)
        if data is not None:
            print("Data from block", block_to_read, ":", data)
        else:
            print("No data read or block reading error.")
    else:
        print("Could not authenticate. Please check the card and key.")

if __name__ == '__main__':
    main()
