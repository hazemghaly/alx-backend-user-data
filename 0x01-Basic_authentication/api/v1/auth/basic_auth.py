#!/usr/bin/env python3
"""
Inherits from Auth.Class defintion for auth create
a class to manage the API authentication.
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    ''' Inherits from Auth.Class defintion for auth create
a class to manage the API authentication.
'''
      def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
            '''eturns the Base64 part of the Authorization
            header for a Basic Authentication
            '''
            if authorization_header is None:
                return None
            if not isinstance(authorization_header, str):
                return None
            if not authorization_header.startswith('Basic '):
                return None
            auth_type, auth_value = authorization_header.split(' ', 1)
            if auth_type == 'Basic':
                return auth_value.strip()
