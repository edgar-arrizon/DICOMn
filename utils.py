import os
import csv
import numpy as np
import matplotlib.pyplot as plt
import pydicom as pydicom
from PIL import Image

def paste_qr_to_dcm(dicom, qr_image_path, output_path, position="top-right"):
    # Step 1: Load the DICOM image

    if hasattr(dicom, 'pixel_array'):
        dcm_arr = dicom.pixel_array
        dicom_image = Image.fromarray(dcm_arr)

        with open("pre.txt", "w") as f:
            print(dcm_arr, file=f)

        # Load the QR code image
        qr_image = Image.open(qr_image_path)
        # print(np.array(qr_image))

        # Resize QR code if necessary to fit within the DICOM image
        qr_image = qr_image.resize((76, 76))  # Adjust size as needed

        # Place QR code in the specified position
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
        dicom.PixelData = modified_array.tobytes()


        with open("post.txt", "w") as f:
            print(modified_array, file=f)

        # Save to output path
        dicom.save_as(output_path)
        print(f"QR code added to DICOM and saved to {output_path}")
    else:
        print("This DICOM file does not contain image data.")

def extract_dicom_attributes(directory, output_file="dicom_attributes.csv"):
    results = []
    file_count = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".dcm"):
                file_path = os.path.join(root, file)
                try:
                    ds = pydicom.dcmread(file_path)
                    attributes = {
                        "Transfer Syntax UID": ds.file_meta.TransferSyntaxUID,
                        # "Image Type": ds.ImageType,
                        "SOP Class UID": ds.SOPClassUID,
                        "Modality": ds.Modality,
                        "Photometric Interpretation": ds.PhotometricInterpretation,
                        # "Rows": ds.Rows,
                        # "Columns": ds.Columns,
                        # "Bits Allocated": ds.BitsAllocated,
                        # "Pixel Spacing": ds.PixelSpacing,
                        # "Smallest Image Pixel Value": ds.SmallestImagePixelValue,
                        # "Largest Image Pixel Value": ds.LargestImagePixelValue,
                        # "Window Center": ds.WindowCenter,
                        # "Window Width": ds.WindowWidth,
                        # "Pixel Data": ds.pixel_array
                    }
                    results.append(attributes)
                    file_count += 1
                except Exception as e:
                    print(f"Error processing file {file_path}: {e}")

    # Write results to CSV file
    fieldnames = []
    if results:
        fieldnames = list(results[0].keys())

    with open(output_file, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    # Log summary
    print(f"Processed {file_count} DICOM files.")

# normalize function for CT modality
# def normalize_ct_dicom(dcm_arr, max_v=None, min_v=None, show=False):
    
#     if max_v: houns_field_max = max_v
#     else: houns_field_max = np.max(dcm_arr)

#     if min_v: houns_field_max = min_v
#     else: houns_field_min = np.min(dcm_arr)

#     houns_field_min =   np.min(dcm_arr)
#     houns_field_max =   np.max(dcm_arr)
#     houns_field_range = houns_field_max - houns_field_min

#     dcm_arr[dcm_arr < houns_field_min] = houns_field_min
#     dcm_arr[dcm_arr > houns_field_max] = houns_field_max

#     #generates values between 0 - 1
#     normalized_dcm_arr = (dcm_arr - houns_field_min) / houns_field_range
#     normalized_dcm_arr *= 255
#     uint8_img = np.int8(normalized_dcm_arr)

#     if show:
#         pillow_img = Image.fromarray(uint8_img)
#         pillow_img.show()

#     return uint8_img

# normalization for MR modality
# def normalize_dcm_pixel_data(dcm_arr):
#     if hasattr(dcm_arr, "RescaleSlope") and hasattr(dcm_arr, "RescaleIntercept"):
#         slope = dcm_arr.RescaleSlope
#         intercept = dcm_arr.RescaleIntercept
#         normalized_dcm_arr = slope * dcm_arr + intercept
#     else:
#         # Default normalization if Rescale Slope and Intercept are not present
#         min_v = np.min(dcm_arr)
#         max_v = np.max(dcm_arr)
#         normalized_dcm_arr = (dcm_arr - min_v) / (max_v - min_v) * 255

#     # Ensure values are within 0-255 range
#     normalized_dcm_arr = np.clip(normalized_dcm_arr, 0, 255)
#     uint8_img = np.uint8(normalized_dcm_arr)

#     return uint8_img