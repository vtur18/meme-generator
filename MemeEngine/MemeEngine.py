"""Write the quote on the image."""
from PIL import Image, ImageDraw, ImageFont
import textwrap
import random
import os


class MemeEngine():
    """MemeEngine class."""

    def __init__(self, output_dir):
        """Output_directory for the generated meme."""
        self.output_dir = output_dir

    def make_meme(self, in_path, body, author, width=500) -> str:
        """Create a Meme With an inspirational Text Greeting."""
        with Image.open(in_path) as img:
            if img.size[0] > width:
                ratio = width/float(img.size[0])
                height = int(ratio*float(img.size[1]))
                img = img.resize((width, height), Image.NEAREST)

            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype('arial.ttf', size=18)
            bodynew = body.replace('"', '')
            msg = f'"{bodynew}" \n - {author}'
            txtwidth, txtheight = draw.textsize(msg, font=font)
            w = random.randint(0, img.size[0]-txtwidth)
            h = random.randint(0, img.size[1]-txtheight)
            draw.multiline_text((w, h), msg, font=font, fill='yellow')

        random_file = str(random.randint(0, 100000))
        out_path = self.output_dir + '/' + random_file + '.png'
        img.save(out_path)
        return out_path
