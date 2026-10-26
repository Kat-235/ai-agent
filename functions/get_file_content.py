import os

def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs

        if valid_target_dir == False:
            raise Exception(f'Error: Cannot read "{directory}" as it is outside the permitted working directory')

        if os.path.isfile(target_dir) == False:
            raise Exception(f'Error: File not found or is not a regular file: "{file_path}"')

        max_chars = 10_000

        with open(f"{working_directory}/{file_path}", "r") as f:
           content = f.read(max_chars)
           if f.read(1):
               content += f'[...File "{file_path}" truncated at {max_chars} characters]'

        return content

    except Exception as e:
        return e
