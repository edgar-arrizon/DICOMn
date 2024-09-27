import utils as ut
import pixel_info as pixel
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

processed_qr_pasted = "modified_dcm/processed_qr_dicom_png.dcm"


def main():
    # read the file 
    dicom = pydicom.dcmread(dcm_sample_axial)
    print(pixel.get_dicom_pixel_info(dicom))

    # get qr and dicom image info
    photometric_interpretation, dcm_bits_allocated, qr_color_space, qr_bitdepth = pixel.get_colorspace_bitdepth_info(dicom, qr_img_png)
    
    # convert png
    pixel.convert_8bit_to_16bit(qr_img_png)
    modified_qr_color_space, modified_qr_bitdepth = pixel.get_qr_pixel_info(modified_qr_png)
    print(f"\n modified qr \n qr_color_space: {modified_qr_color_space},\n qqr_bitdepth: {modified_qr_bitdepth}")
    
    # test the current paste method with the original png
    ut.paste_qr_to_dcm(dicom, qr_img_png, modified_dicom_png) # we expect a transparent qr code in the top right corner
    
    # test current paste method with processed png
    ut.paste_qr_to_dcm(dicom, modified_qr_png, processed_qr_pasted)
    
    #inspect the new dicom file
    new_dicom = pydicom.dcmread(modified_dicom_png)
    print(pixel.get_dicom_pixel_info(new_dicom))

    # paste the qr to dicom

main()