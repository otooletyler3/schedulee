from const import LOGGER_VALID_TYPES, DEBUG

def log(message, type="info"):
    final_type = f'{type}' if type in LOGGER_VALID_TYPES else "info"
    message = f"[{final_type.upper()}] {message}"
    if DEBUG: 
        print(message)

    with open('tmp/session') as s:
        with open(f'logs/{s.readline().rstrip("\n")}', "a") as f:
            f.write(f'{message}\n')