def balanced_parentheses(parentheses: str) -> bool:
    stack = []
    bracket_pairs = {"(": ")", "[": "]", "{": "}"}
    for bracket in parentheses:
        if bracket in bracket_pairs:
            stack.append(bracket)
        elif bracket in (")", "]", "}") and (
            not stack or bracket_pairs[stack.pop()] != bracket
        ):
            return False
    return not stack


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    examples = ["((()))", "(())", "{(())}"]
    for example in examples:
        print(f"{example} is{'' if balanced_parentheses(example) else ' not'} balanced")
