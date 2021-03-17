# fp = open("test.txt", "w")
# fp.write("This file was created using Python!")
# fp.close()


with open("../test.txt", "a") as f:
    f.write("hello this is python file. I am very excited working with files\n")
