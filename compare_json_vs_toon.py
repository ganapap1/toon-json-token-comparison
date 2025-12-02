# compare_json_vs_toon.py
#
# Simple demo to compare JSON vs TOON for LLM prompts.
# - Uses toon-python for TOON encoding
# - Uses tiktoken to count tokens (gpt-4o / gpt-4o-mini style)

import json
from typing import Any

import tiktoken
from toon import encode as toon_encode  # from toon-python


def count_tokens(text: str, model: str = "gpt-4o-mini") -> int:
    """
    Count tokens in a string for a given OpenAI model using tiktoken.
    """
    try:
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        # Fallback for newer/unknown models: use o200k_base (4o family)
        encoding = tiktoken.get_encoding("o200k_base")
    return len(encoding.encode(text))


def pretty_json(obj: Any) -> str:
    """
    Deterministic, pretty JSON for fair comparison.
    """
    return json.dumps(obj, indent=2, ensure_ascii=False, sort_keys=True)


def demo_payload() -> Any:
    """
    Example structured data you might send to an LLM.
    Feel free to change this to your real use case:
    - transaction logs
    - medical records
    - GL lines
    - survey responses, etc.
    """
    return {
        "users": [
            {
                "id": 1,
                "name": "Alice",
                "role": "admin",
                "country": "IN",
                "active": True,
                "score": 87.5,
            },
            {
                "id": 2,
                "name": "Bob",
                "role": "user",
                "country": "AE",
                "active": False,
                "score": 73.0,
            },
            {
                "id": 3,
                "name": "Charlie",
                "role": "analyst",
                "country": "UK",
                "active": True,
                "score": 91.2,
            },
        ],
        "meta": {
            "source_system": "CRM",
            "snapshot_at": "2025-11-30T10:15:00Z",
            "description": "User access & scores for quarterly review.",
        },
    }


def compare_formats(data: Any, model: str = "gpt-4o-mini") -> None:
    # 1) Build prompt with JSON
    json_str = pretty_json(data)

    json_prompt = (
        "You are an AI analyst.\n"
        "Use the following JSON data to summarise user roles and highlight risky users.\n\n"
        f"DATA_JSON:\n{json_str}\n"
    )

    # 2) Build prompt with TOON
    toon_str = toon_encode(data)

    toon_prompt = (
        "You are an AI analyst.\n"
        "Use the following TOON data to summarise user roles and highlight risky users.\n\n"
        "DATA_TOON:\n"
        f"{toon_str}\n"
    )

    # 3) Measure
    json_chars = len(json_prompt)
    toon_chars = len(toon_prompt)

    json_tokens = count_tokens(json_prompt, model=model)
    toon_tokens = count_tokens(toon_prompt, model=model)

    # 4) Report
    print("=== FORMAT COMPARISON ===")
    print(f"Model: {model}")
    print()

    print("JSON prompt:")
    print(json_prompt)
    print(f"\nJSON length : {json_chars} chars")
    print(f"JSON tokens : {json_tokens}")

    print("\n------------------------------\n")

    print("TOON prompt:")
    print(toon_prompt)
    print(f"\nTOON length : {toon_chars} chars")
    print(f"TOON tokens : {toon_tokens}")

    # 5) Savings
    token_diff = json_tokens - toon_tokens
    pct_saving = (token_diff / json_tokens * 100) if json_tokens > 0 else 0.0

    print("\n==============================")
    print(f"Token saving : {token_diff} tokens")
    print(f"Saving %      : {pct_saving:.2f}%")
    print("==============================")


if __name__ == "__main__":
    data = demo_payload()
    compare_formats(data, model="gpt-4o-mini")  # or your actual model name
