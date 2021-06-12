from passlib.context import CryptContext

ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hash:
    @staticmethod
    def bcrypt(self, password):
        return ctx.hash(password)

    @staticmethod
    def verify(hashed_password, plain_password):
        return ctx.verify(plain_password, hashed_password)
