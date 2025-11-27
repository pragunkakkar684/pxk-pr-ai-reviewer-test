import time

def process_data(data):
    print("Processing...")  # ❌ Should be logger
    time.sleep(2)  # ❌ blocking call
    return data
