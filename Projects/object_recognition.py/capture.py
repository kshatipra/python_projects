import cv2
import os
import pickle

object_data = {}

def extract_features(img):
    orb = cv2.ORB_create()
    keypoints, descriptors = orb.detectAndCompute(img, None)
    return descriptors

cam = cv2.VideoCapture(0)

object_name = input("Enter object name: ")

features = []

print("Press 's' to save frame for feature extraction.")
print("Press 'q' to finish capturing.")

while True:
    ret, frame = cam.read()
    cv2.imshow("Capture Object", frame)
    key = cv2.waitKey(1)

    if key == ord('s'):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        desc = extract_features(gray)
        if desc is not None:
            features.append(desc)
            print(f"[+] Saved frame. Total: {len(features)}")
    elif key == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()

# Save features
if os.path.exists("object_data.pkl"):
    with open("object_data.pkl", "rb") as f:
        object_data = pickle.load(f)

object_data[object_name] = features

with open("object_data.pkl", "wb") as f:
    pickle.dump(object_data, f)

print(f"[✓] Saved {len(features)} features for '{object_name}'")
