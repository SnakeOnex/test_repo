import os
import sys

START_MARKER = (
SLIMAK


def get_indentation(line):
    """Returns the number of leading spaces or tabs in a line."""
    return len(line) - len(line.lstrip())


def replace_code_between_markers(filename):
    # Read the file
    try:
        with open(filename, "r") as file:
            lines = file.readlines()

        new_lines = []
        inside_markers = False

        for line in lines:
            if START_MARKER in line:
                inside_markers = True
                indentation = get_indentation(
                    line
                )  # Get indentation from the start marker line
                new_lines.append(line)  # Add the start marker line to the new content

                # Construct the replacement content with the same indentation
                replacement_content = f"""{" " * indentation}#
{" " * indentation}#                    ╔═══════════════════════╗
{" " * indentation}#                    ║                       ║
{" " * indentation}#                    ║       YOUR CODE       ║
{" " * indentation}#                    ║                       ║
{" " * indentation}#                    ╚═══════════════════════╝
{" " * indentation}#
"""
                new_lines.append(replacement_content)

            elif END_MARKER in line:
                inside_markers = False  # End of the block, add the end marker
                new_lines.append(line)
                continue  # Skip the original code between the markers (but keep the end marker)

            if not inside_markers:
                new_lines.append(line)

        # Write the modified content back to the file
        with open(filename, "w") as file:
            file.writelines(new_lines)

        print(f"Replacement complete in {filename}")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
    except Exception as e:
        print(f"An error occurred: {e}")
        
def process_directory(directory):
    """Traverse the directory and process each Python file."""
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                print(f"Processing file: {file_path}")
                replace_code_between_markers(file_path)


if __name__ == "__main__":
    # Check if a filename is provided as an argument
    if len(sys.argv) != 2:
        print("Usage: python replace_code.py <python_file>")
        sys.exit(1)

    # Replace code in the provided Python file
    replace_code_between_markers(sys.argv[1])
