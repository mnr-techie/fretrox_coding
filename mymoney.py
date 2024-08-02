def distribute_apples(weights, payments):
    # Calculate total payment and target proportionate weights
    total_payment = sum(payments)
    total_weight = sum(weights)
    target_weights = [total_weight * (p / total_payment) for p in payments]
    
    # Sort weights in descending order for better proportional distribution
    weights.sort(reverse=True)
    
    # Initialize distribution
    distribution = { "Ram": [], "Sham": [], "Rahim": [] }
    current_weights = [0, 0, 0]
    
    # Assign names to indices
    names = ["Ram", "Sham", "Rahim"]
    
    # Distribute apples
    for weight in weights:
        # Find the person who is furthest from their target weight proportion
        min_diff_index = (None, float('inf'))  # (index, difference)
        
        for i in range(3):
            current_diff = abs((current_weights[i] + weight) - target_weights[i])
            if current_diff < min_diff_index[1]:
                min_diff_index = (i, current_diff)
        
        # Assign the apple to the selected person
        person_index = min_diff_index[0]
        distribution[names[person_index]].append(weight)
        current_weights[person_index] += weight
    
    return distribution

def main():
    # Read apple weights from user input
    apple_weights = []
    while True:
        weight = int(input("Enter apple weight in gram (-1 to stop): "))
        if weight == -1:
            break
        apple_weights.append(weight)
    
    # Payments
    payments = [50, 30, 20]
    
    # Distribute apples
    result = distribute_apples(apple_weights, payments)
    
    # Print result
    print("Distribution Result:")
    for name, weights in result.items():
        print(f"{name}: {', '.join(map(str, weights))}")

if __name__ == "__main__":
    main()
