def add_numbers(a, b):
    return a + b

def multiply_numbers(a, b):
    return a * b

def write_to_file(filename, content):
    with open(filename, "w") as f:
        f.write(content)

def read_from_file(filename): 
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        return "File not found."

if __name__ == "__main__":
    # Example usage without needing input
    result_add = add_numbers(2, 3)
    result_multiply = multiply_numbers(4, 5)

    print(f"Addition Result: {result_add}")
    print(f"Multiplication Result: {result_multiply}")

    write_to_file("output.txt", "This is a test.")
    content = read_from_file("output.txt")
    print(f"File Content: {content}")
