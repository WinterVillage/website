from PIL import Image

def getCroppedImage(image_path: str):
    img = Image.open(image_path)
    bbox = img.getbbox()

    if bbox:
        cropped_img = img.crop(bbox)
    else:
        cropped_img = img

    return cropped_img