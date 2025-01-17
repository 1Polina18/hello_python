def say_hello(name: str) -> str:
    return f"Hello, {name}!"


if __name__ == "__main__":
    user_name = input("En ter your name: ")
    print(say_hello(user_name))
