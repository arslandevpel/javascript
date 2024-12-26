```python
import os
import shutil

class ExePackager:
    def __init__(self, filenames, output_filename):
        self.filenames = filenames
        self.output_filename = output_filename

    def package_files(self):
        with open(self.output_filename, 'wb') as wfd:
            for f in self.filenames:
                with open(f, 'rb') as fd:
                    shutil.copyfileobj(fd, wfd, 1024*1024*10)

if __name__ == "__main__":
    filenames = ["file1.exe", "file2.exe", "file3.exe"]
    output_filename = "output.exe"
    ExePackager(filenames, output_filename).package_files()
```