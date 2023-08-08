def generate_binary_vectors(n):
    if n <= 0 or n > 2528:
        return []

    vectors = []
    queue = ['']

    while queue:
        vector = queue.pop(0)
        if len(vector) == n:
            vectors.append(vector)
        else:
            queue.append(vector + '0')
            queue.append(vector + '1')

    return vectors


if __name__ == '__main__':
    length = int(input("Enter the length of binary vectors: "))
    binary_vectors = generate_binary_vectors(length)
    print("Binary vectors of length", length, "in lexicographical order:")
    for vector in binary_vectors:
        print(vector)
