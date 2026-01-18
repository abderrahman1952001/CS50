import sys
from PIL import Image, ImageOps


def main():

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")


    input_image = sys.argv[1]
    output_image = sys.argv[2]


    extensions = (".jpg", ".jpeg", ".png")


    if not input_image.lower().endswith(extensions):
        sys.exit("Invalid input")

    if not output_image.lower().endswith(extensions):
        sys.exit("Invalid output")


    input_extension = input_image.rsplit(".", 1)[1]
    output_extension = output_image.rsplit(".", 1)[1]

    if input_extension != output_extension:
        sys.exit("Input and output have different extensions")


    try:
        shirt = Image.open("shirt.png")
        photo = Image.open(input_image)
    except FileNotFoundError:
        sys.exit("Input does not exist")

    photo = ImageOps.fit(photo, shirt.size)
    photo.paste(shirt, shirt)
    photo.save(output_image)


if __name__ == "__main__":
    main()
