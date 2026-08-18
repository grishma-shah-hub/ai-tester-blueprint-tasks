from pathlib import Path

TEMPLATE_PATH = Path(__file__).parent.parent / "Templates" / "testcase_creator.md"
ANTI_HALLUCINATION_NOTE = (
    "\n\nFollow anti-hallucination guidelines strictly: only use facts present in the "
    "REQUIREMENTS above, mark any inference clearly, and write 'Not specified' for any "
    "missing information instead of guessing.\n"
)
COVERAGE_NOTE = (
    "\n\nGenerate a MINIMUM of 25 test cases — do not stop early. Comprehensively cover:\n"
    "- Positive scenarios (valid inputs, expected/happy-path behavior)\n"
    "- Negative scenarios (invalid inputs, error handling, unauthorized access)\n"
    "- Edge cases (boundary values, empty/null inputs, concurrency, unusual sequences)\n"
    "Continue generating test cases across all three categories until at least 25 rows "
    "are present in the output table.\n"
)


def build_prompt(ticket: dict, num_cases: str = "25+") -> str:
    template = TEMPLATE_PATH.read_text()

    feature = ticket.get("summary") or "Not specified"
    requirements = ticket.get("description") or "Not specified"

    prompt = (
        template
        .replace("[NUMBER]", num_cases)
        .replace("[FEATURE]", feature)
        .replace("[PASTE REQUIREMENTS HERE]", requirements)
    )
    return prompt + COVERAGE_NOTE + ANTI_HALLUCINATION_NOTE
