import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation

#define MATRIX_ROW_PINS {D3,D2, D1,D4 }
#define MATRIX_COL_PINS { D7,E6,B4,B5,B6,B2,B3,B1,F7,F6,F5,F4 }

class KMKKeyboard(_KMKKeyboard):
    row_pins = (board.D0, board.D1, board.D2, board.D4)
    col_pins = (
        board.D6,
        board.D7,
        board.D8,
        board.D9,
        board.D10,
        board.MOSI,
        board.MISO,
        board.SCK,
        board.A0,
        board.A1,
        board.A2,
        board.A3,
    )
    diode_orientation = DiodeOrientation.COLUMNS
    i2c = board.I2C
