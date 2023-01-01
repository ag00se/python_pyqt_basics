# Simple PyQt/PySide examples

### Install PyQt/PySide

Make sure to use python version 3 or higher and choose **one** of the following.

PyQt6:
```
pip install pyqt6
```
PySide6:
```
pip install pyside6
```
PyQt5:
```
pip install pyqt5
```
PySide2:
```
pip install pyside2
```

**ATTENTION:**

For Raspberry Pi OS one can use PyQt5 from the available repositories:
```
sudo apt install python3-pyqt5
```

### Examples

This repository contains examples using PyQt/PySide to create simple user interfaces.
The examples use 'PySide6'. To use a different version or implementation simply replace 'PySide6' with the respective version/implementation. See the comments in the example files.

To plotting examples use the package 'pyqtgraph'. It can be installed via following command:
```
pip install pyqtgraph
```

**ATTENTION:**
When executing the plotting examples on a Raspberry Pi OS (Raspian 11) the following error may occur:
```
ImportError: libcblas.so.3: cannot open shared object file: No such file or directory
```

If that is the case, install the missing library with the following command:
```
sudo apt-get install libatlas-base-dev
```
See [Link](https://stackoverflow.com/questions/53347759/importerror-libcblas-so-3-cannot-open-shared-object-file-no-such-file-or-dire) for more information.
