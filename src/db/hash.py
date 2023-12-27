from passlib.context import CryptContext

_pwd_cxp = CryptContext(schemes='bcrypt', deprecated='auto')


class Hash:

    @staticmethod
    def bcrypt(password) -> str:
        return _pwd_cxp.hash(password)

    @staticmethod
    def verify(hashed_password, password) -> bool:
        return _pwd_cxp.verify(password, hashed_password)
