import svgwrite

diagrams = {
    'a-hiragana': [
        ((24, 33), (40, 33), (59, 32), (72, 29)),
        ((45, 19), (40, 47), (43, 65), (52, 85)),
        ((66, 40), (64, 51), (52, 94), (29, 84), (12, 64), (54, 40), (77, 53), (100, 67), (85, 86), (63, 89)),
    ],
    'i-hiragana': [
        ((23, 12), (22, 43), (17, 73), (29, 85), (32, 88), (37, 83), (42, 69)),
        ((69, 38), (78, 44), (87, 68), (86, 74)),
    ],
    'u-hiragana': [
        ((35, 22), (40, 23), (57, 27), (66, 28)),
        ((26, 51), (40, 45), (57, 41), (67, 48), (78, 64), (70, 84), (41, 93)),
    ],
    'e-hiragana': [
        ((32, 15), (39, 18), (51, 20), (57, 20)),
        ((22, 40), (33, 39), (54, 37), (62, 35), (56, 43), (33, 63), (14, 84), (42, 55), (51, 55), (54, 58), (58, 62), (54, 82), (60, 81), (62, 84), (77, 82), (84, 81)),
    ],
    'o-hiragana': [
        ((26, 36), (36, 36), (61, 35), (69, 31)),
        ((46, 18), (45, 40), (46, 66), (47, 79), (46, 89), (29, 89), (28, 82), (23, 62), (44, 54), (65, 54), (77, 52), (91, 58), (90, 69), (90, 76), (84, 83), (76, 84), (67, 85), (63, 78), (62, 75)),
        ((77, 29), (82, 31), (90, 36), (93, 41)),
    ],
    'ka-hiragana': [
        ((15,47), (40,45), (52,39), (56,50), (58,59), (59,86), (47,89), (44,89), (40,84), (38,82)),
        ((38,24), (36,51), (20,82), (18,89)),
        ((70,37), (77,45), (85,59), (88,69)),
    ],
    'ki-hiragana': [
        ((26, 34), (37, 35), (58, 33), (70, 28)),
        ((21, 51), (52, 50), (69, 48), (82, 43)),
        ((46, 17), (48, 27), (58, 52), (71, 68), (22, 48), (5, 96), (66, 88)),
    ],
    'ku-hiragana': [
        ((60, 17), (23, 71), (11, 33), (63, 87)),
    ],
    'ke-hiragana': [
        ((25, 21), (16, 80), (27, 84), (35, 70)),
        ((43, 39), (64, 40), (79, 38), (87, 36)),
        ((70, 16), (67, 32), (83, 76), (52, 88)),
    ],
    'ko-hiragana': [
        ((28, 25), (39, 30), (56, 31), (68, 28)),
        ((24, 60), (14, 81), (38, 82), (76, 79)),
    ],
    'sa-hiragana': [
        ((17, 41), (35, 42), (64, 38), (74, 33)),
        ((44, 20), (46, 36), (60, 59), (70, 68), (18, 45), (6, 97), (65, 88)),
    ],
    'shi-hiragana': [
        ((34, 14), (31, 62), (29, 78), (46, 80), (61, 83), (74, 70), (80, 61)),
    ],
    'su-hiragana': [
        ((15, 33), (41, 33), (65, 32), (89, 31)),
        ((57, 15), (57, 40), (63, 69), (45, 68), (27, 64), (37, 39), (54, 49), (66, 63), (53, 86), (39, 91)),
    ],
    'se-hiragana': [
        ((15, 48), (35, 48), (66, 45), (92, 43)),
        ((68, 22), (66, 51), (75, 72), (52, 63)),
        ((38, 25), (35, 96), (35, 84), (81, 84)),
    ],
    'so-hiragana': [
        ((29, 26), (45, 26), (54, 25), (64, 24), (24, 59), (21, 54), (12, 55), (37, 53), (58, 49), (80, 48), (43, 48), (20, 97), (69, 88)),
    ],
    'ta-hiragana': [
        ((20, 35), (32, 35), (47, 34), (62, 30)),
        ((43, 16), (37, 39), (33, 64), (21, 85)),
        ((57, 45), (67, 44), (80, 44), (86, 45)),
        ((50, 64), (49, 83), (68, 82), (87, 80)),
    ],
    'chi-hiragana': [
        ((14, 36), (29, 37), (51, 34), (65, 30)),
        ((38, 16), (33, 43), (31, 55), (29, 67), (76, 28), (98, 94), (34, 86)),
    ],
    'tsu-hiragana': [
        ((15, 40), (110, 5), (95, 83), (38, 76)),
    ],
    'te-hiragana': [
        ((11, 31), (45, 27), (69, 24), (77, 22)),
        ((77, 22), (28, 31), (22, 88), (69, 82)),
    ],
    'to-hiragana': [
        ((36, 19), (35, 27), (36, 38), (41, 50)),
        ((70, 38), (2, 62), (13, 90), (70, 83)),
    ],
    'na-hiragana': [
        ((17, 36), (30, 37), (46, 34), (56, 31)),
        ((42, 18), (35, 43), (27, 61), (18, 74)),
        ((66, 33), (73, 37), (81, 41), (87, 44)),
        ((62, 47), (60, 70), (69, 91), (47, 88), (31, 83), (37, 62), (62, 72), (70, 74), (78, 78), (85, 82)),
    ],
    'ni-hiragana': [
        ((27, 19), (24, 61), (23, 99), (38, 76)),
        ((50, 30), (61, 30), (76, 29), (85, 29)),
        ((50, 60), (51, 76), (58, 79), (89, 77)),
    ],
    'nu-hiragana': [
        ((18, 29), (19, 35), (33, 67), (44, 77)),
        ((54, 21), (48, 60), (35, 89), (22, 81), (9, 73), (19, 28), (63, 36), (93, 46), (82, 76), (66, 83), (51, 88), (50, 66), (64, 68), (71, 69), (80, 75), (87, 82)),
    ],
    'ne-hiragana': [
        ((34, 16), (35, 32), (33, 74), (35, 89)),
        ((14, 41), (23, 39), (35, 36), (42, 32), (32, 51), (22, 67), (15, 76), (39, 38), (64, 30), (71, 36), (83, 41), (86, 83), (63, 81), (41, 76), (59, 48), (88, 80)),
    ],
    'no-hiragana': [
        ((51, 26), (38, 91), (13, 75), (16, 50), (31, 6), (77, 20), (79, 40), (84, 50), (81, 73), (52, 78)),
    ],
    'ha-hiragana': [
        ((22, 22), (16, 89), (24, 94), (33, 79)),
        ((41, 38), (52, 38), (79, 38), (88, 36)),
        ((68, 20), (68, 52), (74, 87), (61, 86), (37, 91), (36, 50), (89, 80)),
    ],
    'hi-hiragana': [
        ((14, 29), (26, 28), (36, 25), (41, 23), (34, 33), (4, 73), (35, 82), (68, 87), (72, 62), (62, 22), (69, 42), (79, 52), (85, 58)),
    ],
    'fu-hiragana': [
        ((33, 22), (38, 25), (53, 31), (59, 32)),
        ((38, 40), (31, 64), (57, 57), (58, 75), (59, 92), (37, 90), (31, 80)),
        ((30, 64), (25, 68), (16, 75), (10, 82)),
        ((65, 58), (72, 64), (78, 68), (84, 78)),
    ],
    'he-hiragana': [
        ((14, 53), (61, 15), (28, 27), (87, 68)),
    ],
    'ho-hiragana': [
        ((21, 20), (17, 64), (17, 100), (32, 77)),
        ((41, 24), (57, 25), (70, 24), (83, 22)),
        ((40, 46), (54, 46), (70, 46), (87, 43)),
        ((67, 28), (65, 60), (76, 83), (57, 84), (31, 84), (44, 50), (88, 78)),
    ],
    'ma-hiragana': [
        ((24, 28), (51, 28), (72, 26), (82, 25)),
        ((30, 43), (37, 48), (63, 46), (79, 44)),
        ((55, 9), (55, 60), (65, 83), (43, 82), (16, 80), (29, 43), (82, 74)),
    ],
    'mi-hiragana': [
        ((24, 25), (34, 24), (45, 23), (55, 21), (38, 58), (35, 81), (20, 75), (4, 62), (30, 33), (87, 65)),
        ((77, 36), (74, 62), (65, 78), (51, 86)),
    ],
    'mu-hiragana': [
        ((14, 34), (35, 34), (46, 33), (59, 30)),
        ((36, 17), (34, 41), (41, 72), (24, 72), (11, 72), (18, 42), (34, 53), (41, 62), (21, 80), (40, 87), (68, 89), (82, 87), (70, 61)),
        ((69, 38), (76, 42), (82, 49), (86, 52)),
    ],
    'me-hiragana': [
        ((25, 25), (26, 44), (38, 61), (48, 75)),
        ((61, 18), (52, 57), (32, 92), (20, 75), (8, 47), (50, 20), (74, 38), (90, 52), (89, 77), (56, 85)),
    ],
    'mo-hiragana': [
        ((48, 16), (37, 74), (37, 82), (55, 85), (79, 89), (84, 70), (80, 54)),
        ((27, 33), (39, 34), (53, 34), (66, 32)),
        ((26, 50), (38, 55), (54, 56), (68, 53)),
    ],
    'ya-hiragana': [
        ((18, 54), (119, 0), (95, 86), (59, 57)),
        ((62, 18), (62, 24), (61, 31), (62, 37)),
        ((33, 22), (39, 42), (51, 69), (57, 89)),
    ],
    'yu-hiragana': [
        ((19, 28), (15, 61), (18, 72), (21, 79), (16, 50), (56, 25), (77, 42), (96, 62), (59, 91), (39, 65)),
        ((56, 19), (56, 42), (64, 66), (41, 91)),
    ],
    'yo-hiragana': [
        ((52, 38), (64, 38), (73, 36), (80, 34)),
        ((51, 14), (51, 59), (60, 84), (38, 84), (13, 87), (18, 42), (81, 77)),
    ],
    'ra-hiragana': [
        ((36, 17), (42, 20), (52, 24), (61, 25)),
        ((33, 35), (30, 46), (29, 59), (28, 68), (77, 21), (102, 91), (38, 85)),
    ],
    'ri-hiragana': [
        ((29, 13), (21, 59), (30, 67), (38, 47)),
        ((62, 11), (69, 64), (59, 75), (37, 84)),
    ],
    'ru-hiragana': [
        ((20, 26), (33, 25), (46, 24), (57, 22), (48, 32), (28, 54), (13, 70), (65, 16), (94, 82), (47, 88), (9, 89), (41, 51), (55, 84)),
    ],
    're-hiragana': [
        ((32, 16), (30, 43), (31, 80), (32, 89)),
        ((13, 41), (22, 39), (32, 37), (38, 33), (32, 46), (20, 68), (12, 75), (38, 42), (73, 14), (69, 48), (67, 82), (72, 94), (87, 66)),
    ],
    'ro-hiragana': [
        ((30, 27), (41, 26), (55, 24), (67, 22), (52, 38), (40, 53), (23, 70), (80, 10), (108, 97), (42, 87)),
    ],
    'wa-hiragana': [
        ((32, 16), (30, 43), (31, 80), (32, 89)),
        ((13, 41), (22, 39), (32, 37), (38, 33), (32, 46), (20, 68), (12, 75), (70, 0), (122, 67), (59, 83)),
    ],
    'wo-hiragana': [
        ((29, 34), (43, 33), (61, 32), (76, 28)),
        ((59, 18), (51, 37), (41, 52), (30, 60), (54, 41), (70, 37), (65, 74)),
        ((91, 46), (15, 74), (41, 94), (86, 87)),
    ],
    'n-hiragana': [
        ((50, 12), (40, 37), (29, 53), (16, 78), (56, 19), (56, 51), (57, 61), (58, 91), (82, 73), (87, 50)),
    ],
    'a-katakana': [
        ((13, 29), (34, 28), (62, 28), (78, 27), (74, 36), (61, 50), (52, 54)),
        ((46, 41), (47, 64), (38, 80), (26, 88)),
    ],
    'i-katakana': [
        ((15, 62), (40, 52), (63, 32), (71, 17)),
        ((54, 43), (53, 58), (54, 71), (53, 88)),
    ],
    'u-katakana': [
        ((55, 19), (55, 24), (55, 30), (55, 38)),
        ((30, 37), (30, 44), (30, 56), (30, 64)),
        ((30, 37), (45, 37), (69, 37), (85, 36), (80, 69), (73, 82), (42, 89)),
    ],
    'e-katakana': [
        ((23, 27), (40, 27), (62, 27), (78, 27)),
        ((51, 27), (51, 40), (51, 60), (51, 70)),
        ((13, 70), (35, 69), (69, 70), (88, 69)),
    ],
    'o-katakana': [
        ((15, 40), (36, 40), (64, 41), (90, 40)),
        ((59, 19), (59, 97), (65, 91), (44, 86)),
        ((55, 41), (44, 62), (26, 76), (16, 82)),
    ],
    'ka-katakana': [
        ((11, 39), (26, 38), (59, 38), (71, 36), (64, 45), (78, 98), (50, 79)),
        ((41, 16), (43, 47), (35, 68), (15, 86)),
    ],
    'ki-katakana': [
        ((21, 39), (31, 37), (66, 32), (75, 30)),
        ((19, 64), (28, 63), (74, 56), (86, 54)),
        ((45, 17), (47, 28), (59, 81), (61, 90)),
    ],
    'ku-katakana': [
        ((46, 18), (43, 33), (34, 48), (23, 55)),
        ((42, 30), (46, 31), (72, 31), (76, 30), (72, 33), (73, 69), (26, 85)),
    ],
    'ke-katakana': [
        ((39, 14), (37, 30), (29, 46), (16, 57)),
        ((33, 34), (39, 34), (78, 35), (84, 35)),
        ((61, 34), (62, 62), (49, 77), (29, 81)),
    ],
    'ko-katakana': [
        ((18, 28), (25, 28), (65, 28), (72, 28), (71, 36), (72, 71), (72, 77)),
        ((18, 70), (24, 69), (65, 70), (71, 70)),
    ],
    'sa-katakana': [
        ((11, 46), (21, 46), (81, 45), (88, 46)),
        ((33, 25), (32, 33), (33, 62), (34, 68)),
        ((64, 20), (65, 69), (63, 79), (40, 87)),
    ],
    'shi-katakana': [
        ((26, 18), (33, 21), (41, 26), (46, 30)),
        ((17, 38), (24, 40), (32, 45), (37, 49)),
        ((24, 80), (52, 74), (75, 56), (83, 38)),
    ],
    'su-katakana': [
        ((24, 30), (38, 29), (59, 28), (69, 27), (60, 51), (40, 72), (14, 81)),
        ((55, 53), (64, 60), (78, 72), (84, 80)),
    ],
    'se-katakana': [
        ((9, 45), (25, 43), (66, 38), (78, 36), (75, 41), (65, 53), (57, 59)),
        ((33, 20), (33, 99), (27, 78), (76, 81)),
    ],
    'so-katakana': [
        ((19, 27), (21, 30), (28, 39), (32, 44)),
        ((71, 22), (64, 67), (47, 76), (26, 82)),
    ],
    'ta-katakana': [
        ((43, 16), (40, 31), (27, 47), (19, 54)),
        ((38, 30), (49, 30), (66, 30), (73, 30), (67, 40), (68, 70), (22, 85)),
        ((37, 46), (46, 50), (58, 59), (65, 66)),
    ],
    'chi-katakana': [
        ((70, 21), (63, 25), (41, 30), (23, 32)),
        ((14, 51), (29, 51), (76, 51), (88, 52)),
        ((53, 32), (51, 49), (60, 78), (29, 86)),
    ],
    'tsu-katakana': [
        ((16, 33), (21, 37), (26, 44), (29, 50)),
        ((36, 25), (41, 31), (46, 37), (48, 43)),
        ((77, 24), (72, 51), (66, 70), (31, 86)),
    ],
    'te-katakana': [
        ((29, 29), (39, 29), (66, 30), (74, 29)),
        ((17, 50), (34, 50), (75, 50), (88, 50)),
        ((55, 50), (55, 61), (54, 78), (32, 87)),
    ],
    'to-katakana': [
        ((39, 11), (40, 25), (39, 63), (39, 84)),
        ((44, 37), (55, 41), (68, 50), (73, 55)),
    ],
    'na-katakana': [
        ((13, 41), (30, 41), (75, 42), (85, 41)),
        ((51, 18), (51, 34), (58, 72), (28, 83)),
    ],
    'ni-katakana': [
        ((28, 36), (39, 36), (67, 37), (78, 37)),
        ((16, 79), (29, 78), (77, 79), (90, 79)),
    ],
    'nu-katakana': [
        ((30, 29), (41, 29), (70, 28), (77, 26), (68, 54), (45, 74), (25, 80)),
        ((42, 44), (51, 49), (74, 65), (80, 73)),
    ],
    'ne-katakana': [
        ((48, 12), (48, 16), (48, 25), (48, 30)),
        ((24, 32), (32, 31), (61, 31), (69, 30), (58, 49), (39, 64), (16, 70)),
        ((48, 56), (49, 63), (48, 81), (48, 87)),
        ((62, 53), (68, 57), (78, 63), (82, 66)),
    ],
    'no-katakana': [
        ((68, 15), (67, 30), (56, 65), (19, 77)),
    ],
    'ha-katakana': [
        ((37, 28), (34, 45), (24, 60), (13, 70)),
        ((61, 26), (69, 36), (82, 56), (86, 69)),
    ],
    'hi-katakana': [
        ((28, 45), (39, 44), (64, 39), (72, 32)),
        ((28, 17), (28, 86), (18, 74), (80, 75)),
    ],
    'fu-katakana': [
        ((20, 32), (36, 33), (70, 32), (78, 31), (71, 75), (50, 77), (29, 82)),
    ],
    'he-katakana': [
        ((14, 63), (63, 32), (17, 29), (88, 75)),
    ],
    'ho-katakana': [
        ((17, 37), (30, 37), (67, 37), (88, 37)),
        ((52, 16), (49, 89), (60, 86), (40, 82)),
        ((35, 53), (32, 58), (24, 71), (18, 77)),
        ((69, 52), (74, 57), (83, 67), (89, 72)),
    ],
    'ma-katakana': [
        ((13, 34), (25, 33), (70, 32), (80, 30), (74, 40), (58, 60), (47, 67)),
        ((30, 54), (39, 59), (56, 75), (61, 81)),
    ],
    'mi-katakana': [
        ((40, 25), (49, 26), (70, 32), (77, 35)),
        ((39, 48), (47, 49), (67, 54), (74, 58)),
        ((30, 71), (41, 71), (74, 82), (81, 87)),
    ],
    'mu-katakana': [
        ((53, 13), (36, 67), (33, 71), (21, 70), (34, 68), (74, 63), (83, 61)),
        ((71, 41), (78, 50), (87, 67), (90, 75)),
    ],
    'me-katakana': [
        ((68, 18), (66, 38), (47, 72), (17, 81)),
        ((30, 36), (43, 40), (66, 58), (74, 65)),
    ],
    'mo-katakana': [
        ((24, 28), (36, 28), (66, 28), (77, 28)),
        ((18, 52), (33, 52), (73, 51), (88, 52)),
        ((50, 33), (48, 86), (45, 80), (83, 79)),
    ],
    'ya-katakana': [
        ((12, 48), (26, 46), (64, 38), (81, 36), (73, 46), (66, 55), (59, 62)),
        ((35, 20), (39, 33), (48, 75), (51, 90)),
    ],
    'yu-katakana': [
        ((26, 34), (35, 35), (60, 35), (69, 35), (68, 43), (67, 68), (67, 75)),
        ((16, 75), (30, 75), (78, 75), (89, 75)),
    ],
    'yo-katakana': [
        ((27, 30), (37, 30), (68, 30), (76, 30), (77, 41), (76, 82), (76, 91)),
        ((31, 55), (42, 55), (66, 55), (76, 55)),
        ((27, 83), (36, 83), (68, 83), (77, 83)),
    ],
    'ra-katakana': [
        ((32, 24), (39, 24), (66, 24), (73, 23)),
        ((22, 42), (36, 42), (71, 42), (83, 41), (79, 58), (67, 83), (31, 86)),
    ],
    'ri-katakana': [
        ((31, 16), (31, 24), (31, 47), (31, 58)),
        ((64, 12), (63, 45), (72, 70), (37, 83)),
    ],
    'ru-katakana': [
        ((35, 23), (33, 51), (34, 59), (14, 77)),
        ((55, 18), (56, 72), (56, 75), (52, 76), (67, 70), (80, 55), (86, 43)),
    ],
    're-katakana': [
        ((38, 14), (38, 57), (40, 73), (35, 74), (60, 69), (79, 52), (83, 38)),
    ],
    'ro-katakana': [
        ((26, 26), (27, 37), (26, 67), (25, 77)),
        ((26, 26), (36, 25), (70, 25), (79, 26), (78, 33), (78, 69), (79, 77)),
        ((26, 69), (39, 69), (67, 69), (79, 69)),
    ],
    'wa-katakana': [
        ((33, 31), (32, 38), (33, 50), (33, 57)),
        ((33, 31), (41, 31), (74, 30), (86, 30), (81, 36), (90, 73), (42, 83)),
    ],
    'wo-katakana': [
        ((24, 28), (35, 29), (75, 29), (80, 27)),
        ((28, 48), (36, 49), (66, 48), (75, 49)),
        ((80, 27), (74, 27), (85, 75), (35, 85)),
    ],
    'n-katakana': [
        ((20, 22), (25, 26), (32, 31), (38, 35)),
        ((20, 79), (40, 76), (72, 58), (80, 33)),
    ],
}

