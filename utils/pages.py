import re

PAGES_RANGE_VALID_CHARACTERS = ["\\-"]
PAGES_LIST_VALID_CHARACTERS = ["\\,"]


def parse_pages_range(pages_range: str) -> list[int, int] | list[int, str] | list[str, int]:
    # Output is 0-based
    pages_range = pages_range.replace(" ", "")

    pattern = f"[^\\d{''.join(PAGES_RANGE_VALID_CHARACTERS)}]"
    if re.search(pattern, pages_range):
        raise ValueError(
            f"Invalid characters found in the input string. Only digits and the following characters are allowed: {[char.replace('\\', '') for char in PAGES_RANGE_VALID_CHARACTERS]
                                                                                                                   }.\nPages Range Input: {pages_range}"
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


def parse_pages_list(pages_list: str) -> list[int]:
    # Output is 0-based
    pages_list = pages_list.replace(" ", "")

    pattern = f"[^\\d{''.join(PAGES_LIST_VALID_CHARACTERS)}]"
    if re.search(pattern, pages_list):
        raise ValueError(
            f"Invalid characters found in the input string. Only digits and the following characters are allowed:{[char.replace('\\', '') for char in PAGES_LIST_VALID_CHARACTERS]
                                                                                                                  }.\nPages List Input: {pages_list}"
        )

    pages_list = pages_list.split(",")

    parsed_pages_list = []
    for page in pages_list:
        if page == "":
            continue
        parsed_pages_list.append(int(page) - 1)  # Make indeces 0-based

    return parsed_pages_list


def parse_pages_to_list(pages: str) -> list[int]:
    if "-" in pages:
        pages = parse_pages_range(pages)
        is_range = True
    else:  # a single number or list. 例: 1 or 1,2,3
        pages = parse_pages_list(pages)

    return pages


def handle_pages_range(pages_range: list, total_number_of_pages: int) -> list[int]:
    if pages_range[1] == "end":
        pages_range[1] = total_number_of_pages

    return range(pages_range[0], pages_range[1] + 1, 1)


def format_page_range(expanded_pages_range: list[int]) -> list[int, int]:
    return [expanded_pages_range[0] + 1, expanded_pages_range[-1] + 1]


def get_naming_string_from_pages_list(pages_list: list, is_range):
    naming_string = ""
    if is_range:
        naming_string = format_page_range(pages_list)
    else:
        naming_string = f"{[page + 1 for page in pages_list]}"

    return naming_string
