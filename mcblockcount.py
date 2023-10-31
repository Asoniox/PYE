block_top = int(input("Top Block Y: "))
block_bottom = int(input("Bottom Block Y: "))
if block_top > block_bottom:
    print("Offset:", block_top - block_bottom)
elif block_top < block_bottom:
    print("Offset:", block_bottom - block_top)