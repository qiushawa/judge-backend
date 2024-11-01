import subprocess
import os, tempfile
from app.executors.message_formater import extract_first_n_lines

def compile_code(code: str):
    with tempfile.NamedTemporaryFile(
        suffix=".c", delete=False, mode="w", encoding="utf-8"
    ) as temp_cpp_file:
        temp_cpp_file.write(code)
        temp_cpp_file.flush()
        cpp_file_path = temp_cpp_file.name
    exe_file_path = cpp_file_path.replace(".c", ".exe")
    compile_command = f"gcc {cpp_file_path} -o {exe_file_path}"
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


def run_code(code, input_text, timeout=5):
    exe_path, compile_result = compile_code(code)
    if compile_result.stderr.strip():
        return None, {"type": "Compile Error", "message": extract_first_n_lines(compile_result.stderr, "G:/tmp/code.c", 10)}
    try:
        result = subprocess.run(
            [exe_path],
            input=input_text,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=timeout
        )
        output = result.stdout
        if result.stderr:
            error = result.stderr
        else:
            error = None
        return output, error
    except subprocess.TimeoutExpired:
        return None, {"type": "Time Limit Exceed", "message": "Program execution time exceeded the maximum limit, possibly due to an infinite loop."}
    except Exception as e:
        return None, {"type": "Runtime Error", "message": str(e)}