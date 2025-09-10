import matplotlib.pyplot as plt
import numpy as np

def generate_aca_chart(household_size=3):
    fpl_base = 14580 + 5180 * (household_size - 1)
    agi_range = np.linspace(fpl_base, 4 * fpl_base, 300)
    base_credit = 6000
    lower_limit = fpl_base
    upper_limit = 4 * fpl_base
    reduction = np.maximum(0, (agi_range - lower_limit) / (upper_limit - lower_limit)) * base_credit
    estimated_ptc = np.maximum(0, base_credit - reduction)

    plt.figure(figsize=(10, 6))
    plt.plot(agi_range, estimated_ptc, label='Estimated Premium Tax Credit')
    plt.axvline(x=lower_limit, color='green', linestyle='--', label='FPL Start')
    plt.axvline(x=upper_limit, color='red', linestyle='--', label='Subsidy Phaseout Limit')
    plt.title(f"ACA Premium Tax Credit Phaseout for Household of {household_size}")
    plt.xlabel("Adjusted Gross Income (AGI)")
    plt.ylabel("Estimated PTC ($)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    filename = f"aca_chart_{household_size}.png"
    plt.savefig(filename)
    plt.close()
    return filename
