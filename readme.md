# Virtual Environment Folder Manager

This Python script helps you find, calculate the size of, and delete virtual environment (venv) folders on your system. It scans a specified drive or path, lists the found venv folders, and provides an option to delete them with a progress bar.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Functions](#functions)
- [Contributing](#contributing)
- [License](#license)

## Features
- Scans a specified drive or directory for virtual environment folders.
- Calculates the total size of found venv folders.
- Displays the size of each venv folder in a human-readable format.
- Provides a progress bar for deleting venv folders.
- Handles permission errors gracefully.

## Installation

To run this script, ensure you have Python installed on your system. You can clone the repository and run the script directly.

```bash
git clone https://github.com/husnainsr/Window-Virtual-Environment-Deleting.git
cd Window-Virtual-Environment-Deleting
python app.py
```

## Usage

Run the script using Python. You will be prompted to enter a drive letter (e.g., D) or a full path to scan for venv folders.

```bash
python app.py
```

### Example Interaction

1. Enter drive letter (e.g. D) or full path (default: C:\): D
2. Scanning D drive for venv folders...
3. Found the following venv folders:
   - D:\path\to\venv1 (10.50 MB)
   - D:\path\to\venv2 (5.25 MB)
4. Total size: 15.75 MB
5. Do you want to delete these folders? (y/n)




## Functions

### `get_folder_size(folder_path)`
Calculates the total size of a folder in bytes.

### `format_size(size_bytes)`
Converts bytes to a human-readable format (B, KB, MB, GB, TB).

### `find_venv_folders(start_path='D:\\')`
Finds all venv folders in the specified drive or path.

### `delete_venv_folders(venv_paths)`
Deletes the specified venv folders and shows a progress bar during deletion.


## License

This project is licensed under the [MIT License](LICENSE) - see the LICENSE file for details.
