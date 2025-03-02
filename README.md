# 🛡️ Secure Data Hiding in Image Using Steganography

## 📜 Project Overview
This project implements **Image Steganography** using the **Least Significant Bit (LSB) technique**, allowing users to **hide secret messages inside images** without any noticeable change. It includes **AES encryption** for enhanced security and provides both a **GUI-based desktop app** and a **Flask-based web version**.

---

## 🎯 **Features**
✅ **Hide & Extract Secret Messages** – Steganography using the LSB method  
✅ **AES Encryption** – Secures messages before embedding  
✅ **User-Friendly GUI** – Built using Tkinter   
✅ **Maintains Image Quality** – No noticeable distortion  
✅ **Supports PNG Images** – Lossless image processing  

---

## 🖥️ **Installation & Setup**
### **🔹 Step 1: Install Dependencies**
Make sure you have **Python 3.x** installed. Then, run:  
```bash
pip install numpy opencv-python pillow cryptography flask tkinter
```

### **🔹 Step 2: Clone the Repository**
```bash
git clone https://github.com/suhasmartha/steganography.git
cd steganography
```

### **🔹 Step 3: Run the GUI Version**
To start the **Tkinter GUI**:
```bash
python gui_steganography.py
```

### **🔹 Step 4: Run the Flask Web Version**
To launch the **Flask Web App**:
```bash
python app.py
```
Then, open `http://127.0.0.1:5000/` in your browser.

---

## 🛠️ **Usage**
### **📌 Step 1: Load an Image**
- Select a PNG image to hide your message.

### **📌 Step 2: Enter Secret Message**
- Type the message you want to hide.

### **📌 Step 3: Hide the Message**
- Click "Hide Message" to embed the message in the image.
- Save the **stego-image** (which contains the hidden text).

### **📌 Step 4: Extract the Message**
- Load the **stego-image** and click "Extract Message" to reveal the hidden text.

---

## 📷 **Screenshots**
### 🔹 **Step 1: Select an Image**
![Step 1](https://via.placeholder.com/400x250?text=Select+Image)

### 🔹 **Step 2: Enter Secret Message**
![Step 2](https://via.placeholder.com/400x250?text=Enter+Secret+Message)

### 🔹 **Step 3: Hide the Message**
![Step 3](https://via.placeholder.com/400x250?text=Hide+Message)

### 🔹 **Step 4: Extract the Message**
![Step 4](https://via.placeholder.com/400x250?text=Extract+Message)

---

## 📜 **Technology Stack**
- **Programming Language:** Python
- **Libraries:** OpenCV, NumPy, PIL (Pillow), Cryptography
- **GUI Framework:** Tkinter
- **Steganography Method:** Least Significant Bit (LSB)

---

## 🔐 **Security & Encryption**
- **AES-256 Encryption** ensures that even if the stego-image is analyzed, the message remains unreadable without the correct decryption key.
- The **LSB method** ensures minimal changes in the image, making detection difficult.

---

## 📌 **To-Do & Future Scope**
🔹 **Add Steganography for Video & Audio Files**  
🔹 **Implement AI-based Steganalysis Resistance**  
🔹 **Enhance UI/UX with Modern Design**  
🔹 **Add Password-Protected Message Extraction**  

---

## 🤝 **Contributing**
Want to contribute? Follow these steps:
1. Fork this repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-branch
   ```
3. Commit your changes:
   ```bash
   git commit -m "Added a new feature"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-branch
   ```
5. Open a **Pull Request**.

---

## 📝 **License**
This project is open-source under the **MIT License**.

---

## 📩 **Contact & Support**
💡 **Developed by:** [Suhas Martha](https://github.com/suhasmartha)  
📌 **GitHub Repo:** [Steganography App](https://github.com/suhasmartha/steganography)  
📧 **Email:** *suhasmartha@gmail.com*  

---

🚀 **Star this repo** if you found it useful! **Happy Coding!** 😊  
