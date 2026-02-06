import os
import sys
import json
from pathlib import Path

def check_specs():
    print("--- Starting Project Chimera Spec-Check ---")
    
    # Define required spec directories
    required_dirs = [
        "specs/technical",
        "specs/functional",
        "specs/agent_architecture",
        "specs/technical/database"
    ]
    
    missing_dirs = []
    for d in required_dirs:
        if not Path(d).is_dir():
            missing_dirs.append(d)
            
    if missing_dirs:
        print(f"❌ Missing required spec directories: {', '.join(missing_dirs)}")
    else:
        print("✅ All required specification directories exist.")

    # Check for SOUL.md and strategy.md
    core_specs = {
        "specs/technical/database/strategy.md": "Database Strategy",
        "specs/agent_architecture/soul_definition.md": "SOUL Definition"
    }
    
    for path, name in core_specs.items():
        if Path(path).exists():
            print(f"✅ FOUND: {name} ({path})")
        else:
            print(f"❌ MISSING: {name} ({path})")

    # Basic markdown validation (ensure they aren't empty)
    md_files = list(Path("specs").rglob("*.md"))
    empty_files = [str(f) for f in md_files if f.stat().st_size == 0]
    
    if empty_files:
        print(f"❌ Found empty spec files: {', '.join(empty_files)}")
    else:
        print(f"✅ Validated {len(md_files)} specification documents.")

    print("--- Spec-Check Complete ---")
    
    if missing_dirs or any(not Path(p).exists() for p in core_specs):
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(check_specs())
