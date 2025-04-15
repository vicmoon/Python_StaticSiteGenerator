from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title
import os

def generate_page(from_path, template_path, dest_path, base_path="/"):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path) as f:
        markdown = f.read()

    with open(template_path) as f:
        template = f.read()

    html_content = markdown_to_html_node(markdown).to_html()

    title = extract_title(markdown)

    result = template.replace("{{ Title }}", title).replace("{{ Content }}", html_content)
    result = result.replace('href="/', f'href="{base_path}')
    result = result.replace('src="/', f'src="{base_path}')


    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(result)

    print(f"✅ Page written to {dest_path}")


