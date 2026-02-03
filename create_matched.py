from PIL import Image

# Create a simple matched.png image (green checkmark background)
img = Image.new('RGB', (120, 120), color=(0, 200, 0))
img.save('other_assets/matched.png')
print("Created matched.png")
