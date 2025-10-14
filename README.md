# ⚙️ Installation & Setup

Follow these steps to install and run the Right-Hand Posture Recognition system.

---

## 🧩 1️⃣ Create a Clean Python Environment

**Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\activate
```

**macOS / Linux (bash / zsh):**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Conda (alternative):**
```bash
conda create -n handpose python=3.10 -y
conda activate handpose
```

---

## 📦 2️⃣ Install Dependencies

If you already have a `requirements.txt` file:
```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install mediapipe opencv-python numpy
```

---

## 🎥 3️⃣ Optional: Test Your Camera

Create a file named `quick_cam_test.py`:

```python
import cv2
cap = cv2.VideoCapture(0)
ok, frame = cap.read()
print("Camera OK?", ok, "Frame shape:", None if not ok else frame.shape)
cap.release()
```

Then run it:
```bash
python quick_cam_test.py
```

If you see “Camera OK? True”, your webcam is working.

---

## 🚀 4️⃣ Run the Posture Recognition App

```bash
python posture_recognition.py
```

---

## ✋ 5️⃣ Register a New Posture

1. Hold your **right hand** in front of the camera.  
2. Press **S** on the keyboard.  
3. In the terminal, type a name for the posture (example: `peace`).  
4. Press **Enter**.  

Example:
```
Detected angles (radians): [0.52 0.14 0.31 0.46 0.77]
Enter name for this posture: peace
✅ Registered posture 'peace' and saved.
```

This will automatically save your posture to:
```
registered_postures.json
```

---

## 🔍 6️⃣ Recognition Mode (Live Detection)

Once postures are saved, the system automatically:
- Computes your current finger angles.
- Compares them to all saved postures.
- Checks if **all 5 angles differ by <10%**.
- If multiple postures match, it picks the **closest one using Euclidean distance**.

Example live output:
```
Detected posture: peace (distance = 0.037)
```

---

## ➕ 7️⃣ Add More Postures

Repeat Step 5 — press **S**, type a new name (e.g., “fist”), and it will be added to the JSON file automatically.

---

## ❌ 8️⃣ Exit the Program

Press **ESC** in the webcam window to quit.

---

## 💾 9️⃣ Where Your Data Is Saved

All registered postures are stored in:
```
registered_postures.json
```
You can back it up or share it between machines.

---

## 🛠️ 10️⃣ Troubleshooting

| Issue | Possible Fix |
|--------|---------------|
| 🕳 Black / empty window | Try `VideoCapture(1)` or close other apps using the camera. |
| ✋ No right-hand detection | Ensure good lighting and keep hand clearly visible. |
| 🐢 Laggy video | Close other programs; runs best on CPU-only environments. |
| 🔒 macOS permissions | Allow Terminal / IDE camera access in System Settings → Privacy & Security. |
| ⚠️ Import errors | Re-run `pip install -r requirements.txt` inside your active environment. |

---

## ⚡ Quick Copy Commands

**Windows PowerShell**
```powershell
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python posture_recognition.py
```

**macOS / Linux**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python posture_recognition.py
```

---

Once you press **S** and type a name,
that posture is automatically saved and recognized live the next time you run the program.
