from .ext import db


class Post(db.Model):
    __tablename__ = "wp_posts"
    ID = db.Column(db.Integer)
    post_author = db.Column(db.Integer)
    post_date = db.Column(db.Datetime)
    post_date_gmt = db.Column(db.Datetime)
    post_content = db.Column(db.Text)
    post_title = db.Column(db.Text)
    post_excerpt = db.Column(db.Text)
    post_status = db.Column(db.String(20))
    comment_status = db.Column(db.String(20))
    ping_status = db.Column(db.String(20))
    post_password = db.Column(db.String(255))
    post_name = db.Column(db.String(200))
    to_ping = db.Column(db.Text)
    pinged = db.Column(db.Text)
    post_modified = db.Column(db.Datetime)
    post_modified_gmt = db.Column(db.Datetime)
    post_content_filtered = db.Column(db.Text)
    post_parent = db.Column(db.Integer)
    guid = db.Column(db.String(255))
    menu_order = db.Column(db.Integer)
    post_type = db.Column(db.String(20))
    post_mime_type = db.Column(db.String(100))
    comment_count = db.Column(db.Integer)