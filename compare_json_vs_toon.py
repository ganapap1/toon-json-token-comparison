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
    return json.dumps(obj, indent=2, ensure_ascii=False)


def demo_payload() -> Any:
    """
    Mock financial data with pre-calculated ratios - same as in index.html
    """
    return {
        "meta": {
            "company_name": "Demo Company",
            "currency": "USD",
            "note": "Financial data for demonstration",
        },
        "statements": {
            "income_statement": [
                {"Line Item": "Total Revenue", 2021: 14093300, 2022: 17025000, 2023: 14805900},
                {"Line Item": "Total Cost of Sales", 2021: 9603000, 2022: 11773700, 2023: 10258600},
                {"Line Item": "Gross Profit", 2021: 4490300, 2022: 5251300, 2023: 4547300},
                {"Line Item": "Operating Expenses", 2021: 2319800, 2022: 2510600, 2023: 2544100},
                {"Line Item": "Net Income", 2021: 1417400, 2022: 1844200, 2023: 1340100},
            ],
            "balance_sheet": [
                {"Line Item": "Cash", 2021: 300500, 2022: 1173400, 2023: 1080200},
                {"Line Item": "Inventory", 2021: 2065000, 2022: 1995300, 2023: 2043200},
                {"Line Item": "Total Assets", 2021: 9536000, 2022: 10329900, 2023: 10480300},
                {"Line Item": "Total Liabilities", 2021: 3442300, 2022: 3234000, 2023: 2747500},
            ],
        },
        "key_ratios": [
            {
                "year": "2023",
                "gross_profit_margin": 30.72,
                "net_profit_margin": 9.05,
                "operating_margin": 13.54,
                "roe": 17.33,
                "roa": 12.78,
                "current_ratio": 5.66,
                "quick_ratio": 4.92,
                "cash_ratio": 0.39,
                "debt_to_equity": 0.36,
                "debt_ratio": 0.26,
                "interest_coverage": 15.8,
                "asset_turnover": 1.41,
                "inventory_turnover": 5.02,
                "operating_cashflow_ratio": 2.15,
            },
            {
                "year": "2022",
                "gross_profit_margin": 30.84,
                "net_profit_margin": 10.83,
                "operating_margin": 16.08,
                "roe": 23.88,
                "roa": 17.86,
                "current_ratio": 3.55,
                "quick_ratio": 2.89,
                "cash_ratio": 0.36,
                "debt_to_equity": 0.42,
                "debt_ratio": 0.31,
                "interest_coverage": 18.2,
                "asset_turnover": 1.65,
                "inventory_turnover": 5.9,
                "operating_cashflow_ratio": 1.98,
            },
            {
                "year": "2021",
                "gross_profit_margin": 31.86,
                "net_profit_margin": 10.06,
                "operating_margin": 15.39,
                "roe": 22.97,
                "roa": 14.87,
                "current_ratio": 4.16,
                "quick_ratio": 3.42,
                "cash_ratio": 0.09,
                "debt_to_equity": 0.56,
                "debt_ratio": 0.36,
                "interest_coverage": 16.5,
                "asset_turnover": 1.48,
                "inventory_turnover": 4.65,
                "operating_cashflow_ratio": 2.24,
            },
        ],
    }


def compare_formats(data: Any, model: str = "gpt-4o-mini") -> None:
    # 1) Build prompt with JSON
    json_str = pretty_json(data)

    json_prompt = (
        "You are a senior financial analyst. Analyse the company's financial performance using the data I provide.\n\n"
        "Use the data below (in JSON or TOON format) and structure your answer under exactly these four headings (Markdown H2):\n\n"
        "## 1. Revenue and Profitability\n"
        "## 2. Balance Sheet and Financial Position\n"
        "## 3. Cash Flow Quality\n"
        "## 4. Key Ratios and Overall Assessment\n\n"
        f"```json\n{json_str}\n```\n"
    )

    # 2) Build prompt with TOON
    toon_str = toon_encode(data)

    toon_prompt = (
        "You are a senior financial analyst. Analyse the company's financial performance using the data I provide.\n\n"
        "Use the data below (in JSON or TOON format) and structure your answer under exactly these four headings (Markdown H2):\n\n"
        "## 1. Revenue and Profitability\n"
        "## 2. Balance Sheet and Financial Position\n"
        "## 3. Cash Flow Quality\n"
        "## 4. Key Ratios and Overall Assessment\n\n"
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
