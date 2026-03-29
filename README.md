# Stock Price Predictor

Lightweight analyzers that score a stock across multiple signals and produce a final recommendation.

Included scripts

- CompanyProfileAnalyzer.py
- GraphAnalyzer.py
- NewsAnalyzer.py
- PriceAndMarketDataAnalyzer.py
- ValuationMetricsAnalyzer.py
- FinalRecommendation.py

Quick start (Windows PowerShell)

1. Create and activate a virtual environment:

```powershell
python -m venv .venv
.\\.venv\\Scripts\\Activate.ps1
```

2. Install dependencies:

```powershell
python -m pip install yfinance pandas numpy scikit-learn nltk serpapi
```

3. (Optional) Configure the SerpAPI key for news analysis:

```powershell
$env:SERP_API_KEY="your_key_here"
```

4. Run individual analyzers:

```powershell
python CompanyProfileAnalyzer.py
python GraphAnalyzer.py
python NewsAnalyzer.py
python PriceAndMarketDataAnalyzer.py
python ValuationMetricsAnalyzer.py
```

5. Run the combined recommendation:

```powershell
python FinalRecommendation.py
```

Notes

- Default ticker symbol is hardcoded as `COALINDIA.NS` in each analyzer. Update the `ticker_symbol` (and company name in NewsAnalyzer) to analyze a different stock.
- NLTK downloads the VADER lexicon on first run.
- The news analyzer expects a SerpAPI key. If you set `SERP_API_KEY` as an environment variable, you should update NewsAnalyzer to read it from the environment instead of a hardcoded value.

License: See the LICENSE file.
