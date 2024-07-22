from flask import request
from flask_restx import Resource

from app.main.exceptions import ApiException
from ..service.ocr_service import find_matches
from ..dto.upload_dto import UploadDto

api = UploadDto.api
_upload = UploadDto.upload

@api.route('/')
@api.response(400, "Bad request")
class ImageUpload(Resource):

    @api.response(200, description="Success")
    @api.expect(_upload, validate=True)
    def post(self):
        img = request.json['image']
        try:
            return find_matches(base_64_img=img)
        except ApiException as ex:
            api.abort(ex.code, ex.message)