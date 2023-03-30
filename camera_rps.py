import cv2
from keras.models import load_model
import numpy as np

def get_prediction():
    model = load_model('keras_model.h5')
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    ret, frame = cap.read()
    normalised_image = get_normalised_image(frame)
    data[0] = normalised_image
    prediction = model.predict(data)
    cv2.imshow('frame', frame)
    # Press q to close the window
    print(prediction)
                
    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

    return prediction

def get_normalised_image(frame):
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        return (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image

get_prediction()