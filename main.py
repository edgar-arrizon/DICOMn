import utils as ut
import pixel_info as pixel
import pydicom as pydicom

import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

# some dicom samples, more in the dcm_samples folder
dcm_sample_axial = "dcm_samples/002_S_0413/Axial_3TE_T2_STAR/2019-08-27_09_39_37.0/S868724/ADNI_002_S_0413_MR_Axial_3TE_T2_STAR__br_raw_20190828115108611_52_S868724_I1221049.dcm" 
field_mapping = "dcm_samples/002_S_0413/Field_Mapping/2019-08-27_09_39_37.0/S868733/ADNI_002_S_0413_MR_Field_Mapping__br_raw_20190828115108376_21_S868733_I1221062.dcm" 
last_field = "dcm_samples/002_S_0413/Field_Mapping/2019-08-27_09_39_37.0/S868733/ADNI_002_S_0413_MR_Field_Mapping__br_raw_20190828115137030_7_S868733_I1221062.dcm" 
axial_dti_straight_last = "dcm_samples/019_S_4367/Axial_DTI_straight/2019-05-20_10_18_12.0/S826089/ADNI_019_S_4367_MR_Axial_DTI_straight_br_raw_20190523093020094_4076_S826089_I1167911.dcm" 

# the QR codes to modify
qr_tiff = "ONMD QR Code/VistaQR-website-www_onemednet_com-2.tiff"
qr_png = "ONMD QR Code/VistaQR-website-www_onemednet_com-2.png"
qr_jpeg = "ONMD QR Code/VistaQR-website-www_onemednet_com-2.jpeg"

# the processed QR code
processed_qr_tiff = "processed_qr/qr_16bit.tiff"
processed_qr_png = "processed_qr/qr_16bit.png"

# the processed dicom (with original QR code)
processed_dicom_jpeg = "processed_dcm/qr_dicom_jpeg.dcm"
processed_dicom_tiff = "processed_dcm/qr_dicom_tiff.dcm"
processed_dicom_png = "processed_dcm/qr_dicom_png.dcm"

# the processed dicom (with processed original QR code)
processed_qr_png_pasted = "processed_dcm/processed_qr_png_dicom.dcm"

def main():
    paste_qr_to_dcm_test(dcm_sample_axial, qr_png)

# tests the pasting method for both a processed and original qr code onto a dicom image
def paste_qr_to_dcm_test(dicom_file, qr):
    dicom = pydicom.dcmread(dcm_sample_axial)
    # print(pixel.get_dicom_pixel_info(dicom))

    # get qr and dicom image info
    photometric_interpretation, dcm_bits_allocated, qr_color_space, qr_bitdepth = pixel.get_colorspace_bitdepth_info(dicom, qr)
    
    # convert png
    pixel.convert_8bit_to_16bit(qr)
    modified_qr_color_space, modified_qr_bitdepth = pixel.get_qr_pixel_info(processed_qr_png)
    print(f"\n modified qr \n qr_color_space: {modified_qr_color_space},\n qqr_bitdepth: {modified_qr_bitdepth}")
    
    # test the current paste method with the original png
    ut.paste_qr_to_dcm(dicom, qr, processed_dicom_png) # we expect a transparent qr code
    
    # test current paste method with processed png
    ut.paste_qr_to_dcm(dicom, processed_qr_png, processed_qr_png_pasted) # the qr code will be normal but the dicom all black
    
    #inspect the new dicom file
    new_dicom = pydicom.dcmread(processed_qr_png_pasted)
    # print(pixel.get_dicom_pixel_info(new_dicom))

main()