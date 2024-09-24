import utils as ut
import pydicom as pydicom
import numpy as np
from PIL import Image

dcm_sample_axial = "dcm_samples/002_S_0413/Axial_3TE_T2_STAR/2019-08-27_09_39_37.0/S868724/ADNI_002_S_0413_MR_Axial_3TE_T2_STAR__br_raw_20190828115108611_52_S868724_I1221049.dcm" # requires normalization, QR is transparent
field_mapping = "dcm_samples/002_S_0413/Field_Mapping/2019-08-27_09_39_37.0/S868733/ADNI_002_S_0413_MR_Field_Mapping__br_raw_20190828115108376_21_S868733_I1221062.dcm" # requires normalization, QR image is black
last_field = "dcm_samples/002_S_0413/Field_Mapping/2019-08-27_09_39_37.0/S868733/ADNI_002_S_0413_MR_Field_Mapping__br_raw_20190828115137030_7_S868733_I1221062.dcm" # requires normalization, QR image is black
axial_dti_straight_last = "dcm_samples/019_S_4367/Axial_DTI_straight/2019-05-20_10_18_12.0/S826089/ADNI_019_S_4367_MR_Axial_DTI_straight_br_raw_20190523093020094_4076_S826089_I1167911.dcm" # doesnt require normalization for qr to print
qr_img_jpeg = "/Users/edgararrizon/Downloads/ONMD QR Code/VistaQR-website-www_onemednet_com-2.jpeg"
modified_dcm = 'output.dcm'

output_dcm = 'modified_dcm/output.dcm'

def main():
    ut.past_qr_to_dcm(axial_dti_straight_last, qr_img_jpeg, output_dcm)

main()