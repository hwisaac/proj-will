# System
from drf_yasg import openapi

# Project
from config.swagger import Swagger


class CommentSwagger:
    list = Swagger(
        body=[],
        res=[
            {
                "name": "200",
                "description": "성공",
                "res": {
                    "data": {
                        "article": {
                            "id": 1,
                            "created_at": "2023-01-31T11:50:56.877932Z",
                            "user_id": 1,
                            "content": "할 말이 없습니다. 죄송합니다.",
                            "nickname": "수줍은 거북이",
                            "like_count": 0,
                            "comment_couunt": 1,
                            "book": {
                                "title": "temp-title",
                                "author": "temp-author",
                                "category": "temp-category",
                                "image_url": "http://books.google.com/books/content?id=N8XyDwAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api",
                            },
                        },
                        "comments": [
                            {
                                "id": 1,
                                "created_at": "2023-02-03T12:18:58.929997Z",
                                "content": "hohoho",
                            },
                        ],
                    },
                    "code": 0,
                    "message": "SUCCESS",
                    "success": True,
                },
            },
        ],
    )
