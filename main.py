import utils as ut
import pydicom as pydicom
import numpy as np
from PIL import Image

dcm_sample_axial = "dcm_samples/002_S_0413/Axial_3TE_T2_STAR/2019-08-27_09_39_37.0/S868724/ADNI_002_S_0413_MR_Axial_3TE_T2_STAR__br_raw_20190828115108623_47_S868724_I1221049.dcm"
dcm_sample_field = "dcm_samples/002_S_0413/Field_Mapping/2019-08-27_09_39_37.0/S868733/ADNI_002_S_0413_MR_Field_Mapping__br_raw_20190828115108376_21_S868733_I1221062.dcm"
qr_img_jpeg = "/Users/edgararrizon/Downloads/ONMD QR Code/VistaQR-website-www_onemednet_com-2.jpeg"
modified_dcm = '/Users/edgararrizon/code/DICOMn/output.dcm'

output_dcm = 'output2.dcm'


def main():
    # load dicom file
    axial_dicom_file = pydicom.dcmread(dcm_sample_axial)
    dcm_axial_field_data = ut.extract_dcm_img_attributes(axial_dicom_file)
    print(dcm_axial_field_data)
    
    # fiel_dicom_file = pydicom.dcmread(dcm_sample_field)
    # dcm_fiel_field_data = ut.extract_dcm_img_attributes(fiel_dicom_file)
    # print(dcm_fiel_field_data)


main()