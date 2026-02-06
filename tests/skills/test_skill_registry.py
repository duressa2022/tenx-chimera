REQUIRED_SKILLS = {
    "skill_trend_fetch",
    "skill_content_generation",
    "skill_publish_content",
    "skill_engagement_manager",
}

REQUIRED_FILES = {
    "README.md",
    "contract.json",
}

def test_required_skills_exist(skills_dir):
    existing = {d.name for d in skills_dir.iterdir() if d.is_dir()}
    missing = REQUIRED_SKILLS - existing
    assert not missing, f"Missing required skills: {missing}"

def test_each_skill_has_required_files(skills_dir):
    for skill_dir in skills_dir.iterdir():
        if not skill_dir.name.startswith("skill_"):
            continue
        for fname in REQUIRED_FILES:
            assert (skill_dir / fname).exists(), \
                f"{skill_dir.name} missing {fname}"
