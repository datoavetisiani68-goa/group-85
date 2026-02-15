def count_vowels(text):
    vowels = "aeiouAEIOUაეიოუ"
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    print(count)
