import glob
import yaml
import os

script_dir = os.path.dirname(os.path.realpath(__file__))


def create_blocks():
    blocks = []
    for fn in glob.glob(os.path.join(script_dir, "_data/creatures/*.yaml")):  
        with open(fn, "r") as file:
            block_data = yaml.safe_load(file)
            blocks.extend(block_data)
        
                 
    with open(os.path.join(script_dir, "_doc/20_Creatures/21_Blocks.md"), "w") as f:
        f.write("""---
title: Creature "Blocks"
category: Creatures
---
        """)
        for b in blocks: 
            print(f"Processing '{b['name']}'...")
            f.write(f"""
**Name:** {b['name']}
 
| --------- | ----- |
| Health    | {b['stats']['health']} |
| Attack    | {b['stats']['attack']} |
| Defence    | {b['stats']['defence']} |

**Tags:** {', '.join(b['tags'] if b['tags'] is not None else "")}

**Tactics:** {b['tactics']}

---
            """)

def main():
    create_blocks()

if __name__ == "__main__":
    main()
