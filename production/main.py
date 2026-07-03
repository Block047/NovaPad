import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.keys import KC
from kmk.modules.rgb import RGB
from kmk.modules.encoder import EncoderHandler

novapad = KMKKeyboard()

novapad.row_pins = (board.D9, board.D8)
novapad.col_pins = (board.D10, board.D0, board.D1)
novapad.diode_orientation = DiodeOrientation.COL2ROW

novapad.keymap = [
    [
        KC.N1, KC.N2, KC.N3,
        KC.N4, KC.N5, KC.N6,
    ]
]

encoder_handler = EncoderHandler()
encoder_handler.pins = (
    (board.D3,board.D2,board.D6,False),
)
encoder_handler.map = [
    ((KC.VOLD,KC.VOLU,KC.MUTE),),
]
novapad.modules.append(encoder_handler)

rgb = RGB(
    pixel_pin=board.D7,
    num_pixels=6,
    val_limit=100,
    hue_default=0,
    sat_default=100,
    val_default=50,
    animation_mode='static',
)
novapad.modules.append(rgb)

try:
    import busio
    import displayio
    import terminalio
    from adafruit_display_text import label
    from i2cdisplaybus import I2CDisplayBus
    import adafruit_displayio_ssd1306

    displayio.release_displays()
    i2c = busio.I2C(board.D5, board.D4)
    display_bus = I2CDisplayBus(i2c, device_address=0x3C)
    display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128,height=32)

    splash = displayio.Group()
    display.root_group = splash
    text_area = label.Label(terminalio.FONT, text="NovaPad", color = 0xFFFFFF, x=4, y=15)
    splash.append(text_area)
except Exception as e:
    print("OLED init fail: ", e)

if __name__ == '__main__':
    novapad.go()