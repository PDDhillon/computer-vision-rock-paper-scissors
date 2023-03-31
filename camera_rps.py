import cv2
import random
from keras.models import load_model
import numpy as np
import time

def get_user_prediction():    
    labels = ["Rock", "Scissors", "Paper", "Nothing"]
    model = load_model('keras_model.h5')
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    start = time.time()
    prediction = None
    while not (int(time.time() - start) == 3):
        ret, frame = cap.read()
        normalised_image = get_normalised_image(frame)
        data[0] = normalised_image
        prediction = model.predict(data)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
                    
    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
    print(f"you chose {labels[np.argmax(prediction[0])]}")

def get_normalised_image(frame):
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        return (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image

def get_computer_choice():
    options = ["Rock","Paper","Scissors"]
    return random.choice(options)

def get_winner(computer_choice,user_choice):
    if(computer_choice == user_choice):
      print("It is a tie!")
      return [0,0]
    if(computer_choice == "Rock"):
      if(user_choice == "Paper"):
        print("You won!")
        return [0,1]
      else:
        print("You lost")
        return [1,0]
    elif(computer_choice == "Paper"):
      if(user_choice == "Rock"):
        print("You lost")
        return [1,0]
      else:
        print("You won!")
        return [0,1]
    elif(computer_choice == "Scissors"):
      if(user_choice == "Rock"):
        print("You won!")
        return [0,1]
      else:
        print("You lost")
        return [1,0]  
      
def get_prediction():
    rounds_played = 5
    current_round = 0
    computer_wins = 0
    user_wins = 0

    while(current_round < rounds_played and computer_wins < 3 and user_wins < 3):    
        user_choice = get_user_prediction()
        computer_choice = get_computer_choice()
        winner = get_winner(computer_choice, user_choice)
        if(np.argmax(winner) == 0):
            computer_wins += 1
        elif(np.argmax(winner) == 1):
            user_wins += 1
        current_round += 1
        print("Computer: ", computer_wins, " User:", user_wins)  
