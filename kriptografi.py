
import tkinter as tk
from tkinter import filedialog, messagebox
import numpy as np

# Implementasi Vigenere Cipher
def vigenere_encrypt(plaintext, key):
    key = key.upper()
    ciphertext = []
    for i in range(len(plaintext)):
        p = ord(plaintext[i].upper())
        k = ord(key[i % len(key)].upper())
        ciphertext.append(chr(((p + k - 2 * ord('A')) % 26) + ord('A')))
    return ''.join(ciphertext)

def vigenere_decrypt(ciphertext, key):
    key = key.upper()
    plaintext = []
    for i in range(len(ciphertext)):
        c = ord(ciphertext[i].upper())
        k = ord(key[i % len(key)].upper())
        plaintext.append(chr(((c - k + 26) % 26) + ord('A')))
    return ''.join(plaintext)

# Implementasi Playfair Cipher
# Playfair cipher implementation (to be added)

# Implementasi Hill Cipher
def hill_encrypt(plaintext, key_matrix):
    matrix_size = key_matrix.shape[0]
    padded_text = plaintext.upper() + 'X' * ((matrix_size - len(plaintext) % matrix_size) % matrix_size)
    plaintext_vector = [ord(char) - ord('A') for char in padded_text]
    ciphertext_vector = []

    for i in range(0, len(plaintext_vector), matrix_size):
        chunk = plaintext_vector[i:i+matrix_size]
        result = np.dot(key_matrix, chunk) % 26
        ciphertext_vector.extend(result)

    ciphertext = ''.join(chr(num + ord('A')) for num in ciphertext_vector)
    return ciphertext

def hill_decrypt(ciphertext, key_matrix):
    # Implement inverse matrix handling and decryption
    pass

# GUI dengan Tkinter
def open_file():
    filepath = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    with open(filepath, 'r') as file:
        text_input.delete("1.0", tk.END)
        text_input.insert(tk.END, file.read())

def save_file(output_text):
    filepath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    with open(filepath, 'w') as file:
        file.write(output_text)

def encrypt():
    selected_cipher = cipher_choice.get()
    text = text_input.get("1.0", tk.END).strip()
    key = key_input.get()

    if len(key) < 12:
        messagebox.showerror("Error", "Kunci harus minimal 12 karakter!")
        return

    if selected_cipher == "Vigenere Cipher":
        result = vigenere_encrypt(text, key)
    elif selected_cipher == "Playfair Cipher":
        result = playfair_encrypt(text, key)  # Implement playfair_encrypt
    elif selected_cipher == "Hill Cipher":
        key_matrix = np.array([[1, 2], [3, 4]])  # Contoh key matrix untuk Hill Cipher
        result = hill_encrypt(text, key_matrix)

    result_output.delete("1.0", tk.END)
    result_output.insert(tk.END, result)

def decrypt():
    selected_cipher = cipher_choice.get()
    text = text_input.get("1.0", tk.END).strip()
    key = key_input.get()

    if len(key) < 12:
        messagebox.showerror("Error", "Kunci harus minimal 12 karakter!")
        return

    if selected_cipher == "Vigenere Cipher":
        result = vigenere_decrypt(text, key)
    elif selected_cipher == "Playfair Cipher":
        result = playfair_decrypt(text, key)  # Implement playfair_decrypt
    elif selected_cipher == "Hill Cipher":
        key_matrix = np.array([[1, 2], [3, 4]])  # Contoh key matrix untuk Hill Cipher
        result = hill_decrypt(text, key_matrix)

    result_output.delete("1.0", tk.END)
    result_output.insert(tk.END, result)

# Antarmuka GUI
root = tk.Tk()
root.title("Rizqi Fitriyani")

# Input text area
tk.Label(root, text="Masukkan Pesan atau Upload File:").pack()
text_input = tk.Text(root, height=10, width=50)
text_input.pack()

# Button untuk upload file
upload_button = tk.Button(root, text="Upload File", command=open_file)
upload_button.pack()

# Pilihan cipher
tk.Label(root, text="Pilih Cipher:").pack()
cipher_choice = tk.StringVar()
cipher_choice.set("Vigenere Cipher")
tk.OptionMenu(root, cipher_choice, "Vigenere Cipher", "Playfair Cipher", "Hill Cipher").pack()

# Input key
tk.Label(root, text="Masukkan Kunci:").pack()
key_input = tk.Entry(root)
key_input.pack()

# Encrypt/Decrypt buttons
encrypt_button = tk.Button(root, text="Enkripsi", command=encrypt)
encrypt_button.pack()

decrypt_button = tk.Button(root, text="Dekripsi", command=decrypt)
decrypt_button.pack()

# Output area
tk.Label(root, text="Hasil:").pack()
result_output = tk.Text(root, height=10, width=50)
result_output.pack()

# Button untuk menyimpan hasil ke file
save_button = tk.Button(root, text="Simpan Hasil", command=lambda: save_file(result_output.get("1.0", tk.END).strip()))
save_button.pack()

root.mainloop()
