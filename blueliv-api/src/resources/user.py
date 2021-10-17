from flask_restful import Resource, reqparse
from hmac import compare_digest
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token
)
from logging import getLogger
from src.models.user import UserModel

log = getLogger(__name__)

log.info("Parsing username and password")
_user_parser = reqparse.RequestParser()
_user_parser.add_argument('username',
                          type=str,
                          required=True,
                          help="This field cannot be blank."
                          )
_user_parser.add_argument('password',
                          type=str,
                          required=True,
                          help="This field cannot be blank."
                          )
log.info("Parse completed")


class UserRegister(Resource):
    def post(self):

        data = _user_parser.parse_args()
        log.info("Retrieve arguments")

        if UserModel.find_by_username(data['username']):
            log.info("Validate if user exists")
            return {"message": "A user with that username already exists"}, 400

        log.info("New user created")
        user = UserModel(data['username'], data['password'])
        user.save_to_db()

        return {"message": "User created successfully."}, 201


class UserLogin(Resource):
    def post(self):

        data = _user_parser.parse_args()

        user = UserModel.find_by_username(data['username'])

        if user and compare_digest(user.password, data['password']):
            log.info("Success login in")
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(user.id)
            return {
                       'access_token': access_token,
                       'refresh_token': refresh_token
                   }, 200

        return {"message": "Invalid Credentials!"}, 401