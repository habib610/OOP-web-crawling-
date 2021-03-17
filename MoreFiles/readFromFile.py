# lines = ["This is Line 1", "This is line 2","This is line 3" ]

# ==> writhing lines
# Method 1
# with open("test.txt", "w") as fl:
#     fl.write("This is Line 1\nThis is line 2\nThis is line 3")

# Method 2
# with open("test.txt", "w") as fl:
#     for line in lines:
#         fl.write(line+"\n")

# reading files all at once ==>
# with open('test.txt', "r") as fp:
#     content = fp.read()
#     print(content)

# reading files by line Method 1 ==>

with open("test.txt", 'r') as fp:
    print(fp.read())
    # for line in fp:
    #     print(line)