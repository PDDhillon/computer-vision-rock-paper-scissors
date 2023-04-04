import cv2
from keras.models import load_model
import numpy as np
import time
from Classes.game import Game
from Classes.user import User
from Classes.computer import Computer

def get_user_prediction(cap):    
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    previous = time.time()
    TIMER = 3
    while (TIMER >= 0):
        current = time.time()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        ret, frame = cap.read()
        cv2.putText(frame,str(TIMER), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_4)
        normalised_image = get_normalised_image(frame)
        data[0] = normalised_image
        cv2.imshow('frame', frame)
        if current-previous >= 1:
                previous = current
                TIMER = TIMER-1 
    return data

def get_normalised_image(frame):
        resized_frame = cv2.resize(cv2.flip(frame, 1), (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        return (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
      
def get_prediction():    
    labels = ["Rock", "Paper", "Scissors", "Nothing"]
    user = User(0,'Nothing')
    computer = Computer(0,'Nothing')
    game = Game(5,3)
    model = load_model('keras_model.h5')
    cap = cv2.VideoCapture(0)    
    while True:  
        if game.is_game_over(user._wins, computer._wins) == True:
           break        
        data = get_user_prediction(cap)        
        prediction = model.predict(data)        
        user._current_choice = labels[np.argmax(prediction[0])]   
        result = game.get_winner(user._current_choice, computer.get_choice())    
        game.played_rounds += 1
        print("******************************")
        print("Round: ", game.played_rounds)
        print("USR: ", user._current_choice)
        print("CPU: ", computer._current_choice)
        if(np.argmax(result) == 0):
            user._wins += 1
            print("USR wins!")
        elif(np.argmax(result) == 1):
            computer._wins += 1
            print("CPU wins")
        print("USR ", user._wins, " - ", computer._wins, " CPU")
        print("******************************")    
    cap.release()
    cv2.destroyAllWindows()