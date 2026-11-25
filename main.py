import os

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/tmp/oneline")
entry_path = os.path.join(output_dir, "output", "entry.txt")

os.makedirs(os.path.dirname(entry_path), exist_ok=True)

joke = "My boss told me to have a good day so I went home early to nap"
with open(entry_path, "w", encoding="utf-8") as f:
    f.write(joke)