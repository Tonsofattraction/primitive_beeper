#NOTES
C = 523.251
C_SHARP = D_FLAT = 554.365
D = 587.330
D_SHARP = E_FLAT = 622.254
E = 659.255
F = 698.456
F_SHARP = G_FLAT = 739.989
G = 783.991
G_SHAP = A_FLAT = 830.609
A = 880.000
A_SHARP = B_FLAT = 932.328
B = 987.767
C_HIGH = 1046.50
PAUSE = 0

#LENGTHS
WHOLE = 1
WHOLEPLUS = 1.5
HALF = 0.5
HALFPLUS = 0.75
QUARTER = 0.25
QUARTERPLUS = 0.375
EIGHTH = 0.125
SIXTEENTH = 0.0625

#TEMPO
SLOW = 0.66
MEDIUM = 0.33
FAST = 0.166

MELODIES = {
    "tada": {
        "tempo": FAST,
        "notes": (
            (WHOLE, C),
            (WHOLE, F),
            (WHOLE, A),
            (WHOLE, C_HIGH),
            (HALF, PAUSE),
            (HALF, A),
            (WHOLE, C_HIGH),
            (HALF, C_HIGH),
        )
    },
    "beepr": {
        "tempo": FAST,
        "notes": (
            (QUARTER, C_HIGH),
            (QUARTER, PAUSE),
            (QUARTER, C_HIGH),
            (QUARTER, PAUSE),
            (QUARTER, C_HIGH),
            (QUARTER, PAUSE),
        )
    },
    "witcher": {
        "tempo": MEDIUM,
        "notes": (
            (HALF, G),
            (WHOLE, C_HIGH),
            (HALF, C_HIGH),
            (WHOLE, G),
            (HALF, G),
            (WHOLE, A_FLAT),
            (HALF, B_FLAT),
            (WHOLE, G),
        )
    },
    "potter": {
        "tempo": FAST,
        "notes": (
            (WHOLE, C),
            (WHOLE, F),
            (HALF, F),
            (HALF, A_FLAT),
            (WHOLE, G),
            (WHOLE, F),
            (WHOLE, F),
            (WHOLE, C_HIGH),
            (WHOLE, B_FLAT),
            (WHOLE, B_FLAT),
            (WHOLE, B_FLAT),
            (WHOLE, G),
            (WHOLE, G),
        )
    },
    "lotr": {
        "tempo": SLOW,
        "notes": (
            (HALFPLUS, G),
            (WHOLE, G_SHAP),
            (QUARTER, G),
            (QUARTER, G_SHAP),
            (QUARTER, G),
            (QUARTER, F),
            (QUARTER, G_SHAP),
            (HALFPLUS, G),
            (WHOLEPLUS, C),
        )
    },
    "loom": {
        "tempo": MEDIUM,
        "notes": (
            (HALF, F),
            (HALF, E),
            (HALF, F),
            (WHOLE, D),
            (WHOLE, A),
            (HALF, F),
            (QUARTER, F),
            (QUARTER, F),
            (HALF, D),
            (HALF, E),
            (WHOLE, F),
            (WHOLE, D),
        )
    }
}
