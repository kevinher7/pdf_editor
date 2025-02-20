import re

PAGES_RANGE_VALID_CHARACTERS = ["\\-"]


def parse_pages_range(pages_range: str) -> list[int, int] | list[int, str] | list[str, int]:
    pages_range = pages_range.replace(" ", "")

    pattern = f"[^\\d{''.join(PAGES_RANGE_VALID_CHARACTERS)}]"
    if re.search(pattern, pages_range):
        raise ValueError(
            f"Invalid characters found in the input string. Only digits and the following characters are allowed: {PAGES_RANGE_VALID_CHARACTERS}.\nPages Range Input: {pages_range}"
        )

    if pages_range.count("-") > 1:
        raise ValueError(
            "Invalid range. Range should only include one '-' character. Ex: '1-5'")
    elif "-" not in pages_range:
        raise ValueError(
            "Invalid range. Input didn't have a recognizable input range. Ranges should include (only) one '-' character. Ex: '1-5'")

    pages_range = pages_range.split("-")

    # From the begininng and until the end.例: -10 and 10-
    pages_range[0] = 1 if pages_range[0] == "" else int(pages_range[0])
    pages_range[1] = "end" if pages_range[1] == "" else int(pages_range[1])

    for idx, page in enumerate(pages_range):
        if isinstance(page, int):
            if int(page) == 0:
                raise ValueError(
                    "Invalid range. Zero ('0') is not a valid page. Count starts at '1'")
            pages_range[idx] = page - 1  # Make range go from 0 to n-1

    return pages_range
