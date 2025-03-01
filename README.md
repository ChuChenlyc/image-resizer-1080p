# 图片批量转换为1920x1080工具

一个简单的工具，用于批量将图片转换为1920x1080分辨率，同时保持原始纵横比，并用透明背景填充额外空间。

## 特性

- 批量处理整个文件夹的图片
- 保持图片原始纵横比
- 使用透明背景填充到1920x1080尺寸
- 简单易用的图形界面
- 进度条显示处理进度

## 安装方法

### 使用预编译的EXE文件

1. 从[发布页面](https://github.com/chuchenlyc/image-resizer-1080p/releases)下载最新的EXE文件
2. 直接运行，无需安装

### 从源代码运行

1. 确保安装了Python 3.6+
2. 克隆此仓库：`git clone https://github.com/chuchenlyc/image-resizer-1080p.git`
3. 安装依赖：`pip install -r requirements.txt`
4. 运行程序：`python src/main.py`

## 使用方法

1. 点击"选择输入文件夹"按钮选择包含图片的文件夹
2. 可选：点击"选择输出文件夹"按钮选择输出位置（默认为输入文件夹下的"resized"子文件夹）
3. 点击"开始处理"按钮开始转换图片
4. 等待处理完成

## 支持的图片格式

- PNG (.png)
- JPEG (.jpg, .jpeg)
- BMP (.bmp)
- GIF (.gif)
- WebP (.webp)

## 许可证

MIT许可证 - 查看 [LICENSE](LICENSE) 文件了解详情