from setuptools import setup, find_packages

setup(
    name="image-resizer-1080p",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "Pillow",
    ],
    author="您的名字",
    author_email="您的邮箱",
    description="批量将图片转换为1920x1080分辨率并保持纵横比的工具",
    keywords="image, resize, 1080p",
    url="https://github.com/您的用户名/image-resizer-1080p",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.6",
)