PREFIXES = {"mr", "mrs", "ms", "dr", "prof"}

def get_first_name(full_name: str):
    parts = full_name.strip().split()
    if parts and parts[0].lower().strip(".") in PREFIXES:
        parts = parts[1:]
    name = parts[0] if parts else ""
    confidence = 0.4 if name else 0.0
    return {"first_name": name, "from_model": False, "confidence": confidence}
