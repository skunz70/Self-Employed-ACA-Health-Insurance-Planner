from fastapi import FastAPI
from pydantic import BaseModel
from aca_chart import generate_aca_chart

app = FastAPI()

class ACARequest(BaseModel):
    agi: float
    household_size: int
    state: str
    filing_status: str

@app.post("/aca_planner")
def aca_planner(data: ACARequest):
    federal_poverty_level = 14580 + 5180 * (data.household_size - 1)
    lower_limit = 1.0 * federal_poverty_level
    upper_limit = 4.0 * federal_poverty_level

    within_range = lower_limit <= data.agi <= upper_limit

    base_credit = 6000  # Simulated average credit value
    reduction = max(0, (data.agi - lower_limit) / (upper_limit - lower_limit)) * base_credit
    estimated_ptc = max(0, base_credit - reduction)

    warning = ""
    if data.agi > upper_limit:
        warning = "Warning: AGI exceeds ACA subsidy limit. You may lose all credits."

    return {
        "estimated_premium_tax_credit": round(estimated_ptc, 2),
        "fpl_range": f"${round(lower_limit)} - ${round(upper_limit)}",
        "within_subsidy_range": within_range,
        "warning": warning
    }
