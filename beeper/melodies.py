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
HALF = 0.5
QUARTER = 0.25
EIGHTH = 0.125
SIXTEENTH = 0.0625

#TEMPO
SLOW = 0.5
MEDIUM = 0.25
FAST = 0.125

MELODIES = {
    "tada": (
        (WHOLE, C),
        (WHOLE, F),
        (WHOLE, A),
        (WHOLE, C_HIGH),
        (HALF, PAUSE),
        (HALF, A),
        (WHOLE, C_HIGH),
        (HALF, C_HIGH),
    ),
    "beepr": (
        (QUARTER, C_HIGH),
        (QUARTER, PAUSE),
        (QUARTER, C_HIGH),
        (QUARTER, PAUSE),
        (QUARTER, C_HIGH),
        (QUARTER, PAUSE),
    ),
}
