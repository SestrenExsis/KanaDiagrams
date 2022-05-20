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
    'ya-hiragana': [],
    'yu-hiragana': [],
    'yo-hiragana': [],
    'ra-hiragana': [],
    'ri-hiragana': [],
    'ru-hiragana': [],
    're-hiragana': [],
    'ro-hiragana': [],
    'n-hiragana': [],
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
]

raw_path_strs = {
    'mo-hiragana': [
        "M482,160 C377,745 375,820 558,850 C797,894 848,704 805,547",
        "M272,332 C398,345 533,346 663,329",
        "M261,503 C389,551 544,563 686,535",
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
