from functools import wraps
from flask import session, redirect, url_for

def login_required(role=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if 'usuario' not in session:
                return redirect(url_for('index'))
            if role is not None and session['usuario']['rol'] != role:
                return redirect(url_for('index'))  # O redireccionar a una página de error
            return func(*args, **kwargs)
        return wrapper
    return decorator
