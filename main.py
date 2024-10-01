import utils as ut
import pixel_info as pixel
import pydicom as pydicom
import numpy as np

from matplotlib import pyplot as plt
from PIL import Image
import constants as const


def main():
    paste_qr_to_dcm_test(const.AXIAL_DTI_STRAIGHT_LAST, const.QR_PNG)

# tests the pasting method for both a processed and original qr code onto a dicom image
def paste_qr_to_dcm_test(dicom_file, qr):
    dicom = pydicom.dcmread(const.AXIAL_DTI_STRAIGHT_LAST)
    # print(pixel.get_dicom_pixel_info(dicom))

    # get qr and dicom image info
    photometric_interpretation, dcm_bits_allocated, qr_color_space, qr_bitdepth = pixel.get_colorspace_bitdepth_info(dicom, qr)
    
    # convert png
    pixel.convert_8bit_to_16bit(qr)
    modified_qr_color_space, modified_qr_bitdepth = pixel.get_qr_pixel_info(const.PROCESSED_QR_PNG)
    print(f"\n modified qr \n qr_color_space: {modified_qr_color_space},\n qqr_bitdepth: {modified_qr_bitdepth}")
    
    # test the current paste method with the original png
    ut.paste_qr_to_dcm(dicom, qr, const.PROCESSED_DICOM_PNG) # we expect a transparent qr code
    
    # test current paste method with processed png
    ut.paste_qr_to_dcm(dicom, const.PROCESSED_QR_PNG, const.PROCESSED_QR_PNG_PASTED) # the qr code will be normal but the dicom all black
    
    #inspect the new dicom file
    new_dicom = pydicom.dcmread(const.PROCESSED_QR_PNG_PASTED)
    # print(pixel.get_dicom_pixel_info(new_dicom))

main()