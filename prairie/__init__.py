import falcon
import json


class CustomEncoder(**kwargs):
    def __init__(self, encoders):
        self.encoders = encoders

    def default(self, o):
        class_name = o.__class__.__name__
        fn = self.encoders.get(class_name, None)
        if fn is not None:
            return fn(o)
        return json.JSONEncoder.default(self, o)


class Middleware(object):
    def __init__(self, custom_encoders):
        self.custom_encoder = CustomEncoder(custom_encoders)
        self.req = None

    def __http_bad_request(self, title='', description=''):
        """Default handling to raise HTTP Bad Request"""
        raise falcon.HTTPBadRequest(title, description)

    def safe_get_json(self, field, default):
        """Safe getter to access json fields"""
        if field not in self.req.json and default is not None:
            self.__http_bad_request('Missing {0} field.'.format(field))

        return self.req.json(field, default)

    def process_request(self, req, resp):
        """Request processing"""
        if not req.content_length:
            return

        body = req.stream.read()
        req.json = {}
        self.req = req
        req.safe_get_json = self.safe_get_json

        try:
            req.json = json.loads(body.decode('utf-8'))
        except ValueError:
            self.__http_bad_request('Invalid JSON', 'Syntax Error')

    def process_response(self, req, resp, resource, req_succeed):
        """Response processing"""
        if getattr(resp, 'json', None) is not None:
            resp.body = str.encode(json.dumps(
                resp.json, cls=self.custom_encoder))