diagram_names = [
    'a-hiragana',
    'i-hiragana',
    'u-hiragana',
    'e-hiragana',
    'o-hiragana',
    'ka-hiragana',
    'ki-hiragana',
    'ku-hiragana',
    'ke-hiragana',
    'ko-hiragana',
    'sa-hiragana',
    'shi-hiragana',
    'su-hiragana',
    'se-hiragana',
    'so-hiragana',
    'ta-hiragana',
    'chi-hiragana',
    'tsu-hiragana',
    'te-hiragana',
    'to-hiragana',
    'na-hiragana',
    'ni-hiragana',
    'nu-hiragana',
    'ne-hiragana',
    'no-hiragana',
    'ha-hiragana',
    'hi-hiragana',
    'fu-hiragana',
    'he-hiragana',
    'ho-hiragana',
    'ma-hiragana',
    'mi-hiragana',
    'mu-hiragana',
    'me-hiragana',
    'mo-hiragana',
    'ya-hiragana',
    'yu-hiragana',
    'yo-hiragana',
    'ra-hiragana',
    'ri-hiragana',
    'ru-hiragana',
    're-hiragana',
    'ro-hiragana',
    'wa-hiragana',
    'wo-hiragana',
    'n-hiragana',
    'a-katakana',
    'i-katakana',
    'u-katakana',
    'e-katakana',
    'o-katakana',
    'ka-katakana',
    'ki-katakana',
    'ku-katakana',
    'ke-katakana',
    'ko-katakana',
    'sa-katakana',
    'shi-katakana',
    'su-katakana',
    'se-katakana',
    'so-katakana',
    'ta-katakana',
    'chi-katakana',
    'tsu-katakana',
    'te-katakana',
    'to-katakana',
    'na-katakana',
    'ni-katakana',
    'nu-katakana',
    'ne-katakana',
    'no-katakana',
    'ha-katakana',
    'hi-katakana',
    'fu-katakana',
    'he-katakana',
    'ho-katakana',
    'ma-katakana',
    'mi-katakana',
    'mu-katakana',
    'me-katakana',
    'mo-katakana',
    'ya-katakana',
    'yu-katakana',
    'yo-katakana',
    'ra-katakana',
    'ri-katakana',
    'ru-katakana',
    're-katakana',
    'ro-katakana',
    'wa-katakana',
    'wo-katakana',
    'n-katakana',
]

