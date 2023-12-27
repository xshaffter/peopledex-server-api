from common.fastapi.db import CRUDDal
from fastapi import HTTPException
from jose import JWTError

from ..hash import Hash
from ..models.user import User
from ..models.token import Token


class UserDAL(CRUDDal[User]):

    def get_current_user(self, token: str) -> User:
        credentials_error = HTTPException(
            403,
            detail='Could not validate credentials',
            headers={'WWW-Authentication': 'Bearer'}
        )
        try:
            token_entity: Token = self._db.query(Token).filter(Token.token == token).first()
            if not token_entity:
                raise credentials_error

            user: User = self._db.query(User).filter(User.id == token_entity.user_id).first()
            if user is None:
                raise credentials_error
        except JWTError:
            raise credentials_error

        return user

    def get_current_user_by_username(self, username: str) -> User:
        credentials_error = HTTPException(
            404,
            detail='No User Found',
        )
        try:
            user: User = self._db.query(User).filter(User.username == username).first()
            if user is None:
                raise credentials_error
        except JWTError:
            raise credentials_error

        return user

    def change_password(self, data, token):
        user = self.get_current_user(token)
        digested_data = dict(data)
        digested_data['password'] = Hash.bcrypt(data.password)
        return self.update(digested_data, id=user.id)

    def create(self, data) -> User:
        digested_data = data.dict()
        del digested_data['password']
        digested_data['password_hash'] = Hash.bcrypt(data.password)
        user = User(
            **digested_data
        )
        self._db.add(user)
        self._db.commit()
        self._db.refresh(user)
        return user

    def add_moderator(self, user, new_moderator):
        # from ..models import Moderation
        # moderation_dal = CRUDDal[Moderation](self._db, Moderation, auto_commit=False)
        # moderation_dal.create(dict(moderated_id=user.id, moderator_id=new_moderator.id))

        user.moderators.append(new_moderator)
        self.commit()

    def delete_moderator(self, user, new_moderator):
        user.moderators.remove(new_moderator)
        self.commit()