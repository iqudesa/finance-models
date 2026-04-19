# 💰 IQuDesa Finance Models Toolkit
# Finance Models

![Docker](https://img.shields.io/badge/Docker-ready-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.36-red)
![Dash](https://img.shields.io/badge/Dash-2.14-orange)

Professional financial models for FinOps: DCF, LBO, Budget.

## Two Dashboard Versions

| Version | File | Port | Description |
|---------|------|------|-------------|
| **Streamlit** | `run_models.py` | 8501 | Quick prototype |
| **Dash** | `run_dash.py` | 8050 | Production-ready |

## Quickstart

```bash
# Streamlit
pip install -r requirements.txt
streamlit run run_models.py

# Dash
python run_dash.py
```

## Source Excel Files

| Model | File | Description |
|-------|------|-------------|
| DCF | `dcf.xlsx` | 5-year discounted cash flow |
| LBO | `lbo.xlsx` | Leveraged buyout returns |
| Budget | `budget.xlsx` | Monthly P&L |

## Live Demo

- Streamlit: http://localhost:8501
- Dash: http://localhost:8050

## License

MIT
