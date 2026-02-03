import os
from PIL import Image, ImageDraw, ImageFont

# Create assets directory if it doesn't exist
if not os.path.exists('assets'):
    os.makedirs('assets')

# Define emojis as simple colored shapes with text
emojis = ['dog.png', 'cat.png', 'bird.png', 'fish.png', 'lion.png', 'panda.png', 'tiger.png', 'bear.png']
colors = [(255, 200, 0), (255, 100, 100), (100, 200, 255), (100, 255, 100), 
          (255, 150, 0), (0, 0, 0), (255, 150, 100), (150, 100, 50)]
labels = ['🐶', '🐱', '🐦', '🐠', '🦁', '🐼', '🐯', '🐻']

# Create images
for filename, color, label in zip(emojis, colors, labels):
    img = Image.new('RGB', (120, 120), color=color)
    draw = ImageDraw.Draw(img)
    
    # Try to use a large font for the emoji
    try:
        font = ImageFont.truetype("arial.ttf", 80)
    except:
        font = ImageFont.load_default()
    
    # Draw the label centered
    bbox = draw.textbbox((0, 0), label, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (120 - text_width) // 2
    y = (120 - text_height) // 2
    draw.text((x, y), label, fill='white', font=font)
    
    img.save(os.path.join('assets', filename))
    print(f"Created {filename}")

print("Assets created successfully!")
