import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation


class KMKKeyboard(_KMKKeyboard):
    def __init__(self) -> None:
        super().__init__()

        self.tx = board.TX # type: ignore # board.GP0
        self.rx = board.RX # type: ignore # board.GP1

        self.data_pin = self.rx

        # self.i2c = board.I2C
        # self.SCL = board.SCL
        # self.SDA = board.SDA

        self.col_pins = (
            board.GP2, # type: ignore
            board.GP3, # type: ignore
            board.GP4, # type: ignore
            board.GP5, # type: ignore
            board.GP6, # type: ignore
            board.GP22, # type: ignore
            board.GP21, # type: ignore
            board.GP20, # type: ignore
            board.GP19, # type: ignore
            board.GP18 # type: ignore
        )

        self.row_pins = (
            board.GP12, # type: ignore
            board.GP13, # type: ignore
            board.GP14, # type: ignore
            board.GP15 # type: ignore
        )

        self.diode_orientation = DiodeOrientation.COL2ROW

        # flake8: noqa
        # fmt: off
        self.coord_mapping = [
        0,  1,  2,  3,  4,  5,  6,  7,  8,  9,
        10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
        20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
                32, 33, 34, 35, 36, 37
        ]