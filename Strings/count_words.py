def count_words(s: str) -> int:
    return len(s.split())

if __name__ == "__main__":
    text = input()
    print(count_words(text))
