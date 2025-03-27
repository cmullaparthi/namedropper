def get_first_name(name: str):
    parts = name.strip().split()
    return {"first_name": parts[-1] if len(parts) > 1 else parts[0], "from_model": False}
