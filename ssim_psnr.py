import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.metrics import structural_similarity as ssim
import os

def calculate_psnr(img1, img2):
    mse = np.mean((img1 - img2) ** 2)
    if mse == 0:
        return 100 #minimum mse
    PIXEL_MAX = 255.0
    return 20 * np.log10(PIXEL_MAX / np.sqrt(mse))

def compare_images(original, processed):
    original = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
    processed = cv2.cvtColor(processed, cv2.COLOR_BGR2GRAY)
    s = ssim(original, processed)
    p = calculate_psnr(original, processed)
    return s, p
folders = [] #all folders path
original_images_path = '' #original folder's path
ssim_scores = {alg: [] for alg in folders}
psnr_scores = {alg: [] for alg in folders}
for folder in folders:
    print(folder)
    for img_name in os.listdir("hybrid"):
        
        original_img_path = os.path.join(original_images_path, img_name[:-4])
        processed_img_path = os.path.join(folder, img_name)
        
        if True:
            original_img = cv2.imread(original_img_path)
            processed_img = cv2.imread(processed_img_path)
      
            if original_img is None or processed_img is None:
                pass
            elif original_img.shape == processed_img.shape:
                s, p = compare_images(original_img, processed_img)

                ssim_scores[folder].append(s)
                psnr_scores[folder].append(p)


# Plotting
plt.figure(figsize=(12, 6))
for alg in folders:
    plt.plot(ssim_scores[alg], label=f'{alg} SSIM')
plt.xlabel('Image Index')
plt.ylabel('SSIM Score')
plt.title('SSIM Scores Comparison')
plt.legend()
plt.show()

plt.figure(figsize=(12, 6))
for alg in folders:
    plt.plot(psnr_scores[alg], label=f'{alg} PSNR')
plt.xlabel('Image Index')
plt.ylabel('PSNR Score')
plt.title('PSNR Scores Comparison')
plt.legend()
plt.show()
