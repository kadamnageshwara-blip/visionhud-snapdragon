import cv2
import numpy as np

class HUDOverlay:
    """
    Renders minimalist, non-intrusive white HUD navigation vector elements
    optimized to prevent cognitive overload for motorcycle riders.
    """
    def __init__(self):
        self.color_white = (255, 255, 255)
        self.color_alert = (200, 200, 255)

    def draw_hud(self, frame, speed_kmh=68, nav_instruction="KEEP STRAIGHT 500m", detections=None):
        overlay = frame.copy()
        height, width, _ = frame.shape

        speed_text = f"{speed_kmh} KM/H"
        cv2.putText(overlay, speed_text, (width // 2 - 60, 40), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, self.color_white, 2, cv2.LINE_AA)
        
        cx, cy = width // 2, height // 2
        cv2.line(overlay, (cx - 15, cy), (cx - 5, cy), self.color_white, 1, cv2.LINE_AA)
        cv2.line(overlay, (cx + 5, cy), (cx + 15, cy), self.color_white, 1, cv2.LINE_AA)
        cv2.line(overlay, (cx, cy - 15), (cx, cy - 5), self.color_white, 1, cv2.LINE_AA)
        cv2.line(overlay, (cx, cy + 5), (cx, cy + 15), self.color_white, 1, cv2.LINE_AA)

        cv2.putText(overlay, f"^ {nav_instruction}", (width // 2 - 120, height - 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, self.color_white, 1, cv2.LINE_AA)

        if detections:
            for det in detections:
                x1, y1, x2, y2, label, score = det
                length = 15
                cv2.line(overlay, (x1, y1), (x1 + length, y1), self.color_white, 2)
                cv2.line(overlay, (x1, y1), (x1, y1 + length), self.color_white, 2)
                cv2.line(overlay, (x2, y2), (x2 - length, y2), self.color_white, 2)
                cv2.line(overlay, (x2, y2), (x2, y2 - length), self.color_white, 2)
                
                cv2.putText(overlay, f"{label} {int(score*100)}%", (x1, y1 - 8),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.4, self.color_white, 1, cv2.LINE_AA)

        return cv2.addWeighted(overlay, 0.85, frame, 0.15, 0)
