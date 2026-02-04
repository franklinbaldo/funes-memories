import random

def generate_svg(filename):
    width = 1200
    height = 630
    bg_color = "#0a0a0a"
    accent_color = "#00ff00"

    svg_content = f'''<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
    <rect width="100%" height="100%" fill="{bg_color}"/>
    <style>
        .text {{ font-family: monospace; fill: {accent_color}; }}
        .dim {{ opacity: 0.5; }}
        .blink {{ animation: blinker 1s linear infinite; }}
        @keyframes blinker {{ 50% {{ opacity: 0; }} }}
    </style>
    '''

    # Add some random "code" lines background
    for i in range(20):
        y = 30 + i * 30
        line_len = random.randint(10, 80)
        chars = "".join(random.choice("010101010101  PROCESS  MEMORY  ALLOC  FREE  ") for _ in range(line_len))
        opacity = random.uniform(0.1, 0.3)
        svg_content += f'<text x="20" y="{y}" class="text" style="opacity:{opacity}; font-size: 14px;">{chars}</text>\n'

    # Main Title
    svg_content += f'''
    <text x="50%" y="45%" dominant-baseline="middle" text-anchor="middle" class="text" font-size="64" font-weight="bold">FUNES REMEMBERS</text>
    <text x="50%" y="55%" dominant-baseline="middle" text-anchor="middle" class="text dim" font-size="32">MEMORY SYSTEM: ONLINE</text>
    '''

    # Cursor
    svg_content += f'<rect x="860" y="335" width="20" height="40" fill="{accent_color}" class="blink" />' # Approximate position

    # Border
    svg_content += f'<rect x="10" y="10" width="{width-20}" height="{height-20}" fill="none" stroke="{accent_color}" stroke-width="2"/>'

    svg_content += '</svg>'

    with open(filename, 'w') as f:
        f.write(svg_content)

if __name__ == "__main__":
    generate_svg("src/assets/hero-memory.svg")
