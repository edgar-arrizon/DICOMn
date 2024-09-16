import matplotlib.pyplot as plt

def access_tags(dcm):
    # Access tags by keyword
    patient_name = dcm.PatientName
    study_date = dcm.StudyDate
    
    # Access tags by tag number (group, element)
    institution_name = dcm[0x0008, 0x0080].value  # Institution Name\
    # print(patient_name, study_date, institution_name)

def display_image(dcm):
    if hasattr(dcm, 'pixel_array'):
        # Extract the pixel array
        image = dcm.pixel_array
        
        # Plot the image using Matplotlib
        plt.imshow(image, cmap='gray')
        plt.show()
    else:
        print("This DICOM file does not contain image data.")
