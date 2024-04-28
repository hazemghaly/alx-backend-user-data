#!/usr/bin/env python3
"""
Route module for the API
"""
from flask import Flask, request
from typing import List, TypeVar


class Auth():
    '''Class defintion for auth create
      a class to manage the API authentication.
    '''
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """False - path and excluded_paths"""
        if path is None:
            return True
        if excluded_paths is None or not excluded_paths:
            return True
        if path in excluded_paths:
            return False
        n_path = path.rstrip('/')
        n_excluded_paths = [p.rstrip('/') for p in excluded_paths]
        if n_path in n_excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """returns None - request will be the Flask request object"""
        if request is None:
            return None

        return request.headers.get("Authorization", None)

    def current_user(self, request=None) -> TypeVar('User'):
        """returns None - request will be the Flask request object"""
        return None
