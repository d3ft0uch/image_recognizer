from flask_restx import fields, Namespace


class UploadDto:
    api = Namespace('upload', description='upload image to scan')
    upload = api.model('upload', {
        'image': fields.String(required=True, description='base64 image')
    })