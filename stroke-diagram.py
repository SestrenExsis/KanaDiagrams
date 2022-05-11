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
        (24, 33, 40, 33, 59, 32, 72, 29),
        (45, 19, 40, 47, 43, 65, 52, 85),
        (66, 40, 64, 51, 52, 94, 29, 84, 12, 64, 54, 40, 77, 53, 100, 67, 85, 86, 63, 89),
    ],
    'i-hiragana': [
        (23, 22, 22, 33, 17, 63, 29, 75, 32, 78, 37, 73, 42, 59),
        (69, 28, 78, 34, 87, 58, 86, 64),
    ],
    'u-hiragana': [
        (35, 22, 40, 23, 57, 27, 66, 28),
        (26, 51, 40, 45, 57, 41, 67, 48, 78, 64, 70, 84, 41, 93),
    ],
    'e-hiragana': [
        (32.2, 15.1, 38.9, 18.3, 51.2, 19.5, 57.4, 19.9),
        (22.2, 39.6, 32.7, 38.5, 53.5, 36.8, 62.2, 34.6, 55.8, 42.8, 33.2, 63.1, 13.8, 83.9, 41.9, 54.7, 50.7, 54.6, 54.0, 58.1, 58.3, 61.7, 54.4, 81.8, 59.6, 81.2, 61.5, 83.9, 77.3, 82.1, 84.1, 80.9),
    ],
    'o-hiragana': [
        (26.3, 36.2, 36.1, 36.4, 60.8, 34.5, 68.8, 31.4),
        (46.4, 17.9, 45.0, 39.6, 46.2, 66.3, 46.7, 79.3, 46.4, 88.9, 29.3, 88.5, 27.5, 82.0, 22.6, 61.9, 44.3, 54.0, 64.5, 53.5, 76.8, 52.1, 90.7, 58.3, 89.6, 69.3, 89.8, 75.7, 84.1, 83.2, 76.1, 83.7, 67.2, 85.2, 63.1, 77.7, 61.7, 75.2),
        (76.6, 29.3, 82.0, 31.4, 90.0, 36.4, 93.2, 41.0),
    ],
}

if __name__ == '__main__':
    diagram_name = 'o-hiragana'
    diagram = diagrams[diagrams]
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
        # TODO: Draw stroke
    dwg.save()
    print("Done!")