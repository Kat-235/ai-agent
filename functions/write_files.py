import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs

        if valid_target_dir == False:
            raise Exception(f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory')

        if os.path.isdir(target_dir):
            raise Exception(f'Error: Cannot write to "{file_path}" as it is a directory')

        os.makedirs(file_path, exist_ok=True)

        with open(f"{working_directory}/{file_path}", "w") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return e
