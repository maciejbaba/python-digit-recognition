print("Initializing...")
print("Importing modules...")

print("Importing cv2...")
import cv2

print("Importing numpy...")
import numpy as np

print("Importing os...")
import os

print("Importing matplotlib...")
import matplotlib.pyplot as plt

print("Importing tensorflow...")
import tensorflow as tf

print("Modules imported successfully")


# # uncomment this to train the model

# print("Declaring mnist...")
# mnist = tf.keras.datasets.mnist

# print("Loading mnist data...")
# (x_train, y_train), (x_test, y_test) = mnist.load_data()

# x_train = tf.keras.utils.normalize(x_train, axis=1)
# x_test = tf.keras.utils.normalize(x_test, axis=1)

# model = tf.keras.models.Sequential()
# model.add(tf.keras.layers.Flatten(input_shape=(28, 28)))
# model.add(tf.keras.layers.Dense(units=128, activation=tf.nn.relu))
# model.add(tf.keras.layers.Dense(units=128, activation=tf.nn.relu))
# model.add(tf.keras.layers.Dense(units=10, activation=tf.nn.softmax))


# model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
# model.fit(x_train, y_train, epochs=3)

# model.save('digits.model')


# uncomment this to test the model

# model = tf.keras.models.load_model("digits.model")

# loss, accuracy = model.evaluate(x_test, y_test)

# print(loss)
# print(accuracy)


print("Loading model...")
model = tf.keras.models.load_model("digits.model")

print("Declaring image_number...")
image_number = 1

print("Starting loop...")
while os.path.isfile(f"images/{image_number}.png"):
    print("Trying to read image...")
    try:
        print(f"Reading image {image_number}...")
        img = cv2.imread(f"images/{image_number}.png")[:, :, 0]
        img = np.invert(np.array([img]))
        prediction = model.predict(img)
        print(f"The number is probably a {np.argmax(prediction)}")
        plt.imshow(img[0], cmap=plt.cm.binary)
        plt.show()
    except:
        print("Error, something went wrong")
    finally:
        print("Incrementing image_number...")
        image_number += 1

print("Done")
print("Exiting...")
