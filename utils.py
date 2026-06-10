# Before
def process_data(data):
    # Basic data processing that does not handle errors well
    processed_data = []
    for item in data:
        processed_data.append(item)
    return processed_data

# After
def process_data(data):
    # Enhanced data processing with error handling
    processed_data = []
    for item in data:
        try:
            processed_data.append(item)
        except Exception as e:
            print(f"Error processing item: {e}")
    return processed_data