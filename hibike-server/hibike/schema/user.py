from marshmallow import fields, Schema

class RequestSetNicknameSchema(Schema):
      nickname = fields.Str(description="닉네임", required=True)
      id = fields.Str(description="유저 아이디", required=True)

class RequestSignupSchema(Schema):
      id = fields.Str(description="유저 아이디", required=True)
      password = fields.Str(description="비밀번호", required=True)
      nickname = fields.Str(description="닉네임", required=True)

class RequestSigninSchema(Schema):
      id = fields.Str(description="유저 아이디", required=True)
      password = fields.Str(description="비밀번호", required=True)
      fcm_token = fields.Str(description="fcm 토큰", required=True)

class RequestFileSchema(Schema):
      id = fields.Str(description="유저 아이디", required=True)
      file = fields.Raw(required=True, type="file")
      
class RequestPostSchema(Schema):
      id = fields.Str(description="유저 아이디", required=True)
      title = fields.Str(description="제목", required=True)
      contents = fields.Str(description="내용", required=True)

class RequestReplySchema(Schema):
      id = fields.Str(description="유저 아이디", required=True)
      contents = fields.Str(description="내용", required=True)
      post_id = fields.Int(description="포스트 id", requird=True)      

class RequestRidingEachSchema(Schema):
      user_id = fields.Str(description="유저 아이디", required=True)
      unique_id = fields.Str(description="유저 아이디", required=True)
      riding_time = fields.Str(description="주행 시간", required=True)
      ave_speed = fields.Str(description="평균 속도", required=True)
      distance = fields.Str(description="평균 거리", required=True)
      
class RequestRidingRegionSchema(Schema):
      region = fields.Str(description="지역", required=True)
      unique_id = fields.Str(description="라이딩 유니크 아이디", required=True)

class RequestDangerRangeSchema(Schema):
      danger_range = fields.List(fields.List(fields.Float,description="위험지역 탐색 범위 리스트", required=True))

class RequestDangerInformationSchema(Schema):
      latitude = fields.Float(description="위도", required=True)
      longitude = fields.Float(description="경도", required=True)

class RequestDeleteDanger(Schema):
      user_id = fields.Str(description="유저 id", required=True)
      latitude = fields.Float(description="위도", required=True)
      longitude = fields.Float(description="경도", required=True)
      my_latitude = fields.Float(description="위도", required=True)
      my_longitude = fields.Float(description="경도", required=True)

class RequestMyPosts(Schema):
      user_id = fields.Str(description="유저 id", required=True)
      page = fields.Int(description="page number", required=True)

class RequestMyDanger(Schema):
      user_id = fields.Str(description="유저 id", required=True)
      page = fields.Int(description="page number", required=True)

class RequestDeleteNearDanger(Schema):
      latitude = fields.Float(description="위도", required=True)
      longitude = fields.Float(description="경도", required=True)
      
class RequestDeleteMyPost(Schema):
      post_id = fields.Int(description="포스트 id", requird=True)
      
class RequestDeleteMyDanger(Schema):
      danger_id = fields.Int(description="위험요소 id", requird=True)