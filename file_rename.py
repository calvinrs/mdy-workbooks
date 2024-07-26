import os

def replace_dots_in_filenames_keep_extension(root_dir, replacement_char='_'):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            base_name, ext = os.path.splitext(filename)
            if '.' in base_name:
                # Replace dots in the base name only, not in the extension
                new_base_name = base_name.replace('.', replacement_char)
                # Reassemble the new filename with its original extension
                new_filename = new_base_name + ext
                old_filepath = os.path.join(dirpath, filename)
                new_filepath = os.path.join(dirpath, new_filename)
                # Rename the file
                os.rename(old_filepath, new_filepath)
                print(f'Renamed: {old_filepath} to {new_filepath}')

def main():
    # Prompt user for input
    root_dir = input("Enter the root directory to start the renaming process: ").strip()
    replacement_char = input("Enter the character to replace dots with (default is '_'): ").strip() or '_'
    
    # Validate the directory path
    if not os.path.isdir(root_dir):
        print(f"Error: The directory '{root_dir}' does not exist.")
        return
    
    # Call the renaming function
    replace_dots_in_filenames_keep_extension(root_dir, replacement_char)

if __name__ == '__main__':
    main()