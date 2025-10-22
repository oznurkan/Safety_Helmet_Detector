import cv2

def drawArea(img, locations):
    for loc in locations:
        x1, y1, x2, y2, label, confidence = loc
        if confidence >= 0.60:
            if label == "helmet":
                color = [0, 255, 0]  # Green color for helmet
            elif label == "head":
                color = [0, 0, 255]  # Red color for head and person
            elif label == "person":
                color = [255, 0, 0]  # Blue color for other labels
            cv2.rectangle(img, (x1, y1), (x2, y2), color, 3)  #bounding-box
            cv2.putText(img, "{}: {:.2f}".format(label, confidence), (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2) #label and confidence çizim üzerinde çizilir.
        else:
            continue

def alertController(locations):
    helmet_detected = True
    for loc in locations:
        if loc[4] == "helmet":
            helmet_detected = False
        elif loc[4] == "head":
            helmet_detected = True
            break

    return helmet_detected

