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

modified_dicom_jpeg = "modified_dcm/modified_dicom_jpeg.dcm"
modified_dicom_tiff = "modified_dcm/modified_dicom_tiff.dcm"
modified_dicom_png = "modified_dcm/modified_dicom_png.dcm"

def main():
    # read the file 
    ut.paste_qr_to_dcm(dcm_sample_axial, qr_img_tiff, modified_dicom_tiff)
    ut.paste_qr_to_dcm(dcm_sample_axial, qr_img_png, modified_dicom_png)

    dcm_color_space, dcm_bits, qr_color_space, qr_bitdepth = qr.get_colorspace_bitdepth_info(axial_dcm_file, "modified_qr/qr_16bit.tiff")
    print("Color Space:", dcm_color_space)
    print("DICOM Bit Depth:", dcm_bits)
    print("QR Code Color Space:", qr_color_space)
    print("QR Code Bit Depth:", qr_bitdepth)

    # qr.convert_8bit_to_16bit(qr_img_tiff)


main()