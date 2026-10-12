AUTHOR = "Daniel Belville Jr."
APP_NAME = "Text Statistics"


def run():
    sample_text = """Students Arcade is a collection of small Python activities.
Each plugin follows the same interface and can be discovered by the launcher."""

    character_count = len(sample_text)
    word_count = len(sample_text.split())
    line_count = len(sample_text.splitlines())

    return (
        f"{APP_NAME}: "
        f"{character_count} characters, "
        f"{word_count} words, "
        f"{line_count} lines"
    )