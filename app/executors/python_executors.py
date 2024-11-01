import subprocess
import os, tempfile
# from app.executors.message_formater import extract_first_n_lines

def run_code(code, input_text, timeout=5):
    with tempfile.NamedTemporaryFile(
        suffix=".py", delete=False, mode="w", encoding="utf-8"
    ) as temp_py_file:
        temp_py_file.write(code)
        temp_py_file.flush()
        py_file_path = temp_py_file.name

    try:
        result = subprocess.run(
            ["python", py_file_path],
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
    finally:
        os.remove(py_file_path)