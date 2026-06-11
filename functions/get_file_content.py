import os
def get_file_content(working_directory,file_path):
  try:
    abs_working_directory = os.path.abspath(working_directory)
    complete_path = os.path.normpath(os.path.join(abs_working_directory,file_path))
    valid_path = os.path.commonpath([complete_path,abs_working_directory]) == abs_working_directory
    if not valid_path:
        return f"Error: Cannot read \"{file_path}\" as it is outside the permitted working directory"
    if os.path.isdir(complete_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    max_chars = 10000
    content = ""
    with open(complete_path,"r")as f:
        content = f.read(max_chars)
        # After reading the first MAX_CHARS...
        if f.read(1):
            content += f'[...File "{file_path}" truncated at {max_chars} characters]'
    return content
  except Exception as e:
     return f"Error: {e}"


