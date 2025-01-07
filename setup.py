from setuptools import setup, find_packages

setup(
    name="test_pip_package",  # 包名
    version="0.1.0",  # 版本号
    author="Your Name",  # 作者名字
    author_email="you@example.com",  # 作者邮箱
    description="A short description of the package",  # 简短描述
    long_description=open("README.md").read(),  # 长描述，通常是从README读取
    long_description_content_type="text/markdown",  # 长描述的内容类型
    url="https://github.com/lvyuanx/test_pip_package",  # 项目主页URL
    packages=find_packages(),  # 自动发现包和子包
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # 使用的许可证
        "Operating System :: OS Independent",  # 操作系统无关性
    ],
    python_requires=">=3.11",  # 所需的最低Python版本
    install_requires=[
        "requests",
    ],
)
