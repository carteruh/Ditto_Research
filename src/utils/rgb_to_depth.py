import os

from PIL import Image
from transformers import pipeline


def RGB_to_depth(src_dir, dst_dir):
    # Create the destination directory if it doesn't exist
    os.makedirs(dst_dir, exist_ok=True)

    # Load the depth estimation pipeline
    pipe = pipeline(task="depth-estimation", model="depth-anything/Depth-Anything-V2-Small-hf")

    # Iterate over the images in the source directory
    for idx, filename in enumerate(sorted(os.listdir(src_dir))):
        # Filter for image files (assuming PNG, JPG, etc.)
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(src_dir, filename)

            # Load the image
            image = Image.open(img_path)

            # Inference to get the depth image
            depth = pipe(image)["depth"]

            # Construct the depth image filename
            depth_filename = f"{str(idx).zfill(4)}_depth.png"
            depth_path = os.path.join(dst_dir, depth_filename)

            # Save the depth image
            depth.save(depth_path)
            print(f"Saved depth image: {depth_path}")

def main(root, states, stages):
    for state in states:
        for stage in stages:
            src_dir = os.path.join(root, state, stage)
            dst_dir = os.path.join(src_dir, 'depth_images')

            RGB_to_depth(src_dir=src_dir, dst_dir=dst_dir)

if __name__ == '__main__':
    object_name = 'Knife'
    object_id = '101217'
    states = ['start', 'end']
    stages = ['train', 'val', 'test']
    root = f'/media/qil/DATA/Carter_Articulated_Objects/Ditto/data/sapien_example/{object_name}/{object_id}'

    main(root, states, stages)
