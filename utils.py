import matplotlib.pyplot as plt
import numpy as np
import pydicom as pydicom
from PIL import Image

def add_qr_to_dicom(dicom_path, qr_image_path, output_path, position="top-right"):
    # Step 1: Load the DICOM image
    dcm = pydicom.dcmread(dicom_path)

    if hasattr(dcm, 'pixel_array'):

        #normalize the dicom pixels
        dcm_arr = dcm.pixel_array
        uint8_pixel_arr = normalize_dcm_pixel_data(dcm_arr)

        dicom_image = Image.fromarray(uint8_pixel_arr)

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

def normalize_dcm_pixel_data(dcm_arr, max_v=None, min_v=None, show=False):
    
    if max_v: houns_field_max = max_v
    else: houns_field_max = np.max(dcm_arr)

    if min_v: houns_field_max = min_v
    else: houns_field_min = np.min(dcm_arr)

    houns_field_min =   np.min(dcm_arr)
    houns_field_max =   np.max(dcm_arr)
    houns_field_range = houns_field_max - houns_field_min

    dcm_arr[dcm_arr < houns_field_min] = houns_field_min
    dcm_arr[dcm_arr > houns_field_max] = houns_field_max

    #generates values between 0 - 1
    normalized_dcm_arr = (dcm_arr - houns_field_min) / houns_field_range
    normalized_dcm_arr *= 255
    uint8_img = np.int8(normalized_dcm_arr)

    if show:
        pillow_img = Image.fromarray(uint8_img)
        pillow_img.show()

    return uint8_img