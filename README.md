STEP-BY-STEP GUIDE: INSTALL, RUN, AND SAVE HAND POSTURES
========================================================

1) CREATE A CLEAN PYTHON ENVIRONMENT (recommended)
---------------------------------------------------
Windows (PowerShell):
    python -m venv venv
    .\venv\Scripts\activate

macOS / Linux (bash or zsh):
    python3 -m venv venv
    source venv/bin/activate

If you prefer Conda:
    conda create -n handpose python=3.10 -y
    conda activate handpose


2) INSTALL DEPENDENCIES WITH PIP
--------------------------------
Make sure you are inside the folder that contains requirements.txt, then run:
    pip install -r requirements.txt

If you don’t have that file, install manually:
    pip install mediapipe opencv-python numpy


3) (OPTIONAL) VERIFY YOUR CAMERA WORKS
--------------------------------------
Create a quick_cam_test.py file with this code:

    import cv2
    cap = cv2.VideoCapture(0)
    ok, frame = cap.read()
    print("Camera OK?", ok, "Frame shape:", None if not ok else frame.shape)
    cap.release()

Run it:
    python quick_cam_test.py
If it prints "Camera OK? True" the webcam is ready.


4) RUN THE POSTURE APPLICATION
------------------------------
Start the main program:
    python posture_recognition.py


5) REGISTER (SAVE) A POSTURE
----------------------------
1. Place your RIGHT hand in front of the camera in the posture you want to save.
2. Press the key S.
3. Look at your terminal — it will ask:
       Enter name for this posture:
4. Type a name (for example: peace) and press ENTER.
5. You’ll see confirmation such as:
       ✅ Registered posture 'peace' and saved.
6. This posture is now stored automatically in the file:
       registered_postures.json


6) RECOGNIZE A SAVED POSTURE (LIVE)
-----------------------------------
- Keep your right hand in view of the camera.
- The app continuously computes your current finger angles.
- It compares those angles to all saved postures.
- If every finger angle differs by less than 10%, it considers it a match.
- If several postures pass that test, it picks the one with the smallest Euclidean distance and shows its name on screen.


7) ADD MORE POSTURES
--------------------
Repeat step 5 for each new hand shape you want (press S again, enter another name).


8) EXIT THE APP
---------------
Press the ESC key in the video window.


9) WHERE YOUR DATA IS SAVED
---------------------------
All registered postures are stored in:
    registered_postures.json
You can copy or share this file between computers to reuse your saved gestures.


10) COMMON TROUBLESHOOTING
--------------------------
• Black or empty window → try using VideoCapture(1) instead of (0) or close other apps using the camera.
• No right-hand detection → ensure good lighting and show your palm facing the camera.
• Laggy video → close CPU-heavy applications; the script runs on CPU only.
• macOS: grant Terminal/IDE camera permission in System Settings → Privacy & Security.
• Import errors → run pip install -r requirements.txt again inside the activated environment.


QUICK COMMANDS RECAP
--------------------
Windows PowerShell:
    python -m venv venv
    .\venv\Scripts\activate
    pip install -r requirements.txt
    python posture_recognition.py

macOS / Linux:
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python posture_recognition.py

-----------------------------------------------------------
Once you press S and name a posture, it is automatically saved
to registered_postures.json and will be recognized live on the
next run of the program.
-----------------------------------------------------------
