import os
import shutil

def copy_directory_recursive(src, dest):
    if os.path.exists(dest):
        shutil.rmtree(dest)

    os.mkdir(dest)

    def recurse(current_src, current_dest):
        for entry in os.listdir(current_src):
            src_path = os.path.join(current_src, entry)
            dest_path = os.path.join(current_dest, entry)

            if os.path.isfile(src_path):
                shutil.copy(src_path, dest_path)
                print(f"Copied file: {src_path} → {dest_path}")
            else:
                os.mkdir(dest_path)
                print(f"Created directory: {dest_path}")
                recurse(src_path, dest_path)

    recurse(src, dest)
