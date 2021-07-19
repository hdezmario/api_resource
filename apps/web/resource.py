from flask_restful import Resource


class TaskAllApp(Resource):
    def get(self):
        return {'task': 'Hello world'}, 201