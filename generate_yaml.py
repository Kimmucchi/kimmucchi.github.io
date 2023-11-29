import os
import yaml
from datetime import datetime

def generate_yaml_for_gifs(folder_path):
    metadata_list = []

    for filename in os.listdir(folder_path):
        if filename.endswith(".gif"):
            gif_path = os.path.join(folder_path, filename)

            # Use filename (without extension) as the default title
            title = os.path.splitext(filename)[0]

            # Set a default description
            description = "Default description for " + title

            # Get the current date as the default date
            date = datetime.now().strftime("%Y-%m-%d")

            metadata = {
                "image": filename,
                "title": title,
                "description": description,
                "date": date
                # Add more fields as needed
            }

            metadata_list.append(metadata)

    output_path = os.path.join(folder_path, "img_metadata.yml")

    with open(output_path, "w") as yaml_file:
        yaml.dump(metadata_list, yaml_file, default_flow_style=False)

if __name__ == "__main__":
    folder_path = input("Enter the path to the folder containing GIFs: ")
    generate_yaml_for_gifs(folder_path)
