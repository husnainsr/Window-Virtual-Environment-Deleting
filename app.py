import os
import shutil
from tqdm import tqdm

def get_folder_size(folder_path):
    """Calculate total size of a folder in bytes"""
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            try:
                total_size += os.path.getsize(file_path)
            except (OSError, PermissionError):
                continue
    return total_size

def format_size(size_bytes):
    """Convert bytes to human readable format"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.2f} TB"

def find_venv_folders(start_path='D:\\'):
    """Find all venv folders and __pycache__ folders in the specified path"""
    venv_paths = []
    pycache_paths = []
    
    try:
        print(f"Scanning {start_path[0]} drive for venv and __pycache__ folders...")
        for root, dirs, _ in os.walk(start_path):
            # Skip AppData directories
            if 'AppData' in root:
                continue
                
            if 'venv' in dirs:
                venv_path = os.path.join(root, 'venv')
                venv_paths.append(venv_path)
                
            if '__pycache__' in dirs:
                pycache_path = os.path.join(root, '__pycache__')
                pycache_paths.append(pycache_path)
                
    except PermissionError as e:
        print(f"Permission error accessing some directories: {e}")
    except Exception as e:
        print(f"Error during scanning: {e}")
            
    return venv_paths, pycache_paths

def delete_venv_folders(venv_paths):
    """Delete venv folders with progress bar"""
    print(f"\nFound {len(venv_paths)} venv folders to delete")
    
    with tqdm(total=len(venv_paths), desc="Deleting venv folders", unit="folder") as pbar:
        for path in venv_paths:
            try:
                shutil.rmtree(path)
                pbar.set_postfix_str(f"Deleted: {path}")
            except PermissionError:
                pbar.set_postfix_str(f"Permission denied: {path}")
            except Exception as e:
                pbar.set_postfix_str(f"Error: {path} - {str(e)}")
            pbar.update(1)

def main():
    # Get drive or path from user
    default_path = 'C:\\'
    user_path = input(f"Enter drive letter (e.g. D) or full path (default: {default_path}): ").strip()
    
    # Convert single letter to drive path
    if len(user_path) == 1:
        start_path = f"{user_path}:\\"
    elif not user_path:
        start_path = default_path
    else:
        start_path = user_path

    # Find all venv and pycache folders in specified path
    venv_paths, pycache_paths = find_venv_folders(start_path)
    all_paths = venv_paths + pycache_paths
    
    if not all_paths:
        print(f"No venv or __pycache__ folders found in {start_path}!")
        return
        
    # Calculate total size
    print("\nCalculating total size...")
    total_size = 0
    for path in all_paths:
        try:
            size = get_folder_size(path)
            total_size += size
        except Exception as e:
            print(f"Error calculating size for {path}: {e}")
    
    # Print folders and total size
    print("\nFound the following folders:")
    for path in venv_paths:
        try:
            size = get_folder_size(path)
            print(f"- {path} ({format_size(size)}) [venv]")
        except Exception:
            print(f"- {path} (size calculation failed) [venv]")
            
    for path in pycache_paths:
        try:
            size = get_folder_size(path)
            print(f"- {path} ({format_size(size)}) [pycache]")
        except Exception:
            print(f"- {path} (size calculation failed) [pycache]")
    
    print(f"\nTotal size: {format_size(total_size)}")
        
    confirm = input("\nDo you want to delete these folders? (y/n): ")
    
    if confirm.lower() == 'y':
        delete_venv_folders(all_paths)  # Reusing the same delete function for both types
        print("\nDeletion complete!")
    else:
        print("\nOperation cancelled.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")