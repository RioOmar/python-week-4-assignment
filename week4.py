def read_and_write_file():
    try:
        # Ask the user for the input filename
        input_filename = input("Enter the filename to read from: ")
        
        # Try to open the file for reading
        with open(input_filename, 'r') as file:
            content = file.read()
        
        # Modify the content (e.g., appending a message)
        modified_content = content + "\nThis is the modified content!"

        # Ask the user for the output filename
        output_filename = input("Enter the filename to write to: ")
        
        # Try to open the output file for writing
        with open(output_filename, 'w') as file:
            file.write(modified_content)
        
        print("Content successfully written to", output_filename)

    except FileNotFoundError:
        print("Error: The file does not exist.")
    except IOError:
        print("Error: Could not read or write to the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
read_and_write_file()
