from pymongo import errors
from . import ROOMS
from flask import flash


def check_username(user_name):
    if len(user_name) < 3:
        flash("Username must be at least 3 characters long.")
        return False
    elif len(user_name) > 20:
        flash("Username must be no more than 20 characters long.")
        return False
    elif " " in user_name:
        flash("Username cannot contain spaces.")
        return False
    return True


def check_password(password):
    if len(password) < 8:
        flash("Password must be at least 8 characters long.")
        return False
    elif len(password) > 20:
        flash("Password must be no more than 20 characters long.")
        return False
    return True


def check_email(email):
    if len(email) < 1:
        flash("Email cannot be empty.")
        return False
    elif len(email) > 20:
        flash("Email cannot be more than 20 characters long.")
        return False
    return True


def check_password_match(password, password_confirm):
    if password != password_confirm:
        flash("Passwords do not match.", category="errors")
        return False
    return True
