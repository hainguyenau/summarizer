from cx_Freeze import setup, Executable
import os

os.environ['TCL_LIBRARY'] = "C:\\Users\\Misa\\Anaconda3\\pkgs\\python-3.6.4-h0c2934d_3\\tcl"
os.environ['TK_LIBRARY'] = "C:\\Users\\Misa\\Anaconda3\\pkgs\\tk-8.6.4-vc14_intel_27"

setup(name='summarize', version='0.1', description='summarize', executables=[Executable('summarize.py')])
