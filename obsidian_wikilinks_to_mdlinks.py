import os
import re
import sys

def convert_wiki_to_md_links(directory):
    # Regular expression to match wiki-style links [[link#heading|alias]] or [[image|100x100]]
    wiki_link_pattern = re.compile(r'\[\[([^\|\]]+)(#[^\|\]]+)?(\|([^\|\]]+))?(\|[^\]]+)?\]\]')

    for root, _, files in os.walk(directory):
        for file_name in files:
            if file_name.endswith(".md"):
                file_path = os.path.join(root, file_name)
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()

                # Replace wiki-style links with standard Markdown links
                new_content = wiki_link_pattern.sub(
                    lambda match: handle_match(match, root),
                    content
                )

                if new_content != content:
                    with open(file_path, 'w', encoding='utf-8') as file:
                        file.write(new_content)
                    print(f"Converted links in {file_path}")

def handle_match(match, root):
    link = match.group(1).replace(' ', '%20')  # Link part
    heading = match.group(2) if match.group(2) else ''  # Heading part (if any)
    alias = match.group(4) if match.group(4) else match.group(1)  # Alias (if any)

    # Get relative path
    rel_link = os.path.relpath(os.path.join(root, link), root)
    rel_link = rel_link.replace('\\', '/')  # Ensure the path uses Unix-style separators

    # Standard Markdown link format
    return f"[{alias}]({rel_link}{heading})"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <directory_path>")
        sys.exit(1)

    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory path")
        sys.exit(1)

    convert_wiki_to_md_links(directory)
