import numpy as np
from PIL import Image
import random
import os

def disrupt_image(image_path, block_size=10, disruption_factor=0.05):
    """
    Disrupts an image by changing random blocks of pixels.
    """
    image = Image.open(image_path)
    image_array = np.array(image)

    height, width, channels = image_array.shape
    num_blocks = int((width // block_size) * (height // block_size) * disruption_factor)

    for _ in range(num_blocks):
        x = random.randint(0, width - block_size)
        y = random.randint(0, height - block_size)
        random_color = np.random.randint(0, 256, (block_size, block_size, channels), dtype=np.uint8)
        image_array[y:y + block_size, x:x + block_size] = random_color

    disrupted_image = Image.fromarray(image_array)
    return disrupted_image


def swap_blocks(image_path, block_size=10, num_swaps=100):
    """
    Swaps random blocks in the image.
    """
    image = Image.open(image_path)
    image_array = np.array(image)

    height, width, channels = image_array.shape

    for _ in range(num_swaps):
        x1 = random.randint(0, width - block_size)
        y1 = random.randint(0, height - block_size)
        x2 = random.randint(0, width - block_size)
        y2 = random.randint(0, height - block_size)

        # Extract the blocks
        block1 = image_array[y1:y1 + block_size, x1:x1 + block_size].copy()
        block2 = image_array[y2:y2 + block_size, x2:x2 + block_size].copy()

        # Swap the blocks
        image_array[y1:y1 + block_size, x1:x1 + block_size] = block2
        image_array[y2:y2 + block_size, x2:x2 + block_size] = block1

    swapped_image = Image.fromarray(image_array)
    return swapped_image


image_path = 'mona_lisa.jpeg'
block_size = random.randint(1, 50)

disruption_factor = round(random.randint(1, 10) / random.randint(2, 10), 2)
new_image = disrupt_image(image_path, block_size, disruption_factor)
output_filename = f"{image_path.split(".")[0]}_b{block_size}_d{disruption_factor}.jpg"

# num_swap = random.randint(1, 100)
# new_image = swap_blocks(image_path, block_size, num_swap)
# output_filename = f"{image_path}_b{block_size}_s{num_swap}.jpg"

new_image.show()

# save picture
output_dir="output"
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, output_filename)
new_image.save(output_path)