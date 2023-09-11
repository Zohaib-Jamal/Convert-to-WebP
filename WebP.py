import tkinter as tk
from tkinter import filedialog
from PIL import Image
import os

def convert_to_webp(input_path, output_path, quality=80):
    try:
        image = Image.open(input_path)
        if image.format in ['JPEG', 'JPG', 'PNG']:
            output_file = os.path.join(output_path, os.path.splitext(os.path.basename(input_path))[0] + '.webp')
            image.save(output_file, 'WEBP', quality=quality)
            return True
        else:
            return False
    except Exception as e:
        print(f"Error converting {input_path}: {e}")
        return False

def batch_convert_to_webp(input_folder, output_folder, quality=80):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                input_path = os.path.join(root, file)
                convert_to_webp(input_path, output_folder, quality)

def browse_input_folder():
    folder_path = filedialog.askdirectory()
    input_folder_entry.delete(0, tk.END)
    input_folder_entry.insert(0, folder_path)

def browse_output_folder():
    folder_path = filedialog.askdirectory()
    output_folder_entry.delete(0, tk.END)
    output_folder_entry.insert(0, folder_path)

def convert_images():
    input_folder = input_folder_entry.get()
    output_folder = output_folder_entry.get()
    quality = int(quality_entry.get())

    batch_convert_to_webp(input_folder, output_folder, quality)

# Create the main window
root = tk.Tk()
root.title("Image Converter")

# Styling
bg_color = "#f0f0f0"
button_color = "#4caf50"
text_color = "#333"

root.configure(bg=bg_color)

# Header
header_label = tk.Label(root, text="Image Converter", font=("Arial", 16, "bold"), bg=bg_color, fg=text_color)
header_label.pack(pady=10)

# Input Folder
input_folder_frame = tk.Frame(root, bg=bg_color)
input_folder_label = tk.Label(input_folder_frame, text="Input Folder:   ", bg=bg_color, fg=text_color)
input_folder_label.pack(side=tk.LEFT, padx=10)
input_folder_entry = tk.Entry(input_folder_frame, bg="white", fg=text_color)
input_folder_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10)
input_folder_button = tk.Button(input_folder_frame, text="Browse", command=browse_input_folder, bg=button_color, fg="white")
input_folder_button.pack(side=tk.RIGHT, padx=10)
input_folder_frame.pack(fill=tk.X, padx=20, pady=5)

# Output Folder
output_folder_frame = tk.Frame(root, bg=bg_color)
output_folder_label = tk.Label(output_folder_frame, text="Output Folder:", bg=bg_color, fg=text_color)
output_folder_label.pack(side=tk.LEFT, padx=10)
output_folder_entry = tk.Entry(output_folder_frame, bg="white", fg=text_color)
output_folder_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10)
output_folder_button = tk.Button(output_folder_frame, text="Browse", command=browse_output_folder, bg=button_color, fg="white")
output_folder_button.pack(side=tk.RIGHT, padx=10)
output_folder_frame.pack(fill=tk.X, padx=20, pady=5)

# Quality
quality_frame = tk.Frame(root, bg=bg_color)
quality_label = tk.Label(quality_frame, text="Quality (0-100):", bg=bg_color, fg=text_color)
quality_label.pack(side=tk.LEFT, padx=10)
quality_entry = tk.Entry(quality_frame, bg="white", fg=text_color)
quality_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10)
quality_frame.pack(fill=tk.X, padx=20, pady=5)

# Convert Button
convert_button = tk.Button(root, text="Convert Images", command=convert_images, bg=button_color, fg="white")
convert_button.pack(pady=10)

# Start the GUI event loop
root.mainloop()
