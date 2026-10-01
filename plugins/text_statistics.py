"""Text Statistics Arcade Plugin."""

AUTHOR = "lui01212"
APP_NAME = "Text Statistics Analyzer"

DEFAULT_TEXT = (
    "Open source software empowers developers worldwide.\n"
    "Collaboration and learning drive continuous innovation.\n"
    "Small consistent contributions create lasting impact."
)


def analyze_text(text: str) -> dict:
    """Calculates character, word, and line statistics for the given text."""
    lines = text.splitlines()
    line_count = len(lines)
    word_count = len(text.split())
    char_count = len(text)
    char_no_spaces = len(text.replace(" ", "").replace("\t", "").replace("\n", "").replace("\r", ""))

    return {
        "lines": line_count,
        "words": word_count,
        "chars": char_count,
        "chars_no_space": char_no_spaces,
    }


def run() -> str:
    """Calculates and returns formatted text statistics."""
    sample = DEFAULT_TEXT
    stats = analyze_text(sample)

    output = (
        f"[Text Statistics]\n"
        f"    Sample text preview: \"{sample.splitlines()[0]}...\"\n"
        f"    - Lines: {stats['lines']}\n"
        f"    - Words: {stats['words']}\n"
        f"    - Characters: {stats['chars']} (excluding whitespace: {stats['chars_no_space']})"
    )
    return output


if __name__ == "__main__":
    print(f"Plugin: {APP_NAME} by {AUTHOR}")
    print(run())
