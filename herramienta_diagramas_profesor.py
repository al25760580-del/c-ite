"""Generador local de diagramas con los simbolos usados en la clase.

No utiliza una libreria de diagramas de flujo. Dibuja directamente los
simbolos de la tabla del profesor y guarda cada resultado como PNG.
"""

from pathlib import Path
from math import sin, pi
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent

# Colors based on the classroom examples
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_HEADER = (58, 58, 58)
HEADER_TOP = (95, 95, 95)
RED_BAR = (170, 45, 16)
ORANGE_BAR = (221, 87, 14)
BEIGE_BAR = (190, 174, 137)
ORANGE = (242, 157, 10)
PROCESS = (226, 61, 19)
SHADOW = (165, 165, 165)


def font(size, bold=False):
    paths = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf",
    ]
    for path in paths:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


FONT_HEADER = font(35, True)
FONT_NODE = font(22, True)
FONT_NODE_SMALL = font(18, True)
FONT_TERMINAL = font(21, False)


def text_lines(draw, box, text, fill=WHITE, preferred=FONT_NODE):
    """Centra un texto con ajuste de linea dentro de una caja."""
    x1, y1, x2, y2 = box
    words = text.replace("\n", " \n ").split()
    lines = []
    current = ""
    for word in words:
        if word == "\\n":
            lines.append(current)
            current = ""
            continue
        candidate = word if not current else current + " " + word
        bbox = draw.textbbox((0, 0), candidate, font=preferred)
        if bbox[2] - bbox[0] <= (x2 - x1 - 24):
            current = candidate
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    if not lines:
        lines = [text]
    line_height = preferred.getbbox("Ag")[3] - preferred.getbbox("Ag")[1] + 7
    total = line_height * len(lines)
    y = y1 + (y2 - y1 - total) / 2
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=preferred)
        x = x1 + (x2 - x1 - (bbox[2] - bbox[0])) / 2
        draw.text((x, y), line, font=preferred, fill=fill)
        y += line_height


def shadow_box(draw, box, radius=0):
    x1, y1, x2, y2 = box
    shifted = (x1 + 5, y1 + 6, x2 + 5, y2 + 6)
    if radius:
        draw.rounded_rectangle(shifted, radius=radius, fill=SHADOW)
    else:
        draw.rectangle(shifted, fill=SHADOW)


def terminal(draw, center, top, label):
    width, height = 190, 46
    x1 = center - width // 2
    x2 = center + width // 2
    box = (x1, top, x2, top + height)
    shadow_box(draw, box, radius=24)
    draw.rounded_rectangle(box, radius=24, fill=ORANGE, outline=(196, 125, 0), width=2)
    text_lines(draw, box, label, fill=WHITE, preferred=FONT_TERMINAL)
    return box


def parallelogram(draw, center, top, label, width=280, height=78):
    skew = 34
    x1 = center - width // 2
    x2 = center + width // 2
    points = [(x1 + skew, top), (x2, top), (x2 - skew, top + height), (x1, top + height)]
    shadow = [(x + 5, y + 6) for x, y in points]
    draw.polygon(shadow, fill=SHADOW)
    draw.polygon(points, fill=ORANGE, outline=(196, 125, 0))
    text_lines(draw, (x1 + 18, top + 4, x2 - 18, top + height - 4), label, fill=WHITE, preferred=FONT_NODE_SMALL)
    return (x1, top, x2, top + height)


def process(draw, center, top, label, width=300, height=78):
    x1 = center - width // 2
    x2 = center + width // 2
    box = (x1, top, x2, top + height)
    shadow_box(draw, box)
    draw.rectangle(box, fill=PROCESS, outline=(180, 44, 12), width=2)
    text_lines(draw, box, label, fill=WHITE, preferred=FONT_NODE_SMALL)
    return box


def document(draw, center, top, label, width=300, height=88):
    x1 = center - width // 2
    x2 = center + width // 2
    y_bottom = top + height
    points = [(x1, top), (x2, top), (x2, y_bottom - 17)]
    wave_count = 4
    wave_width = (x2 - x1) / wave_count
    for i in range(17):
        x = x2 - i * (x2 - x1) / 16
        y = y_bottom - 17 + 8 * sin((i / 16) * wave_count * pi)
        points.append((x, y))
    points.append((x1, top))
    shadow = [(x + 5, y + 6) for x, y in points]
    draw.polygon(shadow, fill=SHADOW)
    draw.polygon(points, fill=ORANGE, outline=(196, 125, 0))
    text_lines(draw, (x1 + 16, top + 8, x2 - 16, y_bottom - 20), label, fill=WHITE, preferred=FONT_NODE_SMALL)
    return (x1, top, x2, y_bottom)


