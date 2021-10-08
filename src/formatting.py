def bool_emojify(bool_var: bool) -> str:
    """Return ✅  or ❌ based on bool state"""
    return "\N{WHITE HEAVY CHECK MARK}" if bool_var else "\N{CROSS MARK}"
