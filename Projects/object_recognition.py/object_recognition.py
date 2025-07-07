import cv2
import pickle
import numpy as np
import pyttsx3

# Load features
with open("object_data.pkl", "rb") as f:
    object_data = pickle.load(f)

orb = cv2.ORB_create()
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
tts = pyttsx3.init()

def extract_features(img):
    _, descriptors = orb.detectAndCompute(img, None)
    return descriptors

def recognize_object(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    desc = extract_features(gray)
    if desc is None:
        return "No match"
    
    best_match = None
    best_score = 0

    for label, features in object_data.items():
        for f in features:
            matches = bf.match(desc, f)
            score = len(matches)
            if score > best_score:
                best_score = score
                best_match = label

    if best_score > 10:  # Threshold
        return best_match
    return "Unknown"

cam = cv2.VideoCapture(0)

spoken = ""

while True:
    ret, frame = cam.read()
    obj = recognize_object(frame)
    cv2.putText(frame, f"Looks like: {obj}", (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 200, 0), 2)
    cv2.imshow("Show & Learn", frame)

    if obj != spoken and obj != "Unknown":
        tts.say(f"That is a {obj}")
        tts.runAndWait()
        spoken = obj

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