def arrow(draw, source_box, target_box):
    x = (source_box[0] + source_box[2]) // 2
    y1 = source_box[3]
    y2 = target_box[1]
    draw.line((x, y1, x, y2), fill=BLACK, width=3)
    head = 12
    draw.polygon([(x, y2), (x - head, y2 - 18), (x + head, y2 - 18)], fill=BLACK)


def header(image, title):
    draw = ImageDraw.Draw(image)
    width = image.width
    draw.rectangle((26, 38, width - 26, 145), fill=HEADER_TOP)
    draw.rectangle((26, 54, width - 26, 145), fill=DARK_HEADER)
    draw.rectangle((26, 145, 230, 158), fill=RED_BAR)
    draw.rectangle((230, 145, 530, 158), fill=ORANGE_BAR)
    draw.rectangle((530, 145, width - 26, 158), fill=BEIGE_BAR)
    bbox = draw.textbbox((0, 0), title, font=FONT_HEADER)
    draw.text((width - 54 - (bbox[2] - bbox[0]), 78), title, font=FONT_HEADER, fill=WHITE)
    return draw


def render(title, steps, destination):
    # Each tuple is a supported class symbol: terminal, input, process, output
    height = 190 + len(steps) * 137 + 80
    image = Image.new("RGB", (1000, height), WHITE)
    draw = header(image, title)
    center = image.width // 2
    previous = None
    top = 184
    for kind, label in steps:
        if kind == "terminal":
            box = terminal(draw, center, top, label)
        elif kind == "input":
            box = parallelogram(draw, center, top, label)
        elif kind == "process":
            box = process(draw, center, top, label)
        elif kind == "output":
            box = document(draw, center, top, label)
        else:
            raise ValueError("Simbolo no soportado: " + kind)
        if previous is not None:
            arrow(draw, previous, box)
        previous = box
        top += 137
    destination.parent.mkdir(parents=True, exist_ok=True)
    image.save(destination, "PNG")



