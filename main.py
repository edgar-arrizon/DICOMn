from matplotlib import pyplot as plt
import utils as ut
import pydicom as pydicom
from PIL import Image
import numpy as np

dcm_sample_axial = "dcm_samples/002_S_0413/Axial_3TE_T2_STAR/2019-08-27_09_39_37.0/S868724/ADNI_002_S_0413_MR_Axial_3TE_T2_STAR__br_raw_20190828115108611_52_S868724_I1221049.dcm" # requires normalization, QR is transparent
field_mapping = "dcm_samples/002_S_0413/Field_Mapping/2019-08-27_09_39_37.0/S868733/ADNI_002_S_0413_MR_Field_Mapping__br_raw_20190828115108376_21_S868733_I1221062.dcm" # requires normalization, QR image is black
last_field = "dcm_samples/002_S_0413/Field_Mapping/2019-08-27_09_39_37.0/S868733/ADNI_002_S_0413_MR_Field_Mapping__br_raw_20190828115137030_7_S868733_I1221062.dcm" # requires normalization, QR image is black
axial_dti_straight_last = "dcm_samples/019_S_4367/Axial_DTI_straight/2019-05-20_10_18_12.0/S826089/ADNI_019_S_4367_MR_Axial_DTI_straight_br_raw_20190523093020094_4076_S826089_I1167911.dcm" # doesnt require normalization for qr to print

qr_img_tiff = "/Users/edgararrizon/Downloads/ONMD QR Code/VistaQR-website-www_onemednet_com-2.tiff"
qr_img_png = "/Users/edgararrizon/Downloads/ONMD QR Code/VistaQR-website-www_onemednet_com-2.png"
qr_img_jpeg = "/Users/edgararrizon/Downloads/ONMD QR Code/VistaQR-website-www_onemednet_com-2.jpeg"

modified_dicom_jpeg = "modified_dcm/modified_dicom_jpeg.dcm"
modified_dicom_tiff = "modified_dcm/modified_dicom_tiff.dcm"
modified_dicom_png = "modified_dcm/modified_dicom_png.dcm"

def main():
    # read the file 
    axial_dcm_file = pydicom.dcmread(dcm_sample_axial)
    # dcm_color_space, dcm_bits, qr_color_space, qr_bitdepth = get_colorspace_bitdepth_info(axial_dcm_file, "modified_qr/qr_16bit.png")
    dcm_color_space, dcm_bits, qr_color_space, qr_bitdepth = get_colorspace_bitdepth_info(axial_dcm_file, "modified_qr/qr_16bit.tiff")
    print("Color Space:", dcm_color_space)
    print("DICOM Bit Depth:", dcm_bits)
    print("QR Code Color Space:", qr_color_space)
    print("QR Code Bit Depth:", qr_bitdepth)

    # convert_8bit_to_16bit(qr_img_tiff)


def get_colorspace_bitdepth_info(dcm_path, qr_path):
    # Gather the Color Space and BitDepth for the DICOM FILE and the QR code
    photometric_interpretation = dcm_path.PhotometricInterpretation 
    dcm_bits_allocated = dcm_path.BitsAllocated

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

    return photometric_interpretation, dcm_bits_allocated, qr_color_space, qr_bitdepth


def convert_8bit_to_16bit(img_path):
    
    # Load the 8-bit image
    img_8bit = Image.open(img_path).convert('L')  # Ensure RGB mode
    plt.imshow(img_8bit)
    plt.show()

    # Convert to NumPy array
    img_array_8bit = np.array(img_8bit)
    # Convert to 16-bit (adjust scaling factor as needed)
    scaling_factor = 255 / img_array_8bit.max()  # Adjust scaling factor
    img_array_16bit = (img_array_8bit * scaling_factor).astype(np.uint16)

    # # Convert back to PIL Image
    img_16bit = Image.fromarray(img_array_16bit)
    plt.imshow(img_16bit)
    plt.show()

    # Save the 16-bit image
    img_16bit.save("modified_qr/qr_16bit.tiff")

main()