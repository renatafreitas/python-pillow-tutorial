from PIL import Image, ImageDraw
import random

def random_colour():
    return(random.randint(0,255),random.randint(0,255),random.randint(0,255))

def interpolate(start_colour, end_colour, factor: float):
    new_colour_rgb = []
    for i in range(3):
        new_colour_value = factor * end_colour[i] + (1 - factor) * start_colour[i]
        new_colour_rgb.append(int(new_colour_value))

    return tuple(new_colour_rgb)

def generate_art():
    image_size_px = 236
    padding_px = 12

    colour_white = (255,255,255)
    colour_black = (0,0,0)
    start_colour = random_colour()
    end_colour = random_colour()

    image = Image.new('RGB', (image_size_px, image_size_px), colour_white)

#     draw lines
    draw = ImageDraw.Draw(image)
    points = []

#     Generate the points
    for _ in range(10):
        random_point = (
            random.randint(padding_px, image_size_px - padding_px),
            random.randint(padding_px, image_size_px - padding_px),
        )
        points.append(random_point)

#      Draw the points
    thickness = 0
    n_points = len(points) - 1
    for i, point in enumerate(points):
        point_1 = point

        if i == n_points:
            point_2 = points[0]
        else:
            point_2 = points[i + 1]

        line_xy = point_1, point_2
        thickness += 1
        colour_factor = 1 / n_points
        line_colour = interpolate(start_colour, end_colour, colour_factor)

        draw.line(line_xy, fill= line_colour, width=thickness)

    image.save('test_img.png')

if __name__ == "__main__":
    generate_art()
