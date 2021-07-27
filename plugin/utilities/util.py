def print_header(header: str):
    sz = 20 - int(len(header)/2)
    print("=" * sz, header, "=" * sz)


def print_sub(header: str):
    sz = 20 - int(len(header)/2)
    print(" " * sz, header, " " * sz)
