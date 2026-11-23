"""Six Words, One Story — make.fun entry.

Writes the six-word story to /output/entry.txt, no trailing newline.
"""

import os

STORY = "Grandma's recipe died with her. Almost."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    words = STORY.split()
    assert len(words) == 6, f"story must be exactly six words, got {len(words)}"
    assert 1 <= len(STORY) <= 60, f"story must be 1-60 chars, got {len(STORY)}"
    assert STORY.strip() == STORY, "story must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
