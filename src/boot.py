import board
import digitalio
from kmk.bootcfg import bootcfg

# REFER to [THE DOCS](../.ALL/boot.md) for more information


# We generally advise against importing your keyboard definition and using
# rows/columns to define sense and source pins, because that essentially loads
# the firmware twice, almost doubling boot times.


# If this key is held during boot, don't run the code which hides the storage and disables serial
# To use another key just count its row and column and use those pins
# You can also use any other pins not already used in the matrix and make a button just for accesing your storage
# If your diode orientation is ROW2COL, then make row the output and col the input
row = digitalio.DigitalInOut(board.GP20) # type: ignore
row.switch_to_output(value=True)  # Output HIGH, "source" pin

col = digitalio.DigitalInOut(board.GP17) # type: ignore
col.switch_to_input(pull=digitalio.Pull.UP)  # "sense" pin (HIGH by default, LOW when pressed)

# Check the state of the sense pin
if col.value:
    # Configuration when the button is NOT pressed (sense = HIGH)
    bootcfg(
        # COL2ROW diode orientation
        # If HIGH, bootcfg() applies the settings

        # Common matrix and direct pin configurations:
        # |diode_orientation |sense pin  |source pin |
        # |------------------|-----------|-----------|
        # |`COL2ROW`         |column     |row        |
        # |`ROW2COL`         |row        |column     |
        # |direct pin        |direct pin |`None`     |

        sense=col,
        source=row,

        # Disable autoreload if the button is pressed
        autoreload=False,
        
        # 1 for a keyboard, 2 for a mouse
        boot_device=1,
        
        # Disable REPL if the button is pressed
        cdc_console=False,

        # Disable data serial if the button is pressed
        cdc_data=False,
        
        # Enable consumer control if the button is not pressed
        consumer_control=True,
        
        # Disable MIDI if the button is pressed
        midi=False,

        # Disable mouse if the button is pressed
        mouse=False,

        # Enable storage if the button is pressed
        storage=False,

        # manufacturer, product
        usb_id=("KMK Keyboards", "Custom Board"),  # Custom USB device name
    )

else:
    # Configuration when the button IS pressed (sense forced to HIGH)
    bootcfg(
        # Force bootcfg to always run, regardless of the state of the sense pin
        # (row is always high)
        sense=row,

        # the default, which disables boot device support.
        boot_device=0, # 1 for a keyboard, 2 for a mouse

        # Disable consumer control
        consumer_control=False,

        # Disable keyboard HID endpoint
        keyboard=False,

        # Disable MIDI
        midi=False,

        # Disable mouse
        mouse=False,

        # manufacturer, product
        # will it work when boot device is disabled ???
        usb_id=("KMK Keyboards", "Storage Mode"),
    )
