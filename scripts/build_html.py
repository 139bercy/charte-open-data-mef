#!/usr/bin/env python3
import os
import re
import subprocess
import sys

def main():
    # Paths
    src_file = "src/main.md"
    template_file = "scripts/templates/default.html"
    output_dir = "build"
    output_file = os.path.join(output_dir, "index.html")

    # 1. Read input markdown
    if not os.path.exists(src_file):
        print(f"Error: Source file {src_file} not found.", file=sys.stderr)
        sys.exit(1)

    with open(src_file, "r", encoding="utf-8") as f:
        markdown_content = f.read()

    # 2. Extract Title (first line starting with '#')
    title = "Charte Open Data des ministères économiques et financiers"
    for line in markdown_content.splitlines():
        if line.startswith("# "):
            title = line[2:].strip()
            break

    # 3. Get Version from Git
    version = "v1.0.0"
    try:
        # Get latest git tag
        version_bytes = subprocess.check_output(
            ["git", "describe", "--tags", "--abbrev=0"],
            stderr=subprocess.DEVNULL
        )
        version = version_bytes.decode("utf-8").strip()
    except Exception:
        try:
            # Fallback if describe fails
            tags_bytes = subprocess.check_output(
                "git tag | tail -1",
                shell=True,
                stderr=subprocess.DEVNULL
            )
            val = tags_bytes.decode("utf-8").strip()
            if val:
                version = val
        except Exception:
            pass

    # 4. Clean markdown: Remove manual table of contents (from '## Table' to '## Introduction')
    # This prevents duplicate TOCs on the page.
    cleaned_markdown = re.sub(
        r'## Table\s*\n.*?(?=\n## Introduction)',
        '',
        markdown_content,
        flags=re.DOTALL
    )

    # 5. Run Pandoc to convert Markdown to HTML Body
    try:
        process = subprocess.Popen(
            ["pandoc", "-f", "gfm", "-t", "html5"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8"
        )
        html_body, stderr = process.communicate(input=cleaned_markdown)
        if process.returncode != 0:
            print(f"Error running pandoc: {stderr}", file=sys.stderr)
            sys.exit(1)
    except Exception as e:
        print(f"Failed to execute pandoc: {e}", file=sys.stderr)
        sys.exit(1)

    # 6. Parse H2 and H3 headings to construct the DSFR SideMenu (TOC)
    # Pandoc generates headings like: <h2 id="id-name">Heading Text</h2>
    headings = re.findall(
        r'<(h2|h3)\s+id="([^"]+)"[^>]*>(.*?)</\1>',
        html_body,
        re.DOTALL
    )

    toc_html = '<ul class="fr-sidemenu__list">\n'
    current_h2_item = None
    h2_has_children = False

    for tag, h_id, h_text in headings:
        # Strip internal HTML tags inside headings (like <strong> or <code>) and clean up newlines/extra spaces
        h_text_clean = re.sub(r'<[^>]+>', '', h_text)
        h_text_clean = re.sub(r'\s+', ' ', h_text_clean).strip()

        # Skip the Table of Contents header itself if it got generated
        if h_id == "table" or h_text_clean.lower() == "table":
            continue

        if tag == "h2":
            if current_h2_item:
                if h2_has_children:
                    toc_html += '        </ul>\n'
                toc_html += '    </li>\n'
            toc_html += f'    <li class="fr-sidemenu__item">\n        <a class="fr-sidemenu__link" href="#{h_id}" target="_self">{h_text_clean}</a>\n'
            current_h2_item = h_id
            h2_has_children = False
        elif tag == "h3" and current_h2_item:
            if not h2_has_children:
                toc_html += '        <ul class="fr-sidemenu__list">\n'
                h2_has_children = True
            toc_html += f'            <li class="fr-sidemenu__item"><a class="fr-sidemenu__link" href="#{h_id}" target="_self">{h_text_clean}</a></li>\n'

    if current_h2_item:
        if h2_has_children:
            toc_html += '        </ul>\n'
        toc_html += '    </li>\n'
    toc_html += '</ul>'

    # 7. Post-process HTML Body (apply DSFR classes, wrap tables)
    # DSFR requires tables to be wrapped in a container with class 'fr-table'
    html_body = html_body.replace('<table>', '<div class="fr-table"><table>')
    html_body = html_body.replace('</table>', '</table></div>')

    # 8. Load HTML template and inject variables
    if not os.path.exists(template_file):
        print(f"Error: Template {template_file} not found.", file=sys.stderr)
        sys.exit(1)

    with open(template_file, "r", encoding="utf-8") as f:
        template_content = f.read()

    final_html = template_content
    final_html = final_html.replace("{{title}}", title)
    final_html = final_html.replace("{{version}}", version)
    final_html = final_html.replace("{{toc}}", toc_html)
    final_html = final_html.replace("{{body}}", html_body)

    # 9. Write final output
    os.makedirs(output_dir, exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(final_html)

    # 10. Copy media assets so they load correctly relative to the build directory
    import shutil
    src_media_dir = "src/media"
    dest_media_dir = os.path.join(output_dir, "src/media")
    if os.path.exists(src_media_dir):
        if os.path.exists(dest_media_dir):
            shutil.rmtree(dest_media_dir)
        shutil.copytree(src_media_dir, dest_media_dir)
        print(f"Copied media assets from '{src_media_dir}' to '{dest_media_dir}'")

    print(f"Success! Generated DSFR-compliant HTML at '{output_file}' (Version: {version})")

if __name__ == "__main__":
    main()
