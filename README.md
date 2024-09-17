# DICOM Functionality Repository

This repository is currently dedicated to practicing and learning how to work with DICOM files. Over time, it will evolve into a project that isolates specific DICOM functionality, focusing on de-identification and post-processing tools, including watermarking.

## Current Status

At the moment, this repo serves as a sandbox for experimenting with DICOM file handling, utilizing Python and the `pydicom` library. As I ramp up, I'll be working on:

- Basic DICOM file reading and manipulation
- Experimenting with common operations like extracting metadata and visualizing images

## Next Steps

### Project Goals

The project will focus on isolating and refining DICOM functionality, including:

1. **De-identification (Deid)**:
   - Redacting sensitive DICOM tags to comply with privacy standards (e.g., HIPAA).

2. **Watermark Functionality**:
   - Adding a post-processing step to insert watermarks on DICOM images.
   - Handling image data stored in DICOM wrappers, which can vary significantly in format (including potentially corrupted or unsupported formats).

### Key Challenges

- **Error Handling**: Since DICOM is a wrapper format, the image data inside can be of various types and formats, potentially leading to edge cases and errors. Careful handling and testing will be crucial.
  
- **Test Suite**: Developing a robust test suite to ensure functionality across various DICOM image formats and resolutions.

### Reference Files

The project will reference legacy DICOM files from the `omni/broker-base/broker_base/dcm` directory. These files are being used in the de-identification process, and I'll be working to identify which parts are essential.

## Future Development

As the project progresses, the following features will be added:

- Comprehensive DICOM manipulation tools
- Watermarking functionality
- Detailed error handling for unsupported or corrupted formats
- Full test coverage for various image formats, resolutions, and color spaces

## How to Run

To get started with the repository:

1. Clone the repo:

   ```bash
   git clone <repository-url>
2. Create a virtual enviornment (venv)
   ```bash
   python3 -m venv venv
3. Activate the virtual environment
   ```bash
   source venv/bin/activate
4. Install dependencies
   ```bash
   pip install -r requirements.txt
