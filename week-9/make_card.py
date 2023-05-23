import bpy
import sys
import argparse
from pathlib import Path

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('character_folder', type=Path)
parser.add_argument('--color', default="red")

argv = sys.argv
print(f"args: {argv}")
argv = argv[argv.index("--") + 1:]  # get all args after "--"
args = parser.parse_args(argv)

print(f"Color: {args.color}")

image_path = Path(args.character_folder, f"blender_{args.character_folder.stem}.png")
print(f"Blenderoading {image_path}")
image = bpy.data.images['placeholder']
image.filepath = str(image_path.resolve())
image.reload()
print(image)

print("Blender: Rendering")
bpy.context.scene.render.filepath = str(Path(args.character_folder, f"card_{args.character_folder.stem}.png").resolve())
bpy.ops.render.render(write_still=True)

print("Blender: Finished!")