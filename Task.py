import sys

def copy_sentence(sentence, times):
    return (sentence + '\n') * times

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python task.py <sentence> <times> <output_file>")
        sys.exit(1)

    sentence = sys.argv[1]
    try:
        times = int(sys.argv[2])
    except ValueError:
        print("The number of times must be an integer.")
        sys.exit(1)

    output_file = sys.argv[3]

    result = copy_sentence(sentence, times)

    with open(output_file, 'w') as f:
        f.write(result)

    print(f"Output written to {output_file}")

    print(f"code by adirtta")
