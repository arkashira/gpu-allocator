# Before
def allocate_gpu(resources, demand):
    # Simple allocation logic that does not account for grey market diversion
    allocated_resources = {}
    for resource in resources:
        if demand > 0:
            allocated_resources[resource] = demand
            demand = 0
    return allocated_resources

# After
def allocate_gpu(resources, demand):
    # Improved allocation logic that considers grey market diversion
    allocated_resources = {}
    grey_market_diversion_rate = 0.1  # Assuming 10% diversion rate
    effective_demand = demand * (1 - grey_market_diversion_rate)
    for resource in resources:
        if effective_demand > 0:
            allocated_resources[resource] = effective_demand
            effective_demand = 0
    return allocated_resources