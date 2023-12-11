# common/utils.py
import os
from pdf2image import convert_from_path

def generate_pdf_thumbnail(pdf_path, thumbnail_path, width=100, height=100):
    try:
        # Convert the first page of the PDF to an image
        images = convert_from_path(pdf_path, size=(width, height), first_page=0, last_page=1)
        
        # Save the image as the thumbnail
        thumbnail_file = f'{os.path.splitext(os.path.basename(pdf_path))[0]}_thumbnail.png'
        thumbnail_path = os.path.join(thumbnail_path, thumbnail_file)
        images[0].save(thumbnail_path, 'PNG')
    except Exception as e:
        print(f"Error generating PDF thumbnail: {e}")

# pdf_path = "/home/khanza/Projects/Final Project WAB/colearn/media/materials/uploads/09_Multi_Attribute_Decision_Making.pdf"
# thumbnail_path = "/home/khanza/Projects/Final Project WAB/colearn/media/materials/thumbnails"
# generate_pdf_thumbnail(pdf_path, thumbnail_path)