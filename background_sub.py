import numpy as np
import matplotlib.pyplot as plt
import cv2


def play_videos(original_frames, background_frames, foreground_frames, num_frames):
    plt.figure(figsize=(15, 5))
    for idx in range(num_frames):
        orig = original_frames[idx]
        bg = background_frames[idx].astype(np.uint8)
        fg = foreground_frames[idx]

        # Create the subplot
        plt.clf()
        plt.subplot(1, 3, 1)
        plt.imshow(cv2.cvtColor(orig, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB
        plt.title("Original Frame")
        plt.axis("off")

        plt.subplot(1, 3, 2)
        plt.imshow(cv2.cvtColor(bg, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB
        plt.title("Background Frame")
        plt.axis("off")

        plt.subplot(1, 3, 3)
        plt.imshow(cv2.cvtColor(fg, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB
        plt.title("Foreground Frame")
        plt.axis("off")
        plt.pause(1e-2)

    plt.show()


cap = cv2.VideoCapture("Video_008.avi")
frames = list()
scale = 1/2

if not cap.isOpened():
    print("Error opening the video file")

while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        frames.append(frame)
        #frames.append(cv2.resize(frame, (int(frame.shape[0] * scale), int(frame.shape[1] * scale))))

    else:
        break

cap.release()
imgs = np.array(frames)
height = imgs.shape[1]
width = imgs.shape[2]
channels = imgs.shape[3]

# Create the data matrices of images
m = height * width * channels
n = imgs.shape[0] - 1
X = np.array([frame.flatten() for frame in frames[:-1]]).T
X_prime = np.array([frame.flatten() for frame in frames[1:]]).T

# Preform singular value decomposition(SVD) on X
U, S, Vt = np.linalg.svd(X, full_matrices=False)

# Retain only the modes with significant singular values
threshold = 1e-4
r = np.sum(S > threshold)
U_r = U[:, :r]
S_r = np.diag(S[:r])
Vt_r = Vt[:r, :]

# Compute the DMD matrix
A_tilda = U_r.T @ X_prime @ Vt_r.T @ np.linalg.inv(S_r)

# Eigen decomposition of the A_tilda matrix
eigenvalues, eigenvectors = np.linalg.eig(A_tilda)

# Compute the DMD modes
phi = X_prime @ Vt_r.T @ np.linalg.inv(S_r) @ eigenvectors

# Identify the Background modes (Eigenvectors close to one
background_indices = np.abs(np.abs(eigenvalues) - 1) < threshold
phi_bg = phi[:, background_indices]

# Reconstruct the background
b = np.linalg.pinv(phi_bg) @ frames[0].flatten()
background_frames = list()
print("Computing background....", end="")
for i in range(len(frames)):
    bg_frame = np.real(phi_bg @ (b * (eigenvalues[background_indices] ** i)))
    background_frames.append(bg_frame.reshape(height, width, channels))
print("Completed")

# Compute the foreground by subtracting the background
foreground_frames = list()
print("Computing foreground....", end="")
for i, frame in enumerate(frames):
    fg_frame = cv2.absdiff(frame, background_frames[i].astype(np.uint8))
    foreground_frames.append(fg_frame.reshape(height, width, channels))
print("Completed")

play_videos(imgs, background_frames, foreground_frames, len(frames))
