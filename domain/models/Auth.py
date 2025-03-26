from peewee import DoesNotExist
from jwt_bottle.JWTPlugin import BaseAuth
from . import User

class Auth(BaseAuth):
    """Classe para autenticação.
    Precisa conter um método estático chamado authenticate e outro
    chamado get_user.

    Os parametros de authenticate ficam a critério do método post.

    O padrão é receber uma requisição POST enviando dados no formato JSON.
    Esses dados são empacotados no argumento kwargs do método authenticate.

    para identificar o usuário é necessário realizar a consulta utilizando
    um ID.
    """

    @staticmethod
    def authenticate(*args, **kwargs):
        """Método para autenticação, aqui utilizei uma classe chamada
        User implementada com o ORM peewee e uma simples regra de 
        autenticação apresentada pelo Eduardo Mendes.
        link: https://www.youtube.com/watch?v=ieGA91ExOH0

        Returns:
            User: dicionário contendo id para gerar o token.
            OBS: é necessário possuir um atributo "id" para gerar o token.
        """
        try:
            if "email" in kwargs and "password" in kwargs:
                user = User.get(User.email==kwargs['email'])
                if user.verify(kwargs['password']):
                    return user
            return None
        except DoesNotExist as err:
            return {"erro": f"Usuário {kwargs['email']} não localizado"}

    @staticmethod
    def get_user(*args, **kwargs):
        """Classe para resgatar usuario autenticado
        utilizando a decodificação de um token.

        Args:
            user_id ([int]): identificador do usuário.

        Returns:
            User: retorna usuário autenticado pelo Token.
        """
        try:
            user = User.get_by_id(kwargs["id"])
            if user:
                return user
            return None
        except DoesNotExist as err:
            return {}