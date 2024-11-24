def simple_file_read_write():
    # Ask the user for the filename
    input_file = input("Enter the filename to read: ")
    
    try:
        # Open and read the file
        with open(input_file, 'r') as file:
            content = file.read()  # Read the entire content of the file
        
        # Modify the content (e.g., add a header)
        modified_content = "Modified File Content:\n\n" + content

        # Write the modified content to a new file
        output_file = "output.txt"
        with open(output_file, 'w') as file:
            file.write(modified_content)

        print(f"Modified content has been saved to '{output_file}'!")

    except FileNotFoundError:
        print("Error: File not found. Please check the filename and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function
simple_file_read_write()
