import matplotlib.pyplot as plt
import numpy as np
import pydicom
from PIL import Image, ImageDraw

# def access_tags(dcm):
    # Access tags by keyword
    # patient_name = dcm.PatientName
    # study_date = dcm.StudyDate

    # Access tags by tag number (group, element)
    # institution_name = dcm[0x0008, 0x0080].value  # Institution Name\
    # print(patient_name, study_date, institution_name)

def display_image(dcm):
    if hasattr(dcm, 'pixel_array'):
        # Extract the pixel array
        image = dcm.pixel_array
        
        # Plot the image using Matplotlib
        plt.imshow(image, cmap='gray')
        plt.show()
    else:
        print("This DICOM file does not contain image data.")

def add_qr_to_dicom(dicom_path, qr_image_path, output_path, position="top-right"):
    # Step 1: Load the DICOM image
    dcm = pydicom.dcmread(dicom_path)
    
    if hasattr(dcm, 'pixel_array'):
        # Convert DICOM pixel array to an image
        dicom_image = Image.fromarray(dcm.pixel_array)

        # Step 2: Load the QR code image
        qr_image = Image.open(qr_image_path).convert("L")  # Convert to grayscale if necessary

        # Step 3: Resize QR code if necessary to fit within the DICOM image
        qr_image = qr_image.resize((76, 76))  # Adjust size as needed

        # Step 4: Place QR code in the specified position
        dicom_width, dicom_height = dicom_image.size
        qr_width, qr_height = qr_image.size

        if position == "bottom-right":
            x = dicom_width - qr_width
            y = dicom_height - qr_height
        elif position == "bottom-left":
            x = 0
            y = dicom_height - qr_height
        elif position == "top-right":
            x = dicom_width - qr_width
            y = 0
        elif position == "top-left":
            x = 0
            y = 0
        else:
            raise ValueError("Invalid position specified.")

        # Overlay QR code onto the DICOM image
        dicom_image.paste(qr_image, (x, y))
        
        # Verifying the image was overlayed correctly
        plt.imshow(dicom_image, cmap='gray')
        plt.show()

        # Step 5: Save the modified DICOM image
        modified_array = np.array(dicom_image)
        dcm.PixelData = modified_array.tobytes()

        # Save to output path
        dcm.save_as(output_path)
        print(f"QR code added to DICOM and saved to {output_path}")
    else:
        print("This DICOM file does not contain image data.")