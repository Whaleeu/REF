from NFC import NFCReader
import board
import busio

def main():
    # Setup I2C connection
    i2c = busio.I2C(board.SCL, board.SDA)
    nfc_reader = NFCReader(i2c)

    print("Waiting for an NFC card...")

    while True:
        uid = nfc_reader.read_uid()
        if uid:
            print('Found card with UID:', uid)
        else:
            print("No card detected.")

if __name__ == '__main__':
    main()

