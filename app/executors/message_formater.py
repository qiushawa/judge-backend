import re

def hide_paths(error_message: str, fake_path) -> str:
    return re.sub(
        r"([a-zA-Z]:)?(\\|\/)[^\s]+", fake_path, error_message
    )  # 隱藏路徑，用假路徑代替


def extract_first_n_lines(error_message: str,fake_path:str,  n: int = 20):
    error_message = hide_paths(error_message, fake_path)
    lines = error_message.splitlines()
    context = lines[:n]
    return "\n".join(context)