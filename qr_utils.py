from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def get_dicom_pixel_info(dicom):
    info = {
        "photometric_interpretation": dicom.get("PhotometricInterpretation", None),
        "bits_allocated": dicom.get("BitsAllocated", None),
        "bits_stored": dicom.get("BitsStored", None),
        "pixel_value_range": (
            dicom.get("SmallestImagePixelValue", None),
            dicom.get("LargestImagePixelValue", None),
        ),
        "transfer_syntax": dicom.file_meta.TransferSyntaxUID.name if dicom.file_meta else None,
        "modality": dicom.get("Modality", None),
        "pixel_spacing": dicom.get("PixelSpacing", (None, None)),
    }
    return info

def get_colorspace_bitdepth_info(dicom, qr_path):
    # Gather the Color Space and BitDepth for the DICOM FILE and the QR code
    dicom_info = get_dicom_pixel_info(dicom)
    color_space = dicom_info["photometric_interpretation"]
    bit_depth = dicom_info["bits_allocated"]
    
    qr = Image.open(qr_path)
    qr_color_space = qr.mode
    qr_bitdepth = qr.info.get('qr_bitdepth', None)

    # if we cant infer the qr_bitdepth we need to check the min max values
    if qr_bitdepth == None:
        qr_image_data = np.array(qr)
        min_value = qr_image_data.min()
        max_value = qr_image_data.max()

        if min_value >= 0 and max_value <= 255:
            qr_bitdepth = 8
        else:
            qr_bitdepth = 16  # Assuming 16-bit based on common image formats

    print(f"photometric_interpretation : {color_space},\n dcm_bits_allocated: {bit_depth},\n qr_color_space: {qr_color_space},\n qr_bitdepth: {qr_bitdepth}")

    return dicom_info["photometric_interpretation"], dicom_info["bits_allocated"], qr_color_space, qr_bitdepth


# def convert_8bit_to_16bit(img_path):
    
#     # Load the 8-bit image
#     img_8bit = Image.open(img_path).convert('L')

#     # Convert to NumPy array
#     img_array_8bit = np.array(img_8bit)

#     # Convert to 16-bit (adjust scaling factor as needed)
#     scaling_factor = 255 / img_array_8bit.max()  # Adjust scaling factor
#     img_array_16bit = (img_array_8bit * scaling_factor).astype(np.uint16)

#     # # Convert back to PIL Image
#     img_16bit = Image.fromarray(img_array_16bit)
#     plt.imshow(img_16bit)
#     plt.show()

#     img_16bit.save("modified_qr/qr_16bit.png")