def render_val(destination):
    """Dibuja la seleccion multiple del ejercicio de VAL."""
    image = Image.new("RGB", (1200, 1050), WHITE)
    draw = header(image, "FUNCION_SELECTIVA_MULTIPLE")
    center = 600

    start = terminal(draw, center, 184, "inicio")
    input_box = parallelogram(draw, center, 270, "NUM y V", width=280, height=78)
    arrow(draw, start, input_box)

    # Selector multiple usado en el ejemplo de la profesora
    selector = [(500, 390), (700, 390), (760, 435), (700, 480), (500, 480), (440, 435)]
    selector_shadow = [(x + 5, y + 6) for x, y in selector]
    draw.polygon(selector_shadow, fill=SHADOW)
    draw.polygon(selector, fill=(120, 78, 65), outline=(85, 55, 45))
    text_lines(draw, (465, 402, 735, 468), "NUM", fill=WHITE, preferred=FONT_NODE)

    # Four branches with straight horizontal and vertical flow lines
    process_specs = [
        (165, "VAL <- 100 * V", "1"),
        (405, "VAL <- 100 ** V", "2"),
        (795, "VAL <- 100 / V", "3"),
        (1050, "VAL <- 0", "De otra forma"),
    ]
    process_boxes = []
    for x, label, branch in process_specs:
        box = process(draw, x, 540, label, width=230 if branch != "De otra forma" else 250, height=76)
        process_boxes.append(box)
        # Label the branch immediately above the process
        label_font = FONT_NODE_SMALL if branch != "De otra forma" else font(14, True)
        bbox = draw.textbbox((0, 0), branch, font=label_font)
        draw.text((x - (bbox[2] - bbox[0]) / 2, 505), branch, font=label_font, fill=BLACK)

    # Selector exits route horizontally or vertically to each process
    # The branch labels identify the selected value
    draw.line((440, 435, 165, 435), fill=BLACK, width=3)
    draw.line((165, 435, 165, 540), fill=BLACK, width=3)
    draw.polygon([(165, 540), (153, 522), (177, 522)], fill=BLACK)

    draw.line((540, 480, 540, 540), fill=BLACK, width=3)
    draw.polygon([(540, 540), (528, 522), (552, 522)], fill=BLACK)

    draw.line((660, 480, 660, 500), fill=BLACK, width=3)
    draw.line((660, 500, 795, 500), fill=BLACK, width=3)
    draw.line((795, 500, 795, 540), fill=BLACK, width=3)
    draw.polygon([(795, 540), (783, 522), (807, 522)], fill=BLACK)

    draw.line((760, 435, 1050, 435), fill=BLACK, width=3)
    draw.line((1050, 435, 1050, 540), fill=BLACK, width=3)
    draw.polygon([(1050, 540), (1038, 522), (1062, 522)], fill=BLACK)

    # Redraw branch labels after the flow lines so every branch is visible
    label_positions = {"1": 100, "2": 405, "3": 795, "De otra forma": 1050}
    for _x, _label, branch in process_specs:
        label_font = FONT_NODE_SMALL if branch != "De otra forma" else font(14, True)
        bbox = draw.textbbox((0, 0), branch, font=label_font)
        label_x = label_positions[branch]
        draw.text((label_x - (bbox[2] - bbox[0]) / 2, 505), branch, font=label_font, fill=BLACK)

    # Branches merge on one horizontal line before the output symbol
    merge_y = 690
    for box in process_boxes:
        x = (box[0] + box[2]) // 2
        draw.line((x, box[3], x, merge_y), fill=BLACK, width=3)
    draw.line((process_boxes[0][0] + (process_boxes[0][2] - process_boxes[0][0]) // 2, merge_y,
               process_boxes[-1][0] + (process_boxes[-1][2] - process_boxes[-1][0]) // 2, merge_y),
              fill=BLACK, width=3)

    output_box = document(draw, center, 735, "VAL", width=300, height=88)
    draw.line((center, merge_y, center, output_box[1]), fill=BLACK, width=3)
    draw.polygon([(center, output_box[1]), (center - 12, output_box[1] - 18), (center + 12, output_box[1] - 18)], fill=BLACK)

    end = terminal(draw, center, 900, "fin")
    draw.line((center, output_box[3], center, end[1]), fill=BLACK, width=3)
    draw.polygon([(center, end[1]), (center - 12, end[1] - 18), (center + 12, end[1] - 18)], fill=BLACK)

    destination.parent.mkdir(parents=True, exist_ok=True)
    image.save(destination, "PNG")


def main():
    render(
        "Invertir_Datos",
        [
            ("terminal", "inicio"),
            ("input", "A, B, C y D"),
            ("output", "D, C, B y A"),
            ("terminal", "fin"),
        ],
        ROOT / "FPA-P7-Primeros-programas" / "Invertir_Datos" / "diagrama.png",
    )
    render(
        "Calculo_Expresion",
        [
            ("terminal", "inicio"),
            ("input", "A y B"),
            ("process", "RES <- (A + B) ** (2 / 3)"),
            ("output", "RES"),
            ("terminal", "fin"),
        ],
        ROOT / "FPA-P7-Primeros-programas" / "Calculo_Expresion" / "diagrama.png",
    )
    render(
        "FPA-P8 Sumador",
        [
            ("terminal", "inicio"),
            ("input", "H1, M1, S1 y H2, M2, S2"),
            ("process", "TOTAL_SEGUNDOS <- S1 + S2"),
            ("process", "ACARREO_MINUTOS <- TOTAL_SEGUNDOS / 60"),
            ("process", "SEGUNDOS <- TOTAL_SEGUNDOS % 60"),
            ("process", "TOTAL_MINUTOS <- M1 + M2 + ACARREO_MINUTOS"),
            ("process", "ACARREO_HORAS <- TOTAL_MINUTOS / 60"),
            ("process", "MINUTOS <- TOTAL_MINUTOS % 60"),
            ("process", "HORAS <- H1 + H2 + ACARREO_HORAS"),
            ("output", "HORAS, MINUTOS y SEGUNDOS"),
            ("terminal", "fin"),
        ],
        ROOT / "FPA-P8-Sumador" / "diagrama.png",
    )
    render(
        "Evaluacion Sumativa",
        [
            ("terminal", "inicio"),
            ("input", "D, R y P"),
            ("process", "LITROS <- D / R y COSTO <- LITROS * P"),
            ("output", "Litros usados: LITROS y Costo total: COSTO"),
            ("terminal", "fin"),
        ],
        ROOT / "Evaluacion-Sumativa-1y2" / "diagrama.png",
    )
    render_val(ROOT / "Evaluacion-2026-10-06-VAL" / "diagrama.png")


if __name__ == "__main__":
    main()
