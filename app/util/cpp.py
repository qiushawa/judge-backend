import re
import subprocess
import os, tempfile


def compile_code(code: str):
    with tempfile.NamedTemporaryFile(
        suffix=".cpp", delete=False, mode="w", encoding="utf-8"
    ) as temp_cpp_file:
        temp_cpp_file.write(code)
        temp_cpp_file.flush()
        cpp_file_path = temp_cpp_file.name
    exe_file_path = cpp_file_path.replace(".cpp", ".exe")
    compile_command = f"g++ {cpp_file_path} -o {exe_file_path}"
    result = subprocess.run(
        compile_command,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8",
        errors="replace",
    )
    os.remove(cpp_file_path)
    return exe_file_path, result


def run_exe(exe_path, input_text):
    try:
        result = subprocess.run(
            [exe_path],
            input=input_text,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        output = result.stdout
        if result.stderr:
            error = result.stderr
        else:
            error = None
        return output, error
    except Exception as e:
        return None, str(e)


def hide_paths(error_message: str) -> str:
    return re.sub(
        r"([a-zA-Z]:)?(\\|\/)[^\s]+", "G:/tmp/code.cpp", error_message
    )  # 隱藏路徑，用假路徑代替


def extract_first_n_lines(error_message: str, n: int = 20):
    error_message = hide_paths(error_message)
    lines = error_message.splitlines()
    context = lines[:n]
    return "\n".join(context)
