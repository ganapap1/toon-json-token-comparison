# TOON vs JSON Token Comparison Tool

[![Live Demo](https://img.shields.io/badge/demo-live-brightgreen)](https://ganapap1.github.io/toon-json-token-comparison/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A powerful interactive web tool that demonstrates token efficiency differences between JSON and TOON (Token Oriented Object Notation) formats when sending structured data to Large Language Models (LLMs).

![TOON vs JSON Comparison Tool](screenshot.png)

## 🎯 What Does This Tool Do?

This tool performs **real-time comparisons** by sending identical data to LLM APIs in both formats:
- **JSON** (traditional format)
- **TOON** (Token Oriented Object Notation)

It then measures and displays the actual token usage, cost savings, and efficiency metrics.

## ✨ Key Features

### 📊 Real-Time Token Analysis
- Live comparison using OpenAI, Anthropic, or Google AI APIs
- Actual token counts from LLM providers (not estimates)
- Side-by-side format visualization

### 💰 Cost Impact Calculator
- Calculate savings for 1K, 10K, and 100K requests/month
- Support for multiple models:
  - GPT-4o Mini ($0.15/1M tokens)
  - GPT-4o ($2.50/1M tokens)
- Real pricing based on actual input token savings

### 📈 Comprehensive Metrics
- **Input Token Savings %**: Shows compression efficiency (typically 30-50%)
- **Output Token Difference**: AI response variance
- **Total Token Savings**: Net tokens saved per request
- **Total Savings %**: Overall reduction across request-response cycle

### 🎨 Interactive UI
- **Collapsible Summary**: Detailed explanation of how TOON achieves savings
- **Hover Tooltips**: In-depth metric explanations with calculations
- **Dynamic Cost Table**: Visual representation of savings at scale
- **Responsive Design**: Works on desktop, tablet, and mobile

### 🚀 Demo Data
- Pre-loaded financial data for quick testing
- "Load Demo Financial Data" button for instant comparison

## 🌐 Interactive Web Demo

**Try it now:** [Live Demo](https://ganapap1.github.io/toon-json-token-comparison/)

- ✅ Single-file HTML application (no installation required)
- ✅ Real-time comparison with OpenAI, Anthropic, and Google AI APIs
- ✅ Side-by-side JSON vs TOON display
- ✅ Live token counting and savings calculation
- ✅ Beautiful, responsive UI with dark green theme
- ✅ Perfect for demonstrations and presentations

## 🧪 How TOON Works

TOON uses a **tabular format** that eliminates repetitive JSON keys:

**JSON (Traditional):**
```json
[
  {"name": "Alice", "age": 30, "city": "NYC"},
  {"name": "Bob", "age": 25, "city": "LA"},
  {"name": "Carol", "age": 35, "city": "Chicago"}
]
```

**TOON (Optimized):**
```
name|age|city
Alice|30|NYC
Bob|25|LA
Carol|35|Chicago
```

By declaring keys once as headers (like a spreadsheet), TOON eliminates redundant tokens. This typically saves **30-50% on input tokens**!

## 📊 Example Results

Based on the demo financial data:
- **Input Token Savings**: 41.45% (485 tokens saved)
- **Total Savings**: 599 tokens per request
- **Monthly Cost Savings** (at 10K requests):
  - GPT-4o Mini: $0.73/month
  - GPT-4o: $12.13/month

At scale (100K requests/month):
- **48.5 million tokens saved**
- GPT-4o savings: **$121.25/month**

## 📦 Installation & Usage

### Option 1: Use Live Demo
Visit: [https://ganapap1.github.io/toon-json-token-comparison/](https://ganapap1.github.io/toon-json-token-comparison/)

### Option 2: Clone and Run Locally
```bash
git clone https://github.com/ganapap1/toon-json-token-comparison.git
cd toon-json-token-comparison
# Open index.html in your browser
```

### Option 3: Run Python Scripts

Install requirements:
```bash
pip install pandas numpy python-dotenv openai tiktoken toon-python openpyxl
```

Run demos:
```bash
# Simple comparison
python compare_json_vs_toon.py

# Quick test without API
python test_demo.py

# Full financial demo with API
python json_vs_toon_demo.py
```

## 🔧 How to Use the Web App

1. **Select Your LLM Provider**
   - OpenAI (GPT models)
   - Anthropic (Claude models)
   - Google AI (Gemini models)

2. **Choose a Model**
   - GPT-4o Mini (cheapest)
   - GPT-4o
   - Claude Sonnet/Opus
   - Gemini Pro/Flash

3. **Enter Your API Key**
   - Get keys from provider dashboards
   - Keys are stored locally in your browser only

4. **Load Demo Data or Paste Your Own**
   - Click "Load Demo Financial Data" for a quick test
   - Or paste your own JSON array data

5. **Compare Formats**
   - Click "Compare Formats" button
   - View real-time results with token counts and cost analysis

## 📖 Understanding the Metrics

### Input Token Savings %
The percentage of tokens saved on input data. This directly translates to cost savings since you pay for input tokens.

**Expected Range**: 30-50% for structured datasets

### Output Token Difference
AI response length variance. Can be positive or negative due to the non-deterministic nature of LLMs.

**Why it varies**: Both formats receive identical instructions, but AI responses have natural 5-10% variation.

### Total Token Savings
Net tokens saved per request (input savings ± output variance).

**Scale it up**: Multiply by monthly request volume for total impact.

### Total Savings %
Overall reduction across the entire request-response cycle.

**Why it's lower**: Includes both compressed input and uncompressed output.

## Project Structure

```
AI_Json_Toon/
├── compare_json_vs_toon.py    # Simple comparison demo
├── json_vs_toon_demo.py        # Financial analysis demo with API calls
├── test_demo.py                # Quick test without API calls
├── uploads/
│   └── Financial_Statement.csv # Sample financial data
└── README.md
```

## Requirements

Install required packages:
```bash
pip install pandas numpy python-dotenv openai tiktoken toon-python openpyxl
```

## Running the Demos

### 1. Simple Comparison
```bash
python compare_json_vs_toon.py
```
Shows side-by-side comparison of JSON vs TOON for user data.

### 2. Financial Demo (Quick Test)
```bash
python test_demo.py
```
Shows token comparison for financial statements without API calls.

### 3. Full Financial Demo (with API)
```bash
python json_vs_toon_demo.py
```
Sends both JSON and TOON prompts to OpenAI API for real-world comparison.

**Note:** You need an OpenAI API key in `.env` file:
```
OPENAI_API_KEY=your_key_here
```

## Sample Output

### JSON Format
```json
{
  "users": [
    {
      "id": 1,
      "name": "Alice",
      "role": "admin",
      "country": "IN",
      "active": true,
      "score": 87.5
    }
  ]
}
```

### TOON Format
```
users[3,]{id,name,role,country,active,score}:
  1,Alice,admin,IN,true,87.5
  2,Bob,user,AE,false,73.0
  3,Charlie,analyst,UK,true,91.2
```

## Use Cases

TOON is ideal for:
- Financial data (statements, transactions, GL entries)
- Tabular data with repeated structures
- Database query results
- Survey responses
- Log files and analytics data
- Any structured data sent to LLMs

## Cost Savings Example

Using GPT-4o-mini at **$0.150 per 1M input tokens**:

For 1,000 financial analysis prompts:
- JSON: 2,858 tokens × 1,000 = 2,858,000 tokens = **$0.43**
- TOON: 1,444 tokens × 1,000 = 1,444,000 tokens = **$0.22**
- **Savings: $0.21 per 1,000 prompts (49%)**

For enterprise scale (1M prompts/year):
- **Annual savings: $210**

## Technical Details

- **Model**: gpt-4o-mini
- **Token Counter**: tiktoken (o200k_base encoding)
- **TOON Library**: toon-python (0.1.2)
- **Data Source**: Financial statements (2020-2023)

## YouTube Video Demo Script

1. **Introduction** - Explain token costs in LLM APIs
2. **Problem** - Show verbose JSON format
3. **Solution** - Introduce TOON format
4. **Demo 1** - Run simple comparison (43.5% savings)
5. **Demo 2** - Run financial demo (49.5% savings)
6. **Cost Analysis** - Show real-world cost implications
7. **Conclusion** - When to use TOON

## Files Fixed

- ✅ Fixed unterminated string in `json_vs_toon_demo.py`
- ✅ Fixed import error (`toon_format` → `toon`)
- ✅ Fixed Windows unicode issues (replaced emoji with ASCII)
- ✅ Added complete main() function with API integration
- ✅ Created test_demo.py for quick testing

## 🎨 Features Showcase

### Color-Coded Metrics
- 🟢 **Green**: Positive savings
- 🟡 **Amber**: Neutral (AI response variance)
- 🔴 **Red**: Negative values (rare)

### Intelligent Tooltips
Hover over the ⓘ icons to see:
- Detailed calculations
- Expected ranges
- Why metrics matter

### Responsive Design
- Desktop: Full feature set with hover tooltips
- Mobile: Touch-friendly with tap tooltips
- Tablet: Optimized layout

## 🛠️ Technology Stack

- **Frontend**: Pure HTML5, CSS3, JavaScript (ES6+)
- **APIs**: OpenAI, Anthropic, Google AI
- **Styling**: Modern CSS with gradients and animations
- **Python Backend** (optional): pandas, numpy, tiktoken, toon-python
- **No Dependencies**: Web app works in any modern browser

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Development Guidelines
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Related Resources

- [TOON Python Library](https://pypi.org/project/toon-python/) - Python implementation
- [OpenAI API](https://platform.openai.com/) - GPT models
- [Anthropic API](https://www.anthropic.com/) - Claude models
- [Google AI](https://ai.google.dev/) - Gemini models

## 👤 Author

**Ganapathy**
- GitHub: [@ganapap1](https://github.com/ganapap1)
- Repository: [toon-json-token-comparison](https://github.com/ganapap1/toon-json-token-comparison)

## 🙏 Acknowledgments

- Token Oriented Object Notation (TOON) format
- OpenAI, Anthropic, and Google AI for their LLM APIs
- The open-source community

## 📮 Support

If you find this tool helpful, please consider:
- ⭐ Starring the repository
- 🐛 Reporting bugs via [Issues](https://github.com/ganapap1/toon-json-token-comparison/issues)
- 💡 Suggesting new features

---

**Made with 💚 for the LLM community** | Demonstrating real-world token efficiency
