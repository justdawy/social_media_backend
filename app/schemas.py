from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import Nested

from app.models import User, Post
 
class PostSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Post
        load_instance = True
        include_fk = True
        include_relationships = True
        exclude = ('user', )

class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        include_relationships = True
        exclude = ('password_hash', 'posts')

class PublicUserSchema(SQLAlchemyAutoSchema):
    class Meta(UserSchema.Meta):
        exclude = ('email', )

user_schema = UserSchema() # type: ignore
public_user_schema = PublicUserSchema()
post_schema = PostSchema()