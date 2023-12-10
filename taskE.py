def compare_subsequences(original, correct, test):
    if len(correct) != len(test):
        return "WL"
    
    for i in range(len(correct)):
        if correct[i] != test[i]:
            return "WS"
    
    if sorted(original.index(x) for x in correct) != sorted(original.index(x) for x in test):
        return "WS"
    
    return "OK"

# Example usage
def main():
    original_sequence = list(map(int, input().split()[1:]))
    correct_answer = list(map(int, input().split()[1:]))
    test_solution = list(map(int, input().split()[1:]))

    result = compare_subsequences(original_sequence, correct_answer, test_solution)
    print(result)

if __name__ == "__main__":
    main()
