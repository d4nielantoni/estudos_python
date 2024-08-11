from PIL import Image
import os
from reportlab.pdfgen import canvas

def images_to_pdf(image_folder, output_pdf):
    try:
        image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('jpeg', 'jpg'))]

        if not image_files:
            raise FileNotFoundError("Nenhum arquivo JPEG encontrado na pasta especificada.")

        image_files.sort()

        pdf_canvas = canvas.Canvas(output_pdf)

        for image_file in image_files:

            image_path = os.path.join(image_folder, image_file)
            image = Image.open(image_path)

            image_width, image_height = image.size

            pdf_canvas.setPageSize((image_width, image_height))

            pdf_canvas.drawImage(image_path, 0, 0, image_width, image_height)

            pdf_canvas.showPage()

        pdf_canvas.save()

        print("PDF criado com sucesso!")

    except FileNotFoundError as fnf_error:
        print(f"Erro: {fnf_error}")
    except Exception as e:
        print(f"Ocorreu um erro ao criar o PDF: {e}")

image_folder = r"C:\Users\danie\Downloads\ilovepdf_pages-to-jpg" 
output_pdf = r"C:\Users\danie\Downloads\vinos.pdf"  # Nome do arquivo PDF de saída
images_to_pdf(image_folder, output_pdf)
