"""Entry for make.fun: The Excuse Your Agent Gives You."""
import os

# Entry text: 123 characters (limit 199), 1 line(s), no trailing newline.
ENTRY = 'I shipped the bug because the compiler approved it, the tests waved it through, and honestly, the code looked so confident.'

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
