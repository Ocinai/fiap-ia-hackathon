
from PIL import Image, ImageDraw, ImageFont

def create_diagram_image():
    """
    Creates an image from the ASCII art diagram.
    """
    ascii_art = """
+-------------------+       +-------------------+       +-------------------+
|                   |       |                   |       |                   |
|   Presentation    | <---> |   Business Logic  | <---> |    Data Access    |
|       Tier        |       |        Tier       |       |        Tier       |
|                   |       |                   |       |                   |
+-------------------+       +-------------------+       +-------------------+
        ^                                                       |
        |                                                       |
        |                                                       |
+-------------------+                                   +-------------------+
|                   |                                   |                   |
|    User/Client    |                                   |     Database      |
|                   |                                   |                   |
+-------------------+                                   +-------------------+
"""
    
    # Create a blank image
    img = Image.new('RGB', (800, 400), color = 'white')
    
    # Get a drawing context
    d = ImageDraw.Draw(img)
    
    # Use a monospaced font
    try:
        font = ImageFont.truetype("cour.ttf", 12)
    except IOError:
        font = ImageFont.load_default()

    # Draw the text
    d.text((10,10), ascii_art, fill=(0,0,0), font=font)
    
    # Save the image
    img.save("dataset/simple_diagram.png")

if __name__ == "__main__":
    create_diagram_image()
