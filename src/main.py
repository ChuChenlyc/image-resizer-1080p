# File: /image-resizer-1080p/image-resizer-1080p/src/main.py

import os
import sys
from PIL import Image
from tkinter import Tk, filedialog, Button, Label, StringVar
from tkinter.ttk import Progressbar
import threading

def resize_image(input_path, output_path):
    """将图像转换为1920x1080分辨率，保持纵横比，并用透明背景填充"""
    try:
        img = Image.open(input_path)
        
        if img.mode != 'RGBA':
            img = img.convert('RGBA')
        
        width, height = img.size
        ratio = min(1920/width, 1080/height)
        new_size = (int(width * ratio), int(height * ratio))
        
        resized_img = img.resize(new_size, Image.LANCZOS)
        
        new_img = Image.new('RGBA', (1920, 1080), (0, 0, 0, 0))
        
        paste_x = (1920 - new_size[0]) // 2
        paste_y = (1080 - new_size[1]) // 2
        
        new_img.paste(resized_img, (paste_x, paste_y), resized_img)
        
        new_img.save(output_path)
        return True
    except Exception as e:
        print(f"处理 {input_path} 时出错: {e}")
        return False

def process_folder(input_folder, output_folder, progress_var, status_var):
    """处理文件夹中的所有图片"""
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    image_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.webp')
    image_files = [f for f in os.listdir(input_folder) 
                  if os.path.isfile(os.path.join(input_folder, f)) 
                  and f.lower().endswith(image_extensions)]
    
    total_files = len(image_files)
    processed = 0
    
    for filename in image_files:
        input_path = os.path.join(input_folder, filename)
        
        output_path = os.path.join(output_folder, filename)
        if not output_path.lower().endswith('.png'):
            output_path = os.path.splitext(output_path)[0] + '.png'
        
        success = resize_image(input_path, output_path)
        
        processed += 1
        progress = int((processed / total_files) * 100)
        progress_var.set(progress)
        
        status_text = f"处理中: {processed}/{total_files} - {filename}"
        status_var.set(status_text)
    
    status_var.set(f"完成! 已处理 {processed}/{total_files} 个文件")

def create_gui():
    """创建图形用户界面"""
    root = Tk()
    root.title("图片批量转换为1920x1080")
    root.geometry("500x300")
    root.resizable(False, False)
    
    input_folder = StringVar()
    output_folder = StringVar()
    status_var = StringVar(value="等待选择文件夹...")
    progress_var = StringVar(value="0")
    
    Label(root, text="照片批量转换工具 (1920x1080)", font=("Arial", 14)).pack(pady=10)
    
    def select_input():
        folder = filedialog.askdirectory(title="选择包含图片的文件夹")
        if folder:
            input_folder.set(folder)
            if not output_folder.get():
                output_folder.set(os.path.join(folder, "resized"))
            status_var.set("已选择输入文件夹")
    
    def select_output():
        folder = filedialog.askdirectory(title="选择输出文件夹")
        if folder:
            output_folder.set(folder)
    
    def start_process():
        if not input_folder.get():
            status_var.set("错误: 请先选择输入文件夹!")
            return
        
        start_button.config(state="disabled")
        input_button.config(state="disabled")
        output_button.config(state="disabled")
        
        thread = threading.Thread(
            target=process_folder, 
            args=(input_folder.get(), output_folder.get(), progress_var, status_var)
        )
        thread.daemon = True
        thread.start()
        
        def check_thread():
            if thread.is_alive():
                root.after(100, check_thread)
            else:
                start_button.config(state="normal")
                input_button.config(state="normal")
                output_button.config(state="normal")
        
        root.after(100, check_thread)
    
    input_frame = Label(root)
    input_frame.pack(fill="x", padx=20, pady=5)
    input_button = Button(input_frame, text="选择输入文件夹", command=select_input)
    input_button.pack()
    
    output_frame = Label(root)
    output_frame.pack(fill="x", padx=20, pady=5)
    output_button = Button(output_frame, text="选择输出文件夹", command=select_output)
    output_button.pack()
    
    start_button = Button(root, text="开始处理", command=start_process)
    start_button.pack(pady=10)
    
    progress = Progressbar(root, orient="horizontal", length=400, mode="determinate", variable=progress_var)
    progress.pack(padx=20, pady=10)
    
    status_label = Label(root, textvariable=status_var)
    status_label.pack(pady=10)
    
    explanation = Label(root, text="此工具将图片转换为1920x1080分辨率，保持纵横比，多余部分用透明填充",
                       font=("Arial", 8), wraplength=450)
    explanation.pack(side="bottom", pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    create_gui()