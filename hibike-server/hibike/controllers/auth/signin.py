from flask import request, session
from flask_apispec import doc, use_kwargs
from hibike import db
from hibike.models.auth import User
from hibike.models.common.redis_conn import RedisConn
from hibike.controllers.auth import (
    API_CATEGORY,
    auth_bp
)
from hibike.schema.user import (
    RequestSigninSchema,
)
from hibike.utils.common import (
    response_json_with_code,
)
import bcrypt

headers = {
    'Content-Type': 'application/json; chearset=utf-8',
    'Authorization':'key=AAAAgdsrYfY:APA91bFPnAbWgVS2NITYanribOeuBkTbB715mTGQzLNjo9W9waNmEjqMYOzzjbwbJilmla-6oA09qnddeIWAUpT_EUte9KJ5vHsBl4tM-jA-OLB29KjoS7vyeaFKL6c0MGfk7wRb7ksQ'
    }

@auth_bp.route('/signin', methods=["POST"])
@use_kwargs(RequestSigninSchema)
@doc(
    tags=[API_CATEGORY],
    summary="로그인",
    description="로그인을 합니다.",
    responses={200: {"description" : "success response"},
               401: {"description" : "Unauthorized"},
    }
)
def login(id, password):
    user_row = User.get_user_by_id(id)
    if user_row is None:
        return response_json_with_code(
            401, 
            result="There is no ID on db."
        )
    if bcrypt.checkpw(password.encode('utf-8'), user_row.password.encode('utf-8')):
        db.session.commit()
        
        session[id] = id
        
        return response_json_with_code(200)
    else:
        return response_json_with_code(
            401, 
            result="Failed"
        )   
        
        
@auth_bp.route('/signout')
@doc(
    tags=[API_CATEGORY],
    summary="로그아웃",
    description="로그아웃을 합니다.",
    responses={200: {"description" : "success response"},
               401: {"description" : "Unauthorized"},
    }
)
def signout():
    id = request.args.get("id")
    
    if session[id]:
        session.pop(id, None)

    return {"result":"success"}
        