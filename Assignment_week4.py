def file_read_write():
    try:
        # Ask the user for the input file name
        input_file = input("Enter the name of the file to read from: ")

        # Attempt to open and read the file
        with open(input_file, "r") as file:
            content = file.readlines()

        # Modify the content (e.g., add line numbers)
        modified_content = [f"{i + 1}: {line}" for i, line in enumerate(content)]

        # Ask for the output file name
        output_file = input("Enter the name of the file to write to: ")

        # Write the modified content to the output file
        with open(output_file, "w") as file:
            file.writelines(modified_content)

        print(f"Modified content successfully written to {output_file}.")

    except FileNotFoundError:
        print("Error: The file you specified does not exist.")
    except PermissionError:
        print("Error: You don't have permission to read or write to the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Run the program
file_read_write()
