import svgwrite
'''
'ka-hiragana': [],
'ki-hiragana': [],
'ku-hiragana': [],
'ke-hiragana': [],
'ko-hiragana': [],
'sa-hiragana': [],
'shi-hiragana': [],
'su-hiragana': [],
'se-hiragana': [],
'so-hiragana': [],
'ta-hiragana': [],
'chi-hiragana': [],
'tsu-hiragana': [],
'te-hiragana': [],
'to-hiragana': [],
'na-hiragana': [],
'ni-hiragana': [],
'nu-hiragana': [],
'ne-hiragana': [],
'no-hiragana': [],
'ha-hiragana': [],
'hi-hiragana': [],
'fu-hiragana': [],
'he-hiragana': [],
'ho-hiragana': [],
'ma-hiragana': [],
'mi-hiragana': [],
'mu-hiragana': [],
'me-hiragana': [],
'mo-hiragana': [],
'ya-hiragana': [],
'yu-hiragana': [],
'yo-hiragana': [],
'ra-hiragana': [],
'ri-hiragana': [],
'ru-hiragana': [],
're-hiragana': [],
'ro-hiragana': [],
'n-hiragana': [],
'''

diagrams = {
    'a-hiragana': [
        ((24, 33), (40, 33), (59, 32), (72, 29)),
        ((45, 19), (40, 47), (43, 65), (52, 85)),
        ((66, 40), (64, 51), (52, 94), (29, 84), (12, 64), (54, 40), (77, 53), (100, 67), (85, 86), (63, 89)),
    ],
    'i-hiragana': [
        ((23, 2), (22, 33), (17, 63), (29, 75), (32, 78), (37, 73), (42, 59)),
        ((69, 28), (78, 34), (87, 58), (86, 64)),
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
}

raw_path_strs = {
    'ko-hiragana': [
        "M287,253 C392,300 567,310 687,288",
        "M242,602 C142,810 388,822 760,792",
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

for raw_path_str in raw_path_strs['ko-hiragana']:
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
    diagram_name = 'ko-hiragana'
    diagram = diagrams[diagram_name]
    stroke_count = len(diagram)
    cell_size = 100
    height = cell_size
    half_height = int(0.5 * height)
    width = stroke_count * cell_size
    dwg = svgwrite.Drawing('test.svg', profile='full')
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
            class_style = 'stroke_order_diagram--existing-path'
            if i == stroke_id:
                class_style = 'stroke_order_diagram--current-path'
            dwg.add(dwg.path(path_str, class_=class_style))
        start_coord = (stroke_id * cell_size + diagram[stroke_id][0][0], diagram[stroke_id][0][1])
        dwg.add(dwg.circle(start_coord, 4, class_='stroke_order_diagram--path-start'))
    dwg.save()
    print("Done!")