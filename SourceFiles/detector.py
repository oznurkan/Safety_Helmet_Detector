import torch
import cv2

class Detector:
    def __init__(self, weightsFilename, confidenceLower=0.85):
        self.confidenceLower = confidenceLower
        self.labels = ["head", "helmet", "person"]
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model = torch.hub.load('ultralytics/yolov5', 'custom', path=weightsFilename, force_reload=True)        
        self.model = self.model.to(self.device).eval()

    def detect(self, frame):
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.model(frame_rgb)

        locations = []
        for result in results.xyxy[0]:
            bbox = result[0:4].cpu().numpy()
            start_x, start_y, end_x, end_y = bbox.astype(int)
            class_id = int(result[5])
            label = self.labels[class_id]
            confidence = float(result[4])

            locations.append([start_x, start_y, end_x, end_y, label, confidence])

        return locations
    
    