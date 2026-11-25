#!/usr/bin/env python3
"""Draw entry.png: the world news of Wednesday 25 November 2026 in one image.

Build tool only (needs Pillow). The graded program is main.py, which copies
the finished entry.png using just the standard library, exactly like the
kit's starter. Run:  python3 make_image.py

Stories, all reported on 25 Nov 2026:
  * Iran's Guards say two tankers hit mines in the Strait of Hormuz
  * Ukraine confirms its naval drones sank a Russian warship off Libya
  * COP31 climate talks collapse in Antalya over fossil-fuel wording
  * Huawei convicted in a US court; Nvidia slides, Nikkei falls 2.8%
  * Pakistan's first astronaut reaches China's space station
  * About 20 hostages freed in a Cartagena supermarket, Colombia
Ticker: Senegal restored as Africa Cup champions; Australia-Solomon
Islands security treaty; France orders Sarkozy case to trial.
"""
import math

from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (247, 243, 234)
INK = (22, 24, 28)
RED = (178, 34, 42)
BLUE = (24, 74, 128)
TEAL = (14, 116, 110)
GOLD = (176, 124, 16)
GREY = (88, 92, 98)
WHITE = (255, 255, 255)
SKY = (219, 233, 244)

SANS_B = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
SERIF_B = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"


def f(path, size):
    return ImageFont.truetype(path, size)


def wrap(d, text, font, maxw):
    words, lines, cur = text.split(), [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if d.textlength(trial, font=font) <= maxw:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def block(d, xy, text, font, fill, maxw, leading=1.14):
    x, y = xy
    for line in wrap(d, text, font, maxw):
        d.text((x, y), line, font=font, fill=fill)
        y += int(font.size * leading)
    return y


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# ---- masthead -------------------------------------------------------------
d.rectangle([0, 0, W, 56], fill=RED)
d.text((28, 13), "THE  WORLD  IN  ONE  PICTURE", font=f(SANS_B, 29), fill=WHITE)
r = "ONE DAY  -  SIX STORIES  -  EVERY CONTINENT"
d.text((W - 28 - d.textlength(r, font=f(SANS_B, 18)), 19), r,
       font=f(SANS_B, 18), fill=WHITE)
d.text((28, 66), "25 NOVEMBER 2026", font=f(SERIF_B, 72), fill=INK)
d.text((30, 146), "Wednesday  -  the day's world news, summed up in a single image",
       font=f(SANS, 24), fill=GREY)
d.line([28, 184, W - 28, 184], fill=INK, width=4)

# ---- hero: Hormuz (y 196..438) --------------------------------------------
d.rectangle([28, 196, W - 28, 438], fill=SKY)
d.rectangle([28, 196, W - 28, 438], outline=BLUE, width=3)
d.text((52, 210), "MIDDLE EAST  -  TOP STORY", font=f(SANS_B, 21), fill=RED)
block(d, (52, 238), "TANKERS HIT MINES IN THE STRAIT OF HORMUZ",
      f(SANS_B, 42), INK, 920)
block(d, (52, 336), "Iran's Revolutionary Guards say two tankers struck mines "
      "in the strait - fears grow for energy shipping and oil supplies.",
      f(SANS, 23), (40, 44, 52), 620)
# tanker, right side
d.polygon([(690, 372), (946, 372), (922, 402), (714, 402)], fill=(52, 58, 66))
d.rectangle([724, 344, 892, 372], fill=(120, 128, 138))
d.rectangle([852, 320, 888, 344], fill=(52, 58, 66))
d.rectangle([742, 326, 830, 344], fill=RED)
d.text((762, 328), "OIL", font=f(SANS_B, 15), fill=WHITE)
for mx, my in [(706, 330), (946, 300)]:
    d.ellipse([mx - 17, my - 17, mx + 17, my + 17], fill=INK)
    for a in range(0, 360, 45):
        d.line([mx, my, mx + int(26 * math.cos(math.radians(a))),
                my + int(26 * math.sin(math.radians(a)))], fill=INK, width=4)
for wy in (412, 426):
    for wx in range(52, W - 80, 64):
        d.arc([wx, wy, wx + 38, wy + 14], 0, 180, fill=BLUE, width=3)

# ---- four panels (y 452..800): 2 x 2 ---------------------------------------
panels = [
    (28, 452, 500, 622, TEAL, "EUROPE  -  WAR AT SEA",
     "UKRAINE SAYS IT SANK A RUSSIAN WARSHIP",
     "Kyiv confirms naval drones sank the corvette Merkury off Benghazi, Libya."),
    (524, 452, 996, 622, GOLD, "CLIMATE  -  ANTALYA, TURKIYE",
     "COP31 TALKS COLLAPSE",
     "Oil producers block any mention of phasing out fossil fuels; talks end in failure."),
    (28, 636, 500, 806, BLUE, "TECHNOLOGY  -  UNITED STATES",
     "HUAWEI CONVICTED IN U.S.; NVIDIA SLIDES",
     "Brooklyn jury convicts Huawei; Nvidia falls about 7% and Japan's Nikkei drops 2.8%."),
    (524, 636, 996, 806, (112, 62, 150), "SPACE  -  PAKISTAN / CHINA",
     "PAKISTAN'S FIRST ASTRONAUT IN ORBIT",
     "Pakistan's first astronaut reaches China's space station - a national first."),
]
for x0, y0, x1, y1, colour, kicker, head, body in panels:
    d.rectangle([x0, y0, x1, y1], fill=WHITE, outline=colour, width=3)
    d.rectangle([x0, y0, x1, y0 + 34], fill=colour)
    d.text((x0 + 16, y0 + 7), kicker, font=f(SANS_B, 17), fill=WHITE)
    y = block(d, (x0 + 16, y0 + 46), head, f(SANS_B, 27), INK, x1 - x0 - 32)
    block(d, (x0 + 16, y + 4), body, f(SANS, 20), (52, 56, 62), x1 - x0 - 32)

# ---- bottom panel: Colombia (y 820..928) -----------------------------------
d.rectangle([28, 820, 996, 928], fill=(253, 238, 214), outline=GOLD, width=3)
d.text((52, 834), "AMERICAS  -  COLOMBIA", font=f(SANS_B, 19), fill=RED)
block(d, (52, 860), "CARTAGENA HOSTAGES FREED", f(SANS_B, 32), INK, 560)
d.text((640, 838), "About 20 people held in a", font=f(SANS, 21), fill=(52, 56, 62))
d.text((640, 866), "supermarket are freed -", font=f(SANS, 21), fill=(52, 56, 62))
d.text((640, 894), "no hostage casualties.", font=f(SANS, 21), fill=(52, 56, 62))

# ---- ticker (y 942..996) ----------------------------------------------------
d.rectangle([0, 942, W, H], fill=INK)
ticker = ("ALSO TODAY:  Senegal restored as Africa Cup champions by the Court of "
          "Arbitration for Sport  -  Australia and Solomon Islands sign a security "
          "treaty  -  France orders the Sarkozy corruption case to trial")
block(d, (28, 954), ticker, f(SANS_B, 19), WHITE, W - 56, leading=1.25)

img.save("entry.png", optimize=True)
print("entry.png written", img.size)
