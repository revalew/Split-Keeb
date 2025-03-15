######################################
# ALL OF THE PIN CONFIGURATION IS DONE IN THE `classes.kb`!
######################################
from classes.kb import KMKKeyboard




######################################
# REQUIRED MODULES
######################################
from kmk.hid import HIDModes
from kmk.extensions.media_keys import MediaKeys

from kmk.keys import KC

from kmk.modules.holdtap import HoldTap
from kmk.modules.layers import Layers
from kmk.modules.tapdance import TapDance

# Notice that this Split module must be added after the HoldTap module to the keyboard.modules.
from kmk.modules.split import Split, SplitType#, SplitSide




######################################
# KEYBOARD CONFIG
######################################
keyboard = KMKKeyboard()

keyboard.extensions.append(MediaKeys())
keyboard.modules = [HoldTap(), Layers(), TapDance()]




######################################
# SPLIT CONFIG
######################################
# EE HANDS / AUTO HANDEDNESS - `split_side=None` (auto detect based on mount point - L or R)
# from storage import getmount
# side = SplitSide.RIGHT if str(getmount('/').label)[-1] == 'R' else SplitSide.LEFT
split = Split(
    split_type=SplitType.UART,
    # split_side=side,
    split_flip=False, # we don't need to flip the split because this is handled by the `coord_mapping` (hopefully)
    uart_flip=True, # both sides are the same (GP0 -> GP0, GP1 -> GP1) so we need to flip the UART
    # use_pio=True, # we don't need to use PIO because we're using the built-in UART
    data_pin=keyboard.rx,
    data_pin2=keyboard.tx,
)

keyboard.modules.append(split)




######################################
# HoldTap, TapDance, MediaKeys, and Layer Config
######################################
LS_Z = KC.HT(KC.Z, KC.LSFT) # type: ignore

RS_SLSH = KC.HT(KC.SLSH, KC.RSFT) # type: ignore

TD_ESC_C_SL_EMO = KC.TD(
    KC.HT(KC.ESC, KC.LCTL, prefer_hold=False) ,# type: ignore
    KC.LGUI(KC.SPC) ,# type: ignore
    KC.LCTL(KC.LGUI(KC.SPC) )# type: ignore
)

LG_SPC = KC.HT(KC.SPC, KC.LGUI) # type: ignore

LY1_TAB = KC.LT(1, KC.TAB) # type: ignore

LY2_ENT = KC.LT(2, KC.ENT) # type: ignore

LS_LBRC = KC.HT(KC.LBRC, KC.LSFT) # type: ignore

RS_BSLS = KC.HT(KC.BSLS, KC.RSFT) # type: ignore

LY5_TAB = KC.LT(5, KC.TAB) # type: ignore

LY6_ENT = KC.LT(6, KC.ENT) # type: ignore

TD_ESC_A_G_EMO = KC.TD(
    KC.HT(KC.ESC, KC.LALT, prefer_hold=False) ,# type: ignore
    KC.LGUI, # type: ignore
    KC.LGUI(KC.DOT) # type: ignore
)




