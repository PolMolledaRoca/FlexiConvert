import argparse
import os
from PIL import Image
import pandas as pd

def images_to_pdf(image_folder, output_pdf):
    images = []
    for file in os.listdir(image_folder):
        if file.endswith(('png', 'jpg', 'jpeg')):
            img = Image.open(os.path.join(image_folder, file)).convert('RGB')
            images.append(img)
    
    if images:
        images[0].save(output_pdf, save_all=True, append_images=images[1:])
        print(f"PDF created successfully: {output_pdf}")
    else:
        print("No valid images found in the folder.")

def csv_to_json(csv_file, json_file):
    try:
        df = pd.read_csv(csv_file)
        df.to_json(json_file, orient='records', indent=4)
        print(f"CSV converted to JSON successfully: {json_file}")
    except Exception as e:
        print(f"Error converting CSV to JSON: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="File Converter: Convert images to PDF and CSV to JSON")
    parser.add_argument("-i", "--images", help="Folder containing images to convert to PDF")
    parser.add_argument("-o", "--output", help="Output PDF file name", default="output.pdf")
    parser.add_argument("-c", "--csv", help="CSV file to convert to JSON")
    parser.add_argument("-j", "--json", help="Output JSON file name", default="output.json")
    
    args = parser.parse_args()
    
    if args.images:
        images_to_pdf(args.images, args.output)
    
    if args.csv:
        csv_to_json(args.csv, args.json)
