"""sidebar-cycle has no agent-side behaviour; all of it lives in desktop/plugin.js.

Hermes imports every enabled directory plugin as a Python package, so the package
needs this module and a register() to load without a warning on each start.
"""


def register(ctx) -> None:
    """Nothing to register: no tools, hooks, or commands."""
