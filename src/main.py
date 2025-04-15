from textnode import TextNode, TextType
from page_generator import generate_page
from markdown_to_html_node import markdown_to_html_node
from file_utils import copy_directory_recursive
from textnode_utils import text_to_children
from generate_pages_recursive import generate_pages_recursive 



def main():
    node = TextNode("**Bold text**", TextType.Bold)
    print(node)

    #Copy static files

    copy_directory_recursive("static", "public")


    generate_pages_recursive("content", "src/template.html", "public")

    #Generate index.html 
    # generate_page("content/index.md", "src/template.html", "public/index.html")
    # generate_page("content/index.md", "src/template.html", "public/index.html")
    # generate_page("content/blog/glorfindel/index.md", "src/template.html", "public/blog/glorfindel/index.html")
    # generate_page("content/blog/tom/index.md", "src/template.html", "public/blog/tom/index.html")
    # generate_page("content/blog/majesty/index.md", "src/template.html", "public/blog/majesty/index.html")
    # generate_page("content/contact/index.md", "src/template.html", "public/contact/index.html")




  



main()