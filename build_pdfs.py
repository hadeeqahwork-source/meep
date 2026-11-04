"""Regenerate the PDFs after editing cv.html or slides.html.
Setup (once):  pip install playwright && playwright install chromium
Run:           python build_pdfs.py
"""
from pathlib import Path
from playwright.sync_api import sync_playwright

here = Path(__file__).parent
with sync_playwright() as p:
    b = p.chromium.launch()
    page = b.new_page()
    for src, out in (("cv.html", "Hadeeqah-CV.pdf"), ("slides.html", "Hadeeqah-Slides.pdf")):
        page.goto((here / src).as_uri())
        page.wait_for_timeout(300)
        page.pdf(path=str(here / out), prefer_css_page_size=True, print_background=True)
        print("Built", out)
    b.close()
