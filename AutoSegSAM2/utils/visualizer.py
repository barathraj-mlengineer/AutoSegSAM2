import numpy as np
import cv2

def overlay_mask(image, mask):
    mask = cv2.resize(mask, (image.shape[1], image.shape[0]))
    colored_mask = np.zeros_like(image)
    colored_mask[:, :, 1] = mask * 255
    return cv2.addWeighted(image, 1, colored_mask, 0.5, 0)
