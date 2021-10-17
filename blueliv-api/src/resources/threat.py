from logging import getLogger
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from src.models.threat import ThreatModel
from src.resources.error import SQLWriteError

log = getLogger(__name__)


class ThreatList(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('author',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('topic',
                        type=str,
                        required=True,
                        help="Every threat needs a description."
                        )
    parser.add_argument('post_date',
                        type=str,
                        required=True,
                        help="Every threat needs a post date."
                        )

    @jwt_required()
    def get(self):

        log.info("Retrieve all threats")
        threats = [threat.json() for threat in ThreatModel.find_all()]
        if threats:
            return {'hits': threats, 'count': len(threats)}, 200

        return {'status': 'OK', 'message': 'No threats'}, 200

    @jwt_required()
    def post(self):

        log.info("Parse new threat")
        data = self.parser.parse_args()
        threat = ThreatModel(**data)

        try:
            log.info("Writing new threat")
            threat.save_to_db()
        except SQLWriteError:
            log.error("Couldn't insert into table threats")
            return {"message": "An error occurred while inserting the threat."}, 500

        return threat.json(), 201