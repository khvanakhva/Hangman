def what_to_do(instructions):
    if instructions.startswith('Simon says '):
        return "I" + instructions.replace('Simon says', '')
    elif instructions.endswith(' Simon says'):
        return "I " + instructions.replace('Simon says', '')
    return "I won't do it!"
