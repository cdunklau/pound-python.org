import sys
import pathlib
import subprocess
import shutil
import urllib.parse


HERE = pathlib.Path(__file__).parent
SOURCES_DIR = HERE.joinpath("sources")
OUTPUT_DIR = HERE.joinpath("pound-python.github.io")

# TODO: Maybe rework this to use the docutils API directly


def build_one(source_rst, dest_html, stylesheet_url):
    builder_path = pathlib.Path(sys.executable).parent.joinpath("rst2html5.py")
    args = [
        str(builder_path.resolve()),
        "--link-stylesheet",
        "--stylesheet",
        stylesheet_url,
        source_rst,
        dest_html,
    ]
    subprocess.run(args, check=True)


def main():
    stylesheet_parts = ("css", "style.css")
    stylesheet_src = SOURCES_DIR.joinpath(*stylesheet_parts)
    stylesheet_url = urllib.parse.quote("/".join(stylesheet_parts))
    stylesheet_dest = OUTPUT_DIR.joinpath(*stylesheet_parts)
    src_rst = SOURCES_DIR.joinpath("index.rst")
    rel_rst = src_rst.relative_to(SOURCES_DIR)
    dest_html = OUTPUT_DIR.joinpath(rel_rst.parent, rel_rst.stem + ".html")

    print("Writing {src} to {dest}".format(src=src_rst, dest=dest_html))
    build_one(src_rst, dest_html, stylesheet_url)
    print("Copying stylesheet")
    stylesheet_dest.parent.mkdir(exist_ok=True)
    shutil.copy2(stylesheet_src, stylesheet_dest)


if __name__ == "__main__":
    main()
