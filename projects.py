PROJECTS = [
    {
        "slug": "retail-forecast",
        "domain": "Retail", "year": "2025", "role": "Lead data scientist",
        "title": "Demand forecasting for weekly replenishment",
        "blurb": "Weekly SKU-store forecasts for 1,240 lines, replacing a spreadsheet model that buyers overrode by hand.",
        "preview_label": "Forecast vs actual",
        "headline_label": "Forecast error", "headline_value": "MAPE 8.4%",
        "stack": ["Python", "LightGBM", "Prophet", "Airflow", "BigQuery"],
        "metrics": [
            {"label": "Forecast error", "value": "8.4%", "note": "MAPE, down from 19.1%"},
            {"label": "Stock-outs", "value": "-23%", "note": "13 weeks post-launch"},
            {"label": "SKU-store pairs", "value": "1,240", "note": "Refreshed weekly"},
            {"label": "Runtime", "value": "6 min", "note": "Full retrain"},
        ],
        "problem1": "Buyers placed replenishment orders from a spreadsheet that averaged the last four weeks of sales. It ignored promotions, school terms and payday cycles, so fast lines ran out mid-month while slow lines sat in the back of the store.",
        "problem2": "The brief was a forecast the buying team would trust enough to stop overriding: accurate on promotional weeks, refreshed before Monday planning, and explainable line by line.",
        "chart_main": "Forecast vs actual, 13-week holdout",
        "chart_b": "Error by SKU category", "chart_c": "Promotion uplift residuals",
        "lessons": [
            {"n": "01", "text": "Most of the gain came from features, not models. Promotion flags and payday-week indicators moved error further than any tuning round."},
            {"n": "02", "text": "Buyers accepted the forecast once each line showed its three biggest drivers. Accuracy alone did not change behaviour."},
            {"n": "03", "text": "Holding out entire weeks rather than random rows exposed a leak that random splits hid completely."},
        ],
        "links": [
            {"label": "Modelling notebook", "url": "github.com/lebohang/retail-forecast"},
            {"label": "Feature pipeline", "url": "github.com/lebohang/retail-forecast/pipeline"},
        ],
    },
    {
        "slug": "thin-file-scorecard",
        "domain": "Lending", "year": "2025", "role": "Data scientist",
        "title": "Credit default scoring on thin-file applicants",
        "blurb": "A scorecard for applicants with no bureau history, built to pass a model risk review as well as a metric bar.",
        "preview_label": "ROC / KS curves",
        "headline_label": "Discrimination", "headline_value": "AUC 0.87",
        "stack": ["Python", "XGBoost", "scikit-learn", "SHAP", "Postgres"],
        "metrics": [
            {"label": "AUC", "value": "0.87", "note": "Out-of-time sample"},
            {"label": "KS", "value": "0.41", "note": "At approval cut-off"},
            {"label": "Approval rate", "value": "+11%", "note": "At constant loss rate"},
            {"label": "Features", "value": "34", "note": "From 260 candidates"},
        ],
        "problem1": "Roughly a third of applicants had too little bureau history to score, so they were declined by default. The portfolio was leaving good borrowers on the table and had no evidence about which of them were actually risky.",
        "problem2": "The model had to work from transactional and device data only, stay monotonic in the features the credit committee cared about, and produce reason codes for every decline.",
        "chart_main": "ROC and KS by score band",
        "chart_b": "SHAP feature importance", "chart_c": "Score distribution by outcome",
        "lessons": [
            {"n": "01", "text": "Monotonic constraints cost about 0.01 AUC and bought the model a signed-off risk review. Worth it."},
            {"n": "02", "text": "Reject inference changed the picture more than any model choice, and it is the part of the work that needed the most documentation."},
            {"n": "03", "text": "Reason codes had to be written with the collections team, not derived automatically from SHAP."},
        ],
        "links": [
            {"label": "Scorecard notebook", "url": "github.com/lebohang/thin-file-scorecard"},
            {"label": "Validation report", "url": "github.com/lebohang/thin-file-scorecard/validation"},
        ],
    },
    {
        "slug": "fleet-routing",
        "domain": "Logistics", "year": "2024", "role": "Optimisation lead",
        "title": "Delivery route optimisation for a 40-vehicle fleet",
        "blurb": "Daily vehicle routing with time windows and load limits, solved in the twelve-minute gap before drivers leave.",
        "preview_label": "Route map placeholder",
        "headline_label": "Distance saved", "headline_value": "-14% km",
        "stack": ["Python", "OR-Tools", "OSRM", "FastAPI", "Docker"],
        "metrics": [
            {"label": "Distance", "value": "-14%", "note": "Per delivery day"},
            {"label": "Planning time", "value": "4 min", "note": "Was 90 min manual"},
            {"label": "On-time rate", "value": "96%", "note": "Up from 88%"},
            {"label": "Stops per day", "value": "870", "note": "Across 40 vehicles"},
        ],
        "problem1": "Three planners split the country by region and built routes by hand every morning. Their plans were good but inconsistent, and nobody could say what a route was supposed to cost.",
        "problem2": "The solver had to respect delivery windows, vehicle capacity and driver shift length, and return a plan fast enough to run twice if a vehicle broke down.",
        "chart_main": "Solved routes, one delivery day",
        "chart_b": "Cost per stop by depot", "chart_c": "Solver convergence",
        "lessons": [
            {"n": "01", "text": "The hard constraint was social, not mathematical. Planners needed to edit the solution, so the tool ships with manual override and re-solve."},
            {"n": "02", "text": "Road-network distances rather than straight lines accounted for most of the realised saving."},
            {"n": "03", "text": "A five-second time limit and a good first-solution heuristic beat a long search almost every day."},
        ],
        "links": [
            {"label": "Solver service", "url": "github.com/lebohang/fleet-routing"},
            {"label": "Benchmark notebook", "url": "github.com/lebohang/fleet-routing/bench"},
        ],
    },
    {
        "slug": "invoice-extract",
        "domain": "Operations", "year": "2024", "role": "Data scientist",
        "title": "Document extraction for supplier invoices",
        "blurb": "OCR and entity extraction that replaced a three-person manual capture process for 4,000 invoices a month.",
        "preview_label": "Field accuracy matrix",
        "headline_label": "Field accuracy", "headline_value": "92.6%",
        "stack": ["Python", "PaddleOCR", "spaCy", "Label Studio", "Redis"],
        "metrics": [
            {"label": "Field accuracy", "value": "92.6%", "note": "Across 9 fields"},
            {"label": "Capture time", "value": "11 min", "note": "Was 6 hours daily"},
            {"label": "Documents", "value": "4,000", "note": "Per month"},
            {"label": "Manual review", "value": "8%", "note": "Low-confidence only"},
        ],
        "problem1": "Invoices arrived as scans and photographs in a shared mailbox. Three people typed nine fields each into the finance system, and the backlog grew every month-end.",
        "problem2": "Full automation was never the target. The goal was to capture the confident majority and route the rest to a person with the fields pre-filled.",
        "chart_main": "Confidence vs accuracy by field",
        "chart_b": "Error types by supplier template", "chart_c": "Queue depth before and after",
        "lessons": [
            {"n": "01", "text": "Confidence calibration mattered more than raw accuracy, because it decides what a human ever sees."},
            {"n": "02", "text": "Twelve supplier templates covered 78% of volume. Handling those well was the whole project."},
            {"n": "03", "text": "The review interface needed as much design attention as the model, and it is what finance judged the project on."},
        ],
        "links": [
            {"label": "Extraction pipeline", "url": "github.com/lebohang/invoice-extract"},
            {"label": "Annotation guide", "url": "github.com/lebohang/invoice-extract/labels"},
        ],
    },
    {
        "slug": "load-forecast",
        "domain": "Energy", "year": "2023", "role": "Analyst",
        "title": "Short-term load forecasting for a municipal grid",
        "blurb": "Day-ahead half-hourly load forecasts used for procurement, with weather and load-shedding schedules as inputs.",
        "preview_label": "Half-hourly load curve",
        "headline_label": "Forecast error", "headline_value": "MAPE 3.1%",
        "stack": ["Python", "LSTM", "PyTorch", "pandas", "Grafana"],
        "metrics": [
            {"label": "Forecast error", "value": "3.1%", "note": "Day-ahead MAPE"},
            {"label": "Peak error", "value": "4.8%", "note": "Evening peak only"},
            {"label": "Horizon", "value": "48", "note": "Half-hourly steps"},
            {"label": "Retrain", "value": "Weekly", "note": "Automated"},
        ],
        "problem1": "Procurement bought day-ahead energy from a rule-of-thumb profile. On cold evenings the municipality bought short and paid penalty rates, and nobody could forecast the effect of a load-shedding stage change.",
        "problem2": "The model needed a 48-step half-hourly horizon, temperature forecasts as an input, and an explicit handle for scheduled outages.",
        "chart_main": "Predicted vs actual load, one week",
        "chart_b": "Error by hour of day", "chart_c": "Sensitivity to temperature",
        "lessons": [
            {"n": "01", "text": "A well-featured gradient boosting baseline was within a point of the LSTM and far easier to hand over. The LSTM won on peak hours only."},
            {"n": "02", "text": "Outage schedules were published as PDFs. Parsing them reliably was half the engineering effort."},
            {"n": "03", "text": "Reporting error at the evening peak rather than on average is what made the forecast credible to procurement."},
        ],
        "links": [
            {"label": "Forecasting notebook", "url": "github.com/lebohang/load-forecast"},
            {"label": "Monitoring dashboard", "url": "github.com/lebohang/load-forecast/dash"},
        ],
    },
]

SKILL_GROUPS = [
    {"label": "Languages and querying", "tools": ["Python", "SQL", "R", "bash"]},
    {"label": "Modelling", "tools": ["scikit-learn", "XGBoost", "LightGBM", "PyTorch", "statsmodels", "OR-Tools"]},
    {"label": "Data and pipelines", "tools": ["Airflow", "dbt", "Spark", "BigQuery", "Postgres", "Redis"]},
    {"label": "Delivery and MLOps", "tools": ["Docker", "FastAPI", "MLflow", "Git", "Grafana", "AWS"]},
]


def get_project(slug):
    return next((p for p in PROJECTS if p["slug"] == slug), None)


def get_next_project(slug):
    idx = next((i for i, p in enumerate(PROJECTS) if p["slug"] == slug), 0)
    return PROJECTS[(idx + 1) % len(PROJECTS)]
