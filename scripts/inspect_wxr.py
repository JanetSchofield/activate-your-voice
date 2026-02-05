from __future__ import annotations

import xml.etree.ElementTree as ET
from pathlib import Path

WXR_PATH = Path(r"C:\Users\benho\My Drive\Ben\Business\Activate Your Voice\Repo\activate-your-voice\activateyourvoice.WordPress.2026-02-04.xml")

ns = {
    "content": "http://purl.org/rss/1.0/modules/content/",
    "wp": "http://wordpress.org/export/1.2/",
}

root = ET.fromstring(WXR_PATH.read_text(encoding="utf-8"))
channel = root.find("channel")
items = channel.findall("item") if channel is not None else []

rows: list[tuple[str, str, str]] = []
for item in items:
    post_type = item.find("wp:post_type", ns)
    status = item.find("wp:status", ns)
    title = item.findtext("title", default="")
    slug = item.findtext("wp:post_name", default="", namespaces=ns)

    if post_type is None:
        continue
    post_type_text = post_type.text or ""
    status_text = status.text if status is not None else ""
    if status_text != "publish":
        continue
    if post_type_text not in {"page", "post"}:
        continue
    rows.append((post_type_text, title, slug))

for row in rows:
    print("\t".join(row))
