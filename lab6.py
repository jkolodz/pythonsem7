from random import randint
import threading

def rand_tab():
    data = []
    for index in range(100):
        data.append(randint(-11, 10))
    print(data)
    print("\n")
    return data


def histogram_thread(input_tab, output_tab, min_value):
    for d in input_tab:
        output_tab[d + min_value] += 1


def print_result(val_1, val_2):
    print_value = []
    for i in range(len(val_1)):
        print_value.append(val_1[i] + val_2[i])
    print(print_value)

def main():
    
    input_data = rand_tab()
    min_val = min(input_data)
    max_val = max(input_data)
    data_size = len(input_data)
    input_data_a=input_data[0:int(data_size / 2)]
    input_data_b=input_data[int(-data_size / 2):]
    output_a=[0] * (max_val - min_val + 1)
    output_b=[0] * (max_val - min_val + 1)

    t1 = threading.Thread(target=histogram_thread, args=(input_data_a, output_a, min_val))
    t2 = threading.Thread(target=histogram_thread, args=(input_data_b, output_b, min_val))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print_result(output_a, output_b)

if __name__ == '__main__':
    main()