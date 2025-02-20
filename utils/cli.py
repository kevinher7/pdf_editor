import re

PAGES_RAGNE_VALID_CHARACTERS = ["\\-"]


def parse_pages_range(pages_range: str) -> list[int]:
    pages_range = pages_range.replace(" ", "")

    pattern = f"[^\\d{''.join(PAGES_RAGNE_VALID_CHARACTERS)}]"
    pages_range = re.sub(pattern, "", pages_range)

    if pages_range.count("-") > 1:
        raise ValueError(
            "Invalid range. Range should only include one '-' character. Ex: '1-5'")
    elif "-" not in pages_range:
        raise ValueError(
            "Invalid range. Input didn't have a recognizable input rangle. Ranges should include (only) one '-' character. Ex: '1-5'")

    pages_range = pages_range.split("-")

    for idx, page in enumerate(pages_range):
        if int(page) == 0:
            raise ValueError(
                "Invalid range. Zero ('0') is not a valid page. Count starts at '1'")

        pages_range[idx] = int(page)

    return pages_range


parse_pages_range("1-2")
