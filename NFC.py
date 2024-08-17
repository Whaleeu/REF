from adafruit_pn532.i2c import PN532_I2C

class NFCReader:
    def __init__(self, i2c_bus):
        """Initialize the NFC reader using the specified I2C bus."""
        self.pn532 = PN532_I2C(i2c_bus, debug=False)
        self.setup()

    def setup(self):
        """Configure the PN532 module to communicate with MiFare cards."""
        self.pn532.SAM_configuration()
        print("NFC reader configured and ready to detect NFC cards.")

    def read_uid(self):
        """Attempt to read the UID from an NFC card."""
        uid = self.pn532.read_passive_target(timeout=0.5)
        if uid is not None:
            return [hex(i) for i in uid]
        return None


