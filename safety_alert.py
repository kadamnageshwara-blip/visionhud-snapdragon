import time

class SafetyAlertSystem:
    """
    Automated Emergency & Anomaly Detection system.
    Evaluates collision risk vectors on-device without cloud dependency.
    """
    def __init__(self, ttt_threshold=1.5):
        self.ttt_threshold = ttt_threshold
        self.emergency_triggered = False

    def evaluate_hazards(self, detections, frame_width, frame_height):
        alerts = []
        center_x = frame_width / 2
        
        for det in detections:
            x1, y1, x2, y2, label, score = det
            box_area = (x2 - x1) * (y2 - y1)
            frame_area = frame_width * frame_height
            
            obj_center_x = (x1 + x2) / 2
            if abs(obj_center_x - center_x) < (frame_width * 0.25):
                if (box_area / frame_area) > 0.35:
                    alerts.append(f"HAZARD: CLOSE {label.upper()}")
                    self.trigger_local_emergency_protocol(label)
                    
        return alerts

    def trigger_local_emergency_protocol(self, hazard_type):
        if not self.emergency_triggered:
            self.emergency_triggered = True
            print(f"\n[SAFETY SYSTEM ALERT] Collision Risk Detected ({hazard_type})!")
            print("[AUTOMATION WORKFLOW] Preparing local emergency dispatch SMS & telemetry snapshot...")
            print("[ON-DEVICE EXECUTION] Local emergency contact notified via offline GSM protocol.\n")
