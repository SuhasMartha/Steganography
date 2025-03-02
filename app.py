import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from cryptography.fernet import Fernet
import os

# Generate a unique key for encryption
SECRET_KEY = Fernet.generate_key()
CIPHER = Fernet(SECRET_KEY)

class SteganographyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Secure Image Steganography")
        self.root.geometry("600x500")
        self.root.configure(bg="#2C3E50")

        self.image_path = None

        # UI Components
        tk.Label(root, text="Secure Image Steganography", font=("Arial", 18, "bold"), fg="white", bg="#2C3E50").pack(pady=10)

        self.img_label = tk.Label(root, text="No Image Selected", fg="white", bg="#2C3E50", font=("Arial", 12))
        self.img_label.pack(pady=5)

        tk.Button(root, text="Select Image", command=self.load_image, bg="#1ABC9C", fg="white", font=("Arial", 12)).pack(pady=5)

        tk.Label(root, text="Enter Secret Message:", fg="white", bg="#2C3E50", font=("Arial", 12)).pack(pady=5)
        self.msg_entry = tk.Entry(root, width=50)
        self.msg_entry.pack(pady=5)

        tk.Button(root, text="Hide Message", command=self.encode_message, bg="#3498DB", fg="white", font=("Arial", 12)).pack(pady=5)
        tk.Button(root, text="Extract Message", command=self.decode_message, bg="#E74C3C", fg="white", font=("Arial", 12)).pack(pady=5)

        self.output_label = tk.Label(root, text="", fg="yellow", bg="#2C3E50", font=("Arial", 12))
        self.output_label.pack(pady=5)

    def load_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("PNG Images", "*.png")])
        if self.image_path:
            img = Image.open(self.image_path)
            img.thumbnail((250, 250))
            img = ImageTk.PhotoImage(img)
            self.img_label.config(image=img, text="", compound="top")
            self.img_label.image = img

    def encode_message(self):
        if not self.image_path:
            messagebox.showerror("Error", "Please select an image first!")
            return
        
        secret_message = self.msg_entry.get()
        if not secret_message:
            messagebox.showerror("Error", "Message cannot be empty!")
            return

        encrypted_message = CIPHER.encrypt(secret_message.encode()).decode() + "##"
        binary_message = ''.join(format(ord(char), '08b') for char in encrypted_message)
        
        image = cv2.imread(self.image_path)
        rows, cols, _ = image.shape
        data_index = 0
        message_length = len(binary_message)

        for row in range(rows):
            for col in range(cols):
                pixel = image[row, col]
                for color in range(3):
                    if data_index < message_length:
                        pixel[color] = pixel[color] & ~1 | int(binary_message[data_index])
                        data_index += 1
                    else:
                        break

        output_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
        if output_path:
            cv2.imwrite(output_path, image)
            messagebox.showinfo("Success", f"Message hidden successfully!\nSaved as: {output_path}")

    def decode_message(self):
        if not self.image_path:
            messagebox.showerror("Error", "Please select an image first!")
            return

        image = cv2.imread(self.image_path)
        binary_message = ""

        for row in image:
            for pixel in row:
                for color in pixel[:3]:
                    binary_message += str(color & 1)

        chars = [binary_message[i:i+8] for i in range(0, len(binary_message), 8)]
        extracted_message = ''.join(chr(int(char, 2)) for char in chars)
        extracted_message = extracted_message.split("##")[0]

        try:
            decrypted_message = CIPHER.decrypt(extracted_message.encode()).decode()
            self.output_label.config(text=f"🔓 Extracted Message: {decrypted_message}")
        except:
            messagebox.showerror("Error", "Decryption failed! Incorrect or corrupted message.")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = SteganographyApp(root)
    root.mainloop()
