@echo off
echo 正在安装依赖...
pip install -r requirements.txt

echo 正在构建EXE文件...
pyinstaller --noconfirm --onefile --windowed --icon=icon.ico --name="ImageResizer1080p" --add-data="icon.ico;." src/main.py

echo 构建完成！
pause