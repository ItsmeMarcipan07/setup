import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "excludes": ["tkinter", "unittest"],
    "zip_include_packages": ["encodings", "PySide6"],
}

additional_files = [
    ("C:\\Users\SESA732254\PycharmProjects\pythonProject1\SYSTEM\weather_config.py", "weather_config.py"),
    ("C:\\Users\SESA732254\PycharmProjects\pythonProject1\SYSTEM\settings.txt", "settings.txt"),
    ("C:\\Users\SESA732254\PycharmProjects\pythonProject1\SYSTEM\sending_info.py", "sending_info.py"),
    ("C:\\Users\SESA732254\PycharmProjects\pythonProject1\SYSTEM\modbus_protocols.py", "modbus_protocols.py"),
    ("C:\\Users\SESA732254\PycharmProjects\pythonProject1\SYSTEM\data_from_user.py", "data_from_user.py"),
    ("C:\\Users\SESA732254\PycharmProjects\pythonProject1\SYSTEM\connection.py", "connection.py"),
    ("C:\\Users\SESA732254\PycharmProjects\pythonProject1\SYSTEM\config.py", "config.py")]

include_packages = ["pymodbus", "pyowm", "time", "pathlib", "tkinter"]

# base="Win32GUI" should be used only for Windows GUI app
base = "Win32GUI" if sys.platform == "win32" else None

setup(
    name="my_app",
    version="1.5",
    description="WEATHRE-APP",
    options={"build_exe": {"include_files": additional_files,
                           "packages": include_packages,
                           "zip_include_packages": ["encodings", "PySide6"]}},
    executables=[Executable("SYSTEM\start.py", base=base,
                            target_name="WEATHER-PLC",
                            icon="C:\\Users\SESA732254\PycharmProjects\pythonProject1\SYSTEM\OIP.ico")],
)
