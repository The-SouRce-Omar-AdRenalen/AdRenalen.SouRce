import asyncio
import os
import random
import re
import textwrap
import aiofiles
import aiohttp
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps
from youtubesearchpython.__future__ import VideosSearch
import numpy as np
from config import YOUTUBE_IMG_URL


circle = Image.open("AdRenalen/assets/Omar.png")

            # changing circle color
            im = circle
            im = im.convert("RGBA")
            color = make_col()

            data = np.array(im)
            black, lead, blue, alpha = data.T

            white_areas = (black == 255) & (blue == 255) & (lead == 255)
            data[..., :-1][white_areas.T] = color

            im2 = Image.fromarray(data)
            circle = im2
            # done

            image3 = image1.crop((280, 0, 1000, 720))
            lum_img = Image.new("L", [720, 720], 0)
            draw = ImageDraw.Draw(lum_img)
            draw.pieslice([(0, 0), (720, 720)], 0, 360, fill=255, outline="white")
            img_arr = np.array(image3)
            lum_img_arr = np.array(lum_img)
            final_img_arr = np.dstack((img_arr, lum_img_arr))
            image3 = Image.fromarray(final_img_arr)
            image3 = image3.resize((600, 600))

            image2.paste(image3, (50, 70), mask=image3)
            image2.paste(circle, (0, 0), mask=circle)
