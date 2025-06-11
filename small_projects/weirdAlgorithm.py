import os, psutil, time

def weird_algorithm(n):
    while (n!=1):
        if (n%2) == 0:
            n = n/2
        else:
            n = (n*3)+1
        print(int(n))

def main():
    while True:
        try:
            n = int(input("Enter the number(positive and integer)"))
            if n<= 0:
                print("Please Enter a positive Integer")
            else:
                start = time.time()
                weird_algorithm(n)
                process = psutil.Process(os.getpid())
                print('Memory usage in Mega Bytes: ', process.memory_info().rss/(1024**2))  # in bytes 
                print(f'Time Taken: {time.time() - start}')
        except ValueError:
            print("Invalid Input. Please enter an integer.")


if __name__ == "__main__":
    main()

#Initially i wrote a simple code, but the time consumed was more than 1.00 s, but now, the code is organised and has more lines, but time consumed is less. 