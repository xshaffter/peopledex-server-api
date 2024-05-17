import uuid

from common.fastapi.aws.manager import AwsConfig
from common.fastapi.db import CRUDDal, get_dal_dependency
from common.fastapi.routing import get, BaseRouter, post, put
from common.fastapi.schemas import HTTPResponseModel
from fastapi import UploadFile, Depends
from fastapi.responses import Response
from starlette import status

from src.db.models.profile import Profile


class StaticsRouter(BaseRouter):

    @get('/{route}')
    def get_item(self, route: str):
        aws = AwsConfig()
        bucket = 'para-mada-personal-bucket'
        s3 = aws.get_s3_client()
        print('requesting ' + route)

        if not route:
            return HTTPResponseModel(status_code=status.HTTP_400_BAD_REQUEST, detail={
                'body': 'No file name provided'
            })
        key = f'statics/{route}'

        response = s3.get_object(Bucket=bucket, Key=key)

        image = response['Body'].read()
        return Response(image, media_type=response["ContentType"])

    @post("/", response_model=HTTPResponseModel)
    async def create_upload_file(self, file: UploadFile):
        aws = AwsConfig()
        bucket = 'para-mada-personal-bucket'
        s3 = aws.get_s3_client()
        filename = f"{uuid.uuid4()}_{file.filename}"
        s3.upload_fileobj(file.file, bucket, f'statics/{filename}')
        return HTTPResponseModel(status_code=201, detail=dict(filename=filename))

    @put("/profile/{profile_id}", response_model=HTTPResponseModel)
    async def update_profile_photo(self, profile_id: int, file: UploadFile, dal: CRUDDal = Depends(get_dal_dependency(CRUDDal, model=Profile))):
        aws = AwsConfig()
        bucket = 'para-mada-personal-bucket'
        s3 = aws.get_s3_client()
        filename = f"{uuid.uuid4()}_{file.filename}"
        s3.upload_fileobj(file.file, bucket, f'statics/{filename}')
        print(id)
        item = dal.update(dict(image_url=f'http://api.para-mada.com/statics/{filename}'), dict(id=profile_id))
        dal.commit()
        return HTTPResponseModel(status_code=status.HTTP_200_OK, detail=dict(profile=item.name, filename=filename))
