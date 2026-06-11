import os
def get_files_info(working_directory,directory = "."):
    try:
        

        absolute_path =  os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(absolute_path,directory))
        vaild_target_dir = os.path.commonpath([absolute_path,target_dir]) == absolute_path
        if vaild_target_dir == False:
            return f'Result for \'{directory}\' directory:\nError: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(target_dir):
            return f'Result for \'{directory}\' directory:\nError: "{directory}" is not a directory'
        

        files = os.listdir(target_dir)
        results_strings = []
        for file in files:
            full_path = os.path.normpath(os.path.join(target_dir,file))
            file_size = os.path.getsize(full_path)
            is_directory = os.path.isdir(full_path)
            results_strings.append(f"- {file}: file_size={file_size} bytes, is_dir={is_directory}")
        return (f"Result for \'{directory}\' directory:\n")+"\n".join(results_strings)
        

            
    except Exception as e:
        return f"Error: {e}"
    
    
    

    
    
