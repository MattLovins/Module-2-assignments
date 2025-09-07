#initialization
FLOAT_LABOR_COST_PER_HOUR = 30.00
FLOAT_WHOLESALE_MULTIPIER = 1.2
floatCostOfLabor = 0.0
floatNumberOfHours = 0.0
floatWholesaleCostMultiplied = 0.0
floatTotalCost = 0.0
floatCostOfMaterials = 0.0

#get data
floatNumberOfHours = float(input("Please enter the projected number of hours for the job: "))
floatCostOfMaterials = float(input("Please enter the wholesale cost of materials for the job: "))

#process data
floatCostOfLabor = FLOAT_LABOR_COST_PER_HOUR * floatNumberOfHours
floatWholesaleCostMultiplied = floatCostOfMaterials * FLOAT_WHOLESALE_MULTIPIER
floatTotalCost = floatCostOfLabor + floatWholesaleCostMultiplied

#output information
print(f"Labor cost for job: {floatCostOfLabor}")
print(f"Wholesale cost of material for job: {floatWholesaleCostMultiplied}")
print(f"Total cost of job: {floatTotalCost}")