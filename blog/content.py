from __future__ import annotations
from html.parser import HTMLParser

def html_to_blocks(html: str) -> dict:
    """
    Simple converter, may need extending later.
    Produces blocks used for:
      - fediverse teaser text
      - search indexing
      - future structured rendering
    Extend as needed.
    """
    parser = _BlockParser()
    parser.feed(html or "")
    return {"type": "doc", "blocks": parser.blocks}


class _BlockParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.blocks: list[dict] = []
        self._stack: list[str] = []
        self._buf: list[str] = []
        self._current_href: str | None = None

    def handle_starttag(self, tag: str, attrs):
        self._stack.append(tag)
        attrs_d = dict(attrs)

        if tag == "a":
            self._current_href = attrs_d.get("href")

        if tag in {"p", "h2", "h3", "h4", "li", "blockquote"}:
            self._buf = []

        if tag == "img":
            src = attrs_d.get("src")
            alt = attrs_d.get("alt")
            if src:
                self.blocks.append({"type": "image", "src": src, "alt": alt})

        if tag == "iframe":
            src = attrs_d.get("src")
            if src:
                self.blocks.append({"type": "embed", "src": src})

    def handle_endtag(self, tag: str):
        # emit text-ish blocks
        if tag in {"p", "h2", "h3", "h4", "li", "blockquote"}:
            text = "".join(self._buf).strip()
            if text:
                self.blocks.append({"type": tag, "text": text})

        if tag == "a":
            self._current_href = None

        if self._stack and self._stack[-1] == tag:
            self._stack.pop()

    def handle_data(self, data: str):
        if self._stack and self._stack[-1] in {"p", "h2", "h3", "h4", "li", "blockquote"}:
            self._buf.append(data)
