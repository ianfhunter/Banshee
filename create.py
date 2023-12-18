import yaml

def create_blocks():
    blocks = []
    for fn in "_data/creatures/*.yaml":
        blocks.append(yaml.parse(fn))
        
                 
    with open("_doc/20_Creatures/21_Blocks.md") as f:
        f.write("""
            ---
            title: Creature "Blocks"
            category: Creatures
            ---
        """)
        for b in blocks: 
            f.write(f"""
            **Name:** {b['name']}
             
            | --------- | ----- |
            | Health    | {b['stat']['health']} |
            | Attack    | {b['stat']['attack']} |
            | Defence    | {b['stat']['defence']} |
    
            **Tags:** {b['tags'].join(',')}
            **Tactics:** {b['tactics']}
            """)

def main():
    create_blocks()

if __name__ == "__main__":
    main()
