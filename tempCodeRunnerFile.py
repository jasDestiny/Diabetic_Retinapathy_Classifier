import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import os


# Disable scientific notation for clarity
np.set_printoptions(suppress=True)
model = tensorflow.keras.models.load_model('keras_model.h5')
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
image = Image.open('./3/0dc8d25b3f69.png')

# resizing the image to be 224x224 and then cropping from the center
size = (224, 224)
image = ImageOps.fit(image, size, Image.ANTIALIAS)
image_array = np.asarray(image)
normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
data[0] = normalized_image_array
prediction = model.predict(data)

# defining output class labels
output_labels = {
    0: "No_DR",
    1: "Mild",
    2: "Moderate",
    3: "Severe",
    4: "Proliferate"
}

# results
os.system("cls")
print("Results: \n")
counter = 0
for i in np.nditer(prediction):
    print(output_labels[counter], i*100, "%")
    counter += 1
