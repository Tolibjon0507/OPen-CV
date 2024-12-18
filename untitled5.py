# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Em2ylgLrWwaiD3QRIojlvr8cFir2Cj9C
"""

import cv2
import matplotlib.pyplot as plt
from google.colab import files

# Rasmni yuklash
uploaded = files.upload(photo_2024-12-17_21-45-51.jpg)

# Yuklangan rasm nomini olish
image_name = next(iter(uploaded))

# Rasmni yuklash
image = cv2.imread(image_name)

# Rasmni oq-qora formatga o'tkazish
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Oq-qora rasmni saqlash
cv2.imwrite('oq_qora_rasm.jpg', gray_image)

# Rasmni ko'rsatish
plt.imshow(gray_image, cmap='gray')
plt.axis('off')  # O'qni o'chirish
plt.show()