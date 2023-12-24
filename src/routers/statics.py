import base64

import boto3
from common.fastapi.routing import get, BaseRouter
from common.fastapi.schemas import HTTPResponseModel
from starlette import status
from fastapi.responses import Response


class StaticsRouter(BaseRouter):

    @get('/{route}')
    def get_item(self, route: str):
        bucket = 'para-mada-personal-bucket'
        s3 = boto3.client('s3')
        print('requesting ' + route)

        if not route:
            return HTTPResponseModel(status_code=status.HTTP_400_BAD_REQUEST, detail={
                'body': 'No file name provided'
            })
        key = f'statics/{route}'

        response = s3.get_object(Bucket=bucket, Key=key)

        image = response['Body'].read()
        return Response(image, media_type=response["ContentType"])
