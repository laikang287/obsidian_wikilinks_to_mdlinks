
# Obsidian WikiLinks to Markdown Links Converter

This script converts Obsidian-style WikiLinks to standard Markdown links in all `.md` files within a specified directory.

## Features

- Converts WikiLinks like `[[page#heading|alias]]` to `[alias](./page.md#heading)`.
- Handles links with headings and aliases.
- Ignores and removes image size or position specifications.
- Processes all `.md` files in a directory recursively.

## Usage

1. **install Python3**

2. **backup**

This script is intended for personal use and has not been thoroughly tested. Please make sure to back up your files before using it.

4. **Run the script:**

Use the following command to run the script and convert all WikiLinks to Markdown links:

```bash
cd obsidian_wikilinks_to_mdlinks
python3 obsidian_wikilinks_to_mdlinks.py <directory_path>  
```

3. **Check the converted files:**

The script will process all `.md` files in the specified directory and its subdirectories. If any links are converted, the script will print the file path.

## Example

Before conversion:

```
[[page#heading|Read More]]
[[image|100x100]]
```

After conversion:

```
[Read More](./page.md#heading)
```

The image link with size information will be removed.
