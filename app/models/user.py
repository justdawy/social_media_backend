from sqlalchemy.sql import func

from app.extensions import db

class User(db.Model):
    __tablename__ = 'users'
    
    # Basic info
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    
    # Profile info
    display_name = db.Column(db.String(100))
    bio = db.Column(db.String(500))
    profile_picture_url = db.Column(db.String(255))
    cover_photo_url = db.Column(db.String(255))
    location = db.Column(db.String(100))
    website = db.Column(db.String(255))
    
    # Timestamps
    created_at = db.Column(
        db.DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    
    def __repr__(self):
        return f'<User {self.username}>'
    
    def to_json(self, include_email=False):
        """"Convert user to dict (for API responses)"""
        data = {
            'id': self.id,
            'username': self.username,
            'display_name': self.display_name,
            'bio': self.bio,
            'profile_picture_url': self.profile_picture_url,
            'cover_photo_url': self.cover_photo_url,
            'location': self.location,
            'website': self.website,
            'created_at': self.created_at.isoformat()
        }
        if include_email:
            data['email'] = self.email
        
        return data