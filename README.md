# Mutual Fund Analytics

## Day 1: Project Setup + Data Ingestion

### Completed Tasks
- Created project structure
- Initialized Git repository
- Created GitHub repository
- Installed Python dependencies
- Generated requirements.txt
- Fetched live NAV data from MFAPI
- Downloaded NAV history for:
  - SBI Bluechip
  - ICICI Bluechip
  - Nippon Large Cap
  - Axis Bluechip
  - Kotak Bluechip
- Saved datasets in data/raw
- Performed basic data quality checks

### Data Quality Summary
- No missing values in date column
- No missing values in nav column
- NAV values are numeric
- Historical NAV data successfully loaded and validated

### Repository Structure

```text
data/
 ├── raw/
 ├── processed/
notebooks/
sql/
dashboard/
reports/
```

## Data Exploration Summary

### Unique Categories
- Equity
- Debt

### Unique Risk Categories
- Low
- Moderate
- Moderately High
- High
- Very High

### Data Quality Checks
- No missing values in date columns
- No missing values in NAV columns
- Numeric fields validated
- Historical NAV data loaded and validated successfully