import os
from page_generator import generate_page 


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for entry in os.listdir(dir_path_content):
        entry_path = os.path.join(dir_path_content, entry)
        dest_entry_path = os.path.join(dest_dir_path, entry)

        if os.path.isfile(entry_path) and entry_path.endswith(".md"):
            #replace  .md with .html 
            dest_file = os.path.join(dest_dir_path, "index.html")
            generate_page(entry_path, template_path, dest_file)

        elif os.path.isdir(entry_path):
            generate_pages_recursive(entry_path, template_path, dest_entry_path)
