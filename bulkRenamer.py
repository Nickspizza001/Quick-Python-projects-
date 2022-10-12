import os


def main():
    i = 0
    path = 'C:/Users/Damilola/Documents/Python Scripts/sample/'
    try:

        for filename in os.listdir(path):
            my_dest = "Text"+ str(i) + '.doc'
            my_source = path + filename
            my_dest = path + my_dest
            os.rename(my_source, my_dest)
            i +=1
    except Exception as e:
        print("Error: ", e)


main()