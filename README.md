# fileOrganizer
# Downloads Organizer

## Overview

This Python script helps you organize files in your Downloads directory by categorizing them into subfolders based on their file types. It automatically creates folders for each file type and moves the respective files into their corresponding folders.

## Prerequisites

Before running the script, make sure you have the following:

- Python 3.x installed on your computer.
- The `os`, `pathlib`, and `shutil` libraries, which are typically included with Python.

## Usage

1. Clone or download the script to your computer.

2. Open a terminal or command prompt.

3. Navigate to the directory where you saved the script.

4. Run the script using the following command:

   ```
   python organize_downloads.py
   ```

5. The script will automatically find your Downloads directory and organize the files.

## Script Details

- The script first locates your Downloads directory using common paths in Windows.
- It then retrieves a list of all files in the Downloads directory.
- For each file, it extracts the file type (extension).
- It creates a subfolder for each unique file type (e.g., PDFs, images, documents).
- Files with the same type are moved into their corresponding subfolders.
- The script prints each file movement operation to the console.

## Example Output

```
Downloads directory found: C:\Users\YourUsername\Downloads
Moving C:\Users\YourUsername\Downloads\example.pdf >>> C:\Users\YourUsername\Downloads\pdf_folder
Moving C:\Users\YourUsername\Downloads\image.jpg >>> C:\Users\YourUsername\Downloads\jpg_folder
Moving C:\Users\YourUsername\Downloads\document.docx >>> C:\Users\YourUsername\Downloads\docx_folder
```

## Customization

- You can customize the file type categories and folder naming by modifying the script.
- To add or modify categories, update the `fileList` variable.
- To change folder naming conventions, adjust the folder naming logic in the script.

## License

This script is provided under the [MIT License](LICENSE.md).

---

Feel free to customize this README file further to include any additional information or instructions specific to your use case.
