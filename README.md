# Ethiopia Financial Inclusion Analysis 

This repository contains the data enrichment process and Exploratory Data Analysis (EDA) for Ethiopia's financial inclusion indicators (2011–2024). This work establishes the foundation for the 2025–2027 forecasting model.

---

## 📊 Task 1: Data Exploration and Enrichment

### Objective
To transform the sparse starter dataset into a high-fidelity unified schema by adding 2024-2025 observations, regulatory events, and impact links discovered through external research.

### Key Additions
* **Observations:** Integrated 2024 Findex estimates and National ID (Fayda) registration numbers to track "Enabler" progress.
* **Events:** Logged the **Mandatory Digital Fuel Payment** policy (2023) and the **Safaricom M-Pesa** market entry.
* **Impact Links:** Established modeled relationships between infrastructure density and digital payment usage with defined lags and magnitudes.

### Enrichment Log Summary
| Indicator Code | Record Type | Value/Status | Source | Confidence |
| :--- | :--- | :--- | :--- | :--- |
| `ACC_OWNERSHIP` | Observation | 49% (2024) | WB Findex | High |
| `INF_DIGITAL_ID` | Observation | 3.5M+ (2024) | NID Ethiopia | Medium |
| `EVENT_FUEL_DIGIT`| Event | Active (2023) | Min. of Transport | High |
| `USG_DIGITAL_PAY` | Impact Link | +15% Lift | Internal Model | Medium |

---

## 🔍 Task 2: Exploratory Data Analysis (EDA)

### Key Insights
1.  **The Multi-Homing Paradox:** While mobile money registrations exploded (100M+ accounts), formal account ownership grew by a smaller margin. This indicates that existing bank users are "multi-homing" (opening mobile wallets) rather than the unbanked entering the system for the first time.
2.  **The "Telebirr Effect":** A sharp inflection point in `USG_DIGITAL_PAYMENT` is visible post-May 2021, correlating with the launch of Telebirr and government-led digitization of fuel and services.
3.  **Infrastructure Correlation:** High correlation exists between 4G coverage expansion and Digital Payment usage, whereas physical ATM density shows a plateauing relationship with modern account ownership.
4.  **Gender Gap:** Data suggests that while digital tools are narrowing the gap, female access to mobile-money-only accounts still lags behind male counterparts by approximately 15%.



### Visualizations Included in Notebooks
* **Temporal Coverage Map:** Heatmap showing data density from 2011–2024.
* **Indicator Growth Rates:** Comparative bar charts of CAGR for different inclusion pillars.
* **Event Timeline:** An interactive timeline overlaying policy milestones onto the national inclusion trend.

---

## 🛠️ How to Run

### 1. Environment Setup
```bash
pip install -r requirements.txt
```

Run Enrichment (Task 1)
Execute the enrichment notebook to generate the unified processed dataset.

``` Location: notebooks/task_1_enrichment.ipynb```
3. Run EDA (Task 2)
View the analysis, correlations, and key visualizations.

```Location: notebooks/task_2_eda.ipynb```

### 📂 Data Quality Assessment

Sparsity: High. Historical Findex data is limited to specific years (2011, 2014, 2017, 2021, 2024).

Consistency: High. The unified schema ensures all records (events vs. observations) are interoperable.

Limitation: A lack of granular regional data (e.g., Tigray vs. Afar) limits the ability to model regional-specific policy impacts.