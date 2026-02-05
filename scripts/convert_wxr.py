from __future__ import annotations

import xml.etree.ElementTree as ET
from pathlib import Path
import re
import sys

def clean_html(html_content: str) -> str:
    """Convert HTML to basic markdown"""
    if not html_content:
        return ""
    
    # Remove WordPress blocks wrapper
    content = re.sub(r'<!-- wp:.*?-->', '', html_content)
    content = re.sub(r'<!-- /wp:.*?-->', '', content)
    
    # Convert paragraphs
    content = re.sub(r'<p>(.*?)</p>', r'\1\n\n', content, flags=re.DOTALL)
    
    # Convert headings
    content = re.sub(r'<h1>(.*?)</h1>', r'# \1\n\n', content)
    content = re.sub(r'<h2>(.*?)</h2>', r'## \1\n\n', content)
    content = re.sub(r'<h3>(.*?)</h3>', r'### \1\n\n', content)
    content = re.sub(r'<h4>(.*?)</h4>', r'#### \1\n\n', content)
    
    # Convert images
    content = re.sub(
        r'<img[^>]*src="([^"]*)"[^>]*alt="([^"]*)"[^>]*>',
        r'![\2](\1)',
        content
    )
    content = re.sub(
        r'<img[^>]*src="([^"]*)"[^>]*>',
        r'![](\1)',
        content
    )
    
    # Convert links
    content = re.sub(r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>', r'[\2](\1)', content, flags=re.DOTALL)
    
    # Convert lists
    content = re.sub(r'<ul>(.*?)</ul>', lambda m: convert_list(m.group(1), '-'), content, flags=re.DOTALL)
    content = re.sub(r'<ol>(.*?)</ol>', lambda m: convert_list(m.group(1), '1.'), content, flags=re.DOTALL)
    
    # Convert strong/bold
    content = re.sub(r'<strong>(.*?)</strong>', r'**\1**', content)
    content = re.sub(r'<b>(.*?)</b>', r'**\1**', content)
    
    # Convert em/italic
    content = re.sub(r'<em>(.*?)</em>', r'*\1*', content)
    content = re.sub(r'<i>(.*?)</i>', r'*\1*', content)
    
    # Remove any remaining HTML tags
    content = re.sub(r'<[^>]+>', '', content)
    
    # Clean up excessive whitespace
    content = re.sub(r'\n\n\n+', '\n\n', content)
    content = content.strip()
    
    return content

def convert_list(list_content: str, marker: str) -> str:
    """Convert HTML list to markdown"""
    items = re.findall(r'<li>(.*?)</li>', list_content, flags=re.DOTALL)
    result = '\n'
    for item in items:
        clean_item = re.sub(r'<[^>]+>', '', item).strip()
        result += f'{marker} {clean_item}\n'
    result += '\n'
    return result

def main():
    if len(sys.argv) < 2:
        print("Usage: python convert_wxr.py <path_to_wxr_file>")
        sys.exit(1)
    
    wxr_path = Path(sys.argv[1])
    
    if not wxr_path.exists():
        print(f"Error: File not found: {wxr_path}")
        sys.exit(1)
    
    output_dir = Path("WPBackup/cleaned/posts")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    ns = {
        "content": "http://purl.org/rss/1.0/modules/content/",
        "wp": "http://wordpress.org/export/1.2/",
        "excerpt": "http://wordpress.org/export/1.2/excerpt/"
    }
    
    root = ET.fromstring(wxr_path.read_text(encoding="utf-8"))
    channel = root.find("channel")
    items = channel.findall("item") if channel is not None else []
    
    posts_created = 0
    
    for item in items:
        post_type = item.find("wp:post_type", ns)
        status = item.find("wp:status", ns)
        
        if post_type is None or status is None:
            continue
            
        post_type_text = post_type.text or ""
        status_text = status.text or ""
        
        # Only process published posts
        if status_text != "publish" or post_type_text != "post":
            continue
        
        title = item.findtext("title", default="")
        slug = item.findtext("wp:post_name", default="", namespaces=ns)
        pub_date = item.findtext("wp:post_date", default="", namespaces=ns)
        content_html = item.findtext("content:encoded", default="", namespaces=ns)
        excerpt = item.findtext("excerpt:encoded", default="", namespaces=ns)
        
        if not slug:
            continue
        
        # Convert content to markdown
        content_md = clean_html(content_html)
        excerpt_md = clean_html(excerpt)
        
        # Extract featured image if exists
        featured_image = ""
        for meta in item.findall("wp:postmeta", ns):
            meta_key = meta.findtext("wp:meta_key", default="", namespaces=ns)
            if meta_key == "_thumbnail_id":
                # We would need to match this ID with the attachments
                # For now, skip this
                pass
        
        # Create frontmatter
        frontmatter = f"""---
title: "{title}"
date: {pub_date}
"""
        if excerpt_md:
            excerpt_clean = excerpt_md.replace('"', '\\"')
            frontmatter += f'description: "{excerpt_clean}"\n'
        
        frontmatter += "---\n\n"
        
        # Write to file
        output_file = output_dir / f"{slug}.md"
        output_file.write_text(frontmatter + content_md, encoding="utf-8")
        posts_created += 1
        print(f"Created: {slug}.md")
    
    print(f"\nTotal posts created: {posts_created}")
    print(f"Output directory: {output_dir}")

if __name__ == "__main__":
    main()