raw_path_strs = {
    'wa-katakana': [
        "M334,318 C329,387 334,503 331,572",
        "M336,311 C416,314 747,309 864,309 C811,362 909,734 427,837",
    ],
    'wo-katakana': [
        "M249,288 C352,291 759,295 805,275",
        "M281,482 C363,490 660,482 759,490",
        "M805,277 C749,275 857,754 354,852",
    ],
    'n-katakana': [
        "M202,229 C252,268 329,314 382,353",
        "M204,798 C407,764 720,588 802,337",
    ],
}

def get_path(path_str) -> tuple:
    # path_str: "M261,345 C370,355 580,330 706,282" -->
    # path: ((26, 35), (37, 36), (58, 33), (71,28))
    parts = path_str.split(' ')
    coords = []
    for part in parts:
        raw_coord = part.split(',')
        x = int(raw_coord[0][1:] if raw_coord[0][0] in 'MC' else raw_coord[0])
        y = int(raw_coord[1][1:] if raw_coord[1][0] in 'MC' else raw_coord[1])
        coord = (x // 10, y // 10)
        coords.append(coord)
    result = tuple(coords)
    print(result)
    return result

for path_name in raw_path_strs:
    print(path_name)
    for raw_path_str in raw_path_strs[path_name]:
        get_path(raw_path_str)

def get_path_str(coords, offset) -> str:
    # coords: ((24, 33), (40, 33), (59, 32), (72, 29)), offset: (1,2) -->
    # result: 'M 25,35 C 41,35, 60,34, 73,31'
    path = []
    for coord in coords:
        if len(path) == 0:
            path.append('M')
        elif len(path) == 2:
            path.append('C')
        adjusted_coord = (coord[0] + offset[0], coord[1] + offset[1])
        path.append(' '.join(map(str, adjusted_coord)))
    result = ' '.join(path)
    return result

if __name__ == '__main__':
    for diagram_name in diagram_names:
        cell_size = 100
        diagram = diagrams[diagram_name]
        stroke_count = len(diagram)
        width = stroke_count * cell_size
        height = cell_size
        half_height = int(0.5 * height)
        dwg = svgwrite.Drawing('assets/' + diagram_name + '.svg',
            profile='full',
            size=(width, height),
            viewBox=(0, 0, width, height)
            )
        dwg.add_stylesheet('stroke-diagram.css', title="Stroke Diagram")
        dwg.add(dwg.line((1, 1), (width - 1, 1), class_='stroke-diagram--bounding-box'))
        dwg.add(dwg.line((1, 1), (1, height - 1), class_='stroke-diagram--bounding-box'))
        dwg.add(dwg.line((1, height - 1), (width - 1, height - 1), class_='stroke-diagram--bounding-box'))
        dwg.add(dwg.line((0, half_height), (width, half_height), class_='stroke-diagram--guide-line'))
        for stroke_id in range(stroke_count):
            # Draw grid
            mid = int((stroke_id + 0.5) * cell_size)
            dwg.add(dwg.line((mid, 1), (mid, height - 1), class_='stroke-diagram--guide-line'))
            right = int((stroke_id + 1) * cell_size)
            dwg.add(dwg.line((right - 1, 1), (right - 1, height - 1), class_='stroke-diagram--bounding-box'))
            start_coord = None
            for i in range(stroke_id + 1):
                path_str = get_path_str(diagram[i], (stroke_id * cell_size, 0))
                class_style = 'stroke-diagram--existing-path'
                if i == stroke_id:
                    class_style = 'stroke-diagram--current-path'
                dwg.add(dwg.path(path_str, class_=class_style))
            start_coord = (stroke_id * cell_size + diagram[stroke_id][0][0], diagram[stroke_id][0][1])
            dwg.add(dwg.circle(start_coord, 4, class_='stroke-diagram--path-start'))
        dwg.save()
