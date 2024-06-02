#!/usr/bin/env python3
"""
Inherits from Auth.Class defintion for auth create
      a class to manage the API authentication.
"""
from api.v1.auth.auth import Auth
import base64
from typing import Tuple, TypeVar, Union
from api.v1.views.users import User


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

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        '''
        that returns the decoded value of a
        Base64 string base64_authorization_header
        '''
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_credentials = base64.b64decode(base64_authorization_header)
            decoded_credentials_utf8 = decoded_credentials.decode('utf-8')
        except Exception as e:
            return None
        return decoded_credentials_utf8

    def extract_user_credentials(
              self,
              decoded_base64_authorization_header: str
              ) -> Tuple[str]:
        '''
        Extract email username and password
        that returns the user email and password
        from the Base64 decoded value.
        '''
        if (
            decoded_base64_authorization_header is None
            or type(decoded_base64_authorization_header) != str
            or ":" not in decoded_base64_authorization_header
        ):
            return None, None
        credentials = decoded_base64_authorization_header.split(':')
        return credentials[0], ':'.join(credentials[1:])

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str
            ) -> TypeVar('User'):
        '''
        Gets the User instance based on given email and password
        '''
        if (
            user_email is None or type(user_email) != str
            or user_pwd is None or type(user_pwd) != str
        ):
            return None
        User.load_from_file()
        if User.count() > 0:
            users = User.search({'email': user_email})
            for user in users:
                if user.is_valid_password(user_pwd):
                    return user
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        '''
        Loads the current_user object
        API is fully protected by a Basic Authentication!
        '''
        email, password = self.extract_user_credentials(
            self.decode_base64_authorization_header(
                self.extract_base64_authorization_header(
                    self.authorization_header(request=request))))
        print(email, password)
        return self.user_object_from_credentials(email, password)
