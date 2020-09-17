number_of_runs = 0
total_time = 0

while True:
    one_run = input("Enter 10 km run time, or 'q' to exit: ")

    if one_run == 'q':
        break

    else:
        number_of_runs += 1
        total_time += float(one_run)

average_time = total_time / number_of_runs

print(f"Average of {average_time}, over {number_of_runs} runs")


# In a real-world Python application, if you’re taking input from the user and calling float (docs.python.org/3/library/functions.html#float), you should probably wrap it within try (docs.python.org/3/reference/compound_stmts.html#the-try-statement), in case the user gives us an illegal value:

# try:
#     n = float(input("Enter a number: "))
#     print(f"n = {n}")
# except ValueError as e:
#     print("Hey!  That's not a valid number!")