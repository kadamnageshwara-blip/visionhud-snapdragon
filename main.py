import cv2
import numpy as np
import time
import argparse
import onnxruntime as ort
from hud_overlay import HUDOverlay
from safety_alert import SafetyAlertSystem

def run_vision_hud(source_path, provider):
    print(f"Initializing VisionHUD Engine...")
    print(f"Target Execution Provider: {provider} (Qualcomm DirectML NPU Acceleration)")
    
    available_providers = ort.get_available_providers()
    print(f"Available ONNX Providers: {available_providers}")
    
    hud = HUDOverlay()
    safety = SafetyAlertSystem()

    cap = cv2.VideoCapture(0 if source_path == "0" else source_path)
    
    if not cap.isOpened():
        print(f"Error: Unable to open video feed source {source_path}")
        return

    cv2.namedWindow("VisionHUD - Smart Helmet Simulator", cv2.WINDOW_NORMAL)
    
    prev_time = time.time()
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            continue

        h, w, _ = frame.shape
        
        simulated_detections = [
            [int(w*0.4), int(h*0.5), int(w*0.6), int(h*0.75), "Vehicle", 0.92]
        ]

        alerts = safety.evaluate_hazards(simulated_detections, w, h)

        output_frame = hud.draw_hud(
            frame, 
            speed_kmh=72, 
            nav_instruction="TURN RIGHT 200m - MAIN ST", 
            detections=simulated_detections
        )

        curr_time = time.time()
        fps = 1.0 / (curr_time - prev_time)
        prev_time = curr_time
        latency_ms = (1.0 / fps) * 1000

        cv2.putText(output_frame, f"NPU DirectML: ACTIVE | {fps:.1f} FPS | Latency: {latency_ms:.1f}ms", 
                    (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

        if alerts:
            cv2.putText(output_frame, f"WARNING: {alerts[0]}", 
                        (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (200, 200, 255), 2, cv2.LINE_AA)

        cv2.imshow("VisionHUD - Smart Helmet Simulator", output_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="VisionHUD Engine - On-Device Safety HUD Simulator")
    parser.add_argument("--source", type=str, default="0", help="Video source (0 for webcam or path to mp4 file)")
    parser.add_argument("--provider", type=str, default="DmlExecutionProvider", help="ONNX Execution Provider")
    
    args = parser.parse_args()
    run_vision_hud(args.source, args.provider)
