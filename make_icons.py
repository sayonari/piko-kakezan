# アイコン生成: uv run --with pillow make_icons.py
from PIL import Image, ImageDraw
N = 64
img = Image.new('RGB', (N, N), '#1d2b53')
d = ImageDraw.Draw(img)
def cube(x, y, s, base, hi, lo, dark):
    d.rectangle([x, y, x+s-1, y+s-1], fill=dark)
    d.rectangle([x+1, y+1, x+s-2, y+s-2], fill=lo)
    d.rectangle([x+1, y+1, x+s-3, y+s-3], fill=base)
    d.line([x+1, y+1, x+s-3, y+1], fill=hi); d.line([x+1, y+1, x+1, y+s-3], fill=hi)
ROWS = [('#ff77a8', '#ffc2d9', '#b3537a', '#401d2b'), ('#29adff', '#c4f0ff', '#1868c0', '#06204a'),
        ('#00e436', '#a8f5bc', '#00a026', '#003a0e'), ('#ffa300', '#ffe28c', '#d45f00', '#4a1d00')]
for r, col in enumerate(ROWS):
    d.rounded_rectangle([7, 9 + r*12, 56, 19 + r*12], radius=3, fill='#2b3a6b')
    for j in range(4):
        cube(10 + j*11 + (0 if j < 2 else 0), 10 + r*12, 9, *col)
for s, name in [(512, 'icon-512.png'), (192, 'icon-192.png'), (180, 'icon-180.png')]:
    img.resize((s, s), Image.NEAREST).save(name)
