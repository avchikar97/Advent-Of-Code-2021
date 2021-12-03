
def main(input_filename : str):
    num_increase = 0
    curr_window = []
    window_sums = []
    with open(input_filename, "r") as input_file:
        for line in input_file:
            curr = int(line)
            curr_window.append(curr)
            if(len(curr_window) == 3):
                window_sums.append(sum(curr_window))
                curr_window.pop(0)

    if(window_sums):
        prev = -1
        for curr in window_sums:
            if(prev != -1):
                if(curr > prev):
                    num_increase += 1
            prev = curr
            print(f"prev = {prev}, curr = {curr}")

    print(f"Number of increases in {input_filename} = {num_increase}")
    return



if __name__ == "__main__":
    main("input1.txt")