######################################
# KEYBOARD LAYOUT
######################################
keyboard.keymap = [
    [
        KC.Q, KC.W, KC.F,            KC.P,    KC.G,   KC.J,    KC.L,    KC.U,            KC.Y,   KC.BSPC,
        KC.A, KC.R, KC.S,            KC.T,    KC.D,   KC.H,    KC.N,    KC.E,            KC.I,   KC.O,
        LS_Z, KC.X, KC.C,            KC.V,    KC.B,   KC.K,    KC.M,    KC.COMM,         KC.DOT, RS_SLSH,
                    TD_ESC_C_SL_EMO, KC.LALT, LG_SPC, LY1_TAB, LY2_ENT, TD_ESC_C_SL_EMO
    ],
    [
        KC.UNDS, KC.MINS, KC.PLUS, KC.EQL,  KC.COLN, KC.GRV,  KC.MRWD, KC.MPLY, KC.MFFD, KC.DEL,
        KC.LCBR, KC.LPRN, KC.RPRN, KC.RCBR, KC.PIPE, KC.ESC,  KC.LEFT, KC.UP,   KC.DOWN, KC.RGHT,
        LS_LBRC, KC.QUOT, KC.DQUO, KC.RBRC, KC.SCLN, KC.TILD, KC.VOLD, KC.MUTE, KC.VOLU, RS_BSLS,
                          KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS
    ],
    [
        KC.EXLM, KC.AT, KC.HASH, KC.DLR,  KC.PERC,  KC.CIRC, KC.AMPR, KC.ASTR, KC.CAPS, KC.BSPC,
        KC.N1,   KC.N2, KC.N3,   KC.N4,   KC.N5,    KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,
        KC.LSFT, KC.NO, KC.NO,   KC.NO,   KC.MO(3), KC.NO,   KC.NO,   KC.COMM, KC.DOT,  RS_SLSH, # type: ignore
                        KC.TRNS, KC.TRNS, KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS
    ], 
    [
        KC.NO,  KC.NO, KC.NO,   KC.NO,    KC.NO,   KC.NO,   KC.NO,   KC.NO,  KC.NO, KC.TO(4), # type: ignore
        KC.F1,  KC.F2, KC.F3,   KC.F4,    KC.F5,   KC.F6,   KC.F7,   KC.F8,  KC.F9, KC.F10,
        KC.F11, KC.NO, KC.NO,   KC.RESET, KC.TRNS, KC.NO,   KC.NO,   KC.NO,  KC.NO, KC.F12,
                       KC.TRNS, KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS
    ],
    [
        KC.Q, KC.W, KC.F,           KC.P,    KC.G,   KC.J,    KC.L,    KC.U,           KC.Y,   KC.BSPC,
        KC.A, KC.R, KC.S,           KC.T,    KC.D,   KC.H,    KC.N,    KC.E,           KC.I,   KC.O,
        LS_Z, KC.X, KC.C,           KC.V,    KC.B,   KC.K,    KC.M,    KC.COMM,        KC.DOT, RS_SLSH,
                    TD_ESC_A_G_EMO, KC.LCTL, KC.SPC, LY5_TAB, LY6_ENT, TD_ESC_A_G_EMO
    ],
    [
        KC.UNDS, KC.MINS, KC.PLUS, KC.EQL,  KC.COLN, KC.GRV,  KC.MRWD, KC.MPLY, KC.MFFD, KC.DEL,
        KC.LCBR, KC.LPRN, KC.RPRN, KC.RCBR, KC.PIPE, KC.ESC,  KC.LEFT, KC.UP,   KC.DOWN, KC.RGHT,
        LS_LBRC, KC.QUOT, KC.DQUO, KC.RBRC, KC.SCLN, KC.TILD, KC.VOLD, KC.MUTE, KC.VOLU, RS_BSLS,
                          KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS
    ],
    [
        KC.EXLM, KC.AT, KC.HASH, KC.DLR,  KC.PERC,  KC.CIRC, KC.AMPR, KC.ASTR, KC.CAPS, KC.BSPC,
        KC.N1,   KC.N2, KC.N3,   KC.N4,   KC.N5,    KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,
        KC.LSFT, KC.NO, KC.NO,   KC.NO,   KC.MO(7), KC.NO,   KC.NO,   KC.COMM, KC.DOT,  RS_SLSH, # type: ignore
                        KC.TRNS, KC.TRNS, KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS
    ],
    [
        KC.NO,  KC.NO, KC.NO,   KC.NO,    KC.NO,   KC.NO,   KC.NO,   KC.NO,  KC.NO, KC.TO(0), # type: ignore
        KC.F1,  KC.F2, KC.F3,   KC.F4,    KC.F5,   KC.F6,   KC.F7,   KC.F8,  KC.F9, KC.F10,
        KC.F11, KC.NO, KC.NO,   KC.RESET, KC.TRNS, KC.NO,   KC.NO,   KC.NO,  KC.NO, KC.F12,
                       KC.TRNS, KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS
    ]
]




######################################
# RUN
######################################
if __name__ == '__main__':
    keyboard.go(hid_type=HIDModes.USB)