# Background Subtraction with Dynamic Mode Decomposition (DMD)

This project showcases a video processing pipeline for separating background and foreground using Dynamic Mode Decomposition (DMD). By leveraging linear algebra techniques like Singular Value Decomposition (SVD) and eigen decomposition, this approach efficiently extracts background frames and computes foreground dynamics.

## Features

- **Dynamic Mode Decomposition (DMD):** Employs DMD to decompose video frames into background and foreground components.
- **Custom Background Reconstruction:** Uses eigen decomposition to identify background modes and reconstruct frames.
- **Foreground Isolation:** Subtracts background from original frames to highlight dynamic objects.
- **Interactive Visualization:** Displays original, background, and foreground frames side-by-side for comparison.

## Requirements

To run the project, ensure you have the following dependencies:

- **Python**
- Libraries:
  - `numpy`
  - `matplotlib`
  - `opencv-python`

## Workflow

1. **Video Loading:** Read video frames from the input file (`Video_008.avi`).
2. **Preprocessing:** Flatten frames to create data matrices for processing.
3. **SVD Decomposition:** Perform Singular Value Decomposition on the frame matrix.
4. **DMD Matrix Construction:** Build the reduced-rank DMD matrix.
5. **Eigen Decomposition:** Extract eigenvalues and eigenvectors to identify background modes.
6. **Background Reconstruction:** Reconstruct background frames using the identified modes.
7. **Foreground Computation:** Subtract background from original frames to isolate dynamic elements.
8. **Visualization:** Display original, background, and foreground frames using `matplotlib`.

## Applications

This project is applicable in scenarios such as:

- Video surveillance for detecting moving objects.
- Preprocessing for computer vision tasks requiring clean backgrounds.
- Motion analysis in scientific and industrial videos.

## Example

The project processes an input video (`Video_008.avi`), reconstructs the background, and isolates the foreground. It then visualizes the results and offers an intuitive understanding of video dynamics.

---

Feel free to explore and adapt this code for your video analysis and processing needs!

More information about the algrithm is avaiable here: https://doi.org/10.1007/s10851-022-01068-0
