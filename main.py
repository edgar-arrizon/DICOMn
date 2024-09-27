import utils as ut
import qr_utils as qr
import pydicom as pydicom

import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

dcm_sample_axial = "dcm_samples/002_S_0413/Axial_3TE_T2_STAR/2019-08-27_09_39_37.0/S868724/ADNI_002_S_0413_MR_Axial_3TE_T2_STAR__br_raw_20190828115108611_52_S868724_I1221049.dcm" # requires normalization, QR is transparent
field_mapping = "dcm_samples/002_S_0413/Field_Mapping/2019-08-27_09_39_37.0/S868733/ADNI_002_S_0413_MR_Field_Mapping__br_raw_20190828115108376_21_S868733_I1221062.dcm" # requires normalization, QR image is black
last_field = "dcm_samples/002_S_0413/Field_Mapping/2019-08-27_09_39_37.0/S868733/ADNI_002_S_0413_MR_Field_Mapping__br_raw_20190828115137030_7_S868733_I1221062.dcm" # requires normalization, QR image is black
axial_dti_straight_last = "dcm_samples/019_S_4367/Axial_DTI_straight/2019-05-20_10_18_12.0/S826089/ADNI_019_S_4367_MR_Axial_DTI_straight_br_raw_20190523093020094_4076_S826089_I1167911.dcm" # doesnt require normalization for qr to print

qr_img_tiff = "/Users/edgararrizon/Downloads/ONMD QR Code/VistaQR-website-www_onemednet_com-2.tiff"
qr_img_png = "/Users/edgararrizon/Downloads/ONMD QR Code/VistaQR-website-www_onemednet_com-2.png"
qr_img_jpeg = "/Users/edgararrizon/Downloads/ONMD QR Code/VistaQR-website-www_onemednet_com-2.jpeg"

modified_qr_tiff = "modified_qr/qr_16bit.tiff"
modified_qr_png = "modified_qr/qr_16bit.png"

modified_dicom_jpeg = "modified_dcm/qr_dicom_jpeg.dcm"
modified_dicom_tiff = "modified_dcm/qr_dicom_tiff.dcm"
modified_dicom_png = "modified_dcm/qr_dicom_png.dcm"

def main():
    # read the file 
    dicom = pydicom.dcmread(dcm_sample_axial)
    photometric_interpretation, dcm_bits_allocated, qr_color_space, qr_bitdepth = qr.get_colorspace_bitdepth_info(dicom, qr_img_png)
    
    # convert qr to 16 bit, correct color space and save as new png
    # convert_8bit_to_16bit(qr_img_png)
    
    #inspect the new qr image


    # paste the qr to dicom

def convert_8bit_to_16bit(img_path):
    
    # Load the 8-bit image
    img_8bit = Image.open(img_path).convert('L')

    # Convert to NumPy array
    img_array_8bit = np.array(img_8bit)

    # Convert to 16-bit (adjust scaling factor as needed)
    scaling_factor = 255 / img_array_8bit.max()  # Adjust scaling factor
    img_array_16bit = (img_array_8bit * scaling_factor).astype(np.uint16)

    # # Convert back to PIL Image
    img_16bit = Image.fromarray(img_array_16bit, mode="I;16")
    plt.imshow(img_16bit)
    plt.show()

    img_16bit.save("modified_qr/qr_16bit_2.png", mode="I;16")

main()