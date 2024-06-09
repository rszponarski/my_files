def delete_lines(input_file_name, output_file_name):
    with open(input_file_name, 'r') as input_file:
        lines = input_file.readlines()

    linie_for_save = [lin for lin in lines if any(c.isalpha() for c in lin.strip())]

    with open(output_file_name, 'w') as output_file:
        for n_lin in linie_for_save:
            output_file.write(n_lin)


my_file_in = "wig_40_file_to_clean.txt"
mu_file_out = "wig_40_cleanup.txt"

delete_lines(my_file_in, mu_file_out)
print("File is ready")
