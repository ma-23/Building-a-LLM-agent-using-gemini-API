import os
def write_file(working_directory,file_path,content):
  try:
    abs_working_directory = os.path.abspath(working_directory)
    target_path = os.path.normpath(os.path.join(abs_working_directory,file_path))
    is_valid_path = os.path.commonpath([target_path,abs_working_directory]) == abs_working_directory
    if not is_valid_path:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    if  os.path.isdir(target_path) == True:
        return f'Error: Cannot write to "{file_path}" as it is a directory'
    os.makedirs(os.path.dirname(target_path),exist_ok=True)

    with open(target_path,"w") as f:
        f.write(content)
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
  except Exception as e:
     return f"Error: {e} **Exception error"




