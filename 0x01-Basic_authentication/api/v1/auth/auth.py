#!/usr/bin/env python3
"""
Route module for the API
"""
from flask import Flask, request
from typing import List, TypeVar


class Auth():
    """Class defintion for auth"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """False - path and excluded_paths"""
        if path is None:
            return True
        if excluded_paths is None or  excluded_paths is empty:
            return True
        if path is in excluded_paths:
            return False

    def authorization_header(self, request=None) -> str:
        """returns None - request will be the Flask request object"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """returns None - request will be the Flask request object"""
        return None
