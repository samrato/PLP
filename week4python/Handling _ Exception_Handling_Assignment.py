def read_and_modify_file():
    try:
       
        input_filename = input("Enter the name of the file to read: ")
        with open(input_filename, 'r') as infile:
            content = infile.read()
        modified_content = content.upper()
        output_filename = "modified_" + input_filename

      
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f" Success! Modified content has been written to '{output_filename}'")

    except FileNotFoundError:
        print("Error: The file does not exist.")
    except PermissionError:
        print("Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f" An unexpected error occurred: {e}")


read_and_modify_file()
