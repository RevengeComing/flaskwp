__all__ = (
    "generate_post_class",
    "generate_comment_class",
    "generate_user_class",
)

def generate_post_class(db):
    """
    table : wp_posts;
    +-----------------------+---------------------+------+-----+---------------------+----------------+
    | Field                 | Type                | Null | Key | Default             | Extra          |
    +-----------------------+---------------------+------+-----+---------------------+----------------+
    | ID                    | bigint(20) unsigned | NO   | PRI | NULL                | auto_increment |
    | post_author           | bigint(20) unsigned | NO   | MUL | 0                   |                |
    | post_date             | datetime            | NO   |     | 0000-00-00 00:00:00 |                |
    | post_date_gmt         | datetime            | NO   |     | 0000-00-00 00:00:00 |                |
    | post_content          | longtext            | NO   |     | NULL                |                |
    | post_title            | text                | NO   |     | NULL                |                |
    | post_excerpt          | text                | NO   |     | NULL                |                |
    | post_status           | varchar(20)         | NO   |     | publish             |                |
    | comment_status        | varchar(20)         | NO   |     | open                |                |
    | ping_status           | varchar(20)         | NO   |     | open                |                |
    | post_password         | varchar(255)        | NO   |     |                     |                |
    | post_name             | varchar(200)        | NO   | MUL |                     |                |
    | to_ping               | text                | NO   |     | NULL                |                |
    | pinged                | text                | NO   |     | NULL                |                |
    | post_modified         | datetime            | NO   |     | 0000-00-00 00:00:00 |                |
    | post_modified_gmt     | datetime            | NO   |     | 0000-00-00 00:00:00 |                |
    | post_content_filtered | longtext            | NO   |     | NULL                |                |
    | post_parent           | bigint(20) unsigned | NO   | MUL | 0                   |                |
    | guid                  | varchar(255)        | NO   |     |                     |                |
    | menu_order            | int(11)             | NO   |     | 0                   |                |
    | post_type             | varchar(20)         | NO   | MUL | post                |                |
    | post_mime_type        | varchar(100)        | NO   |     |                     |                |
    | comment_count         | bigint(20)          | NO   |     | 0                   |                |
    +-----------------------+---------------------+------+-----+---------------------+----------------+
    """
    class WPPost(db.Model):
        __bind_key__ = "wordpress"
        __tablename__ = "wp_posts"
        ID = db.Column(db.BigInteger, primary_key=True)
        post_author = db.Column(db.BigInteger)
        post_date = db.Column(db.DateTime)
        post_date_gmt = db.Column(db.DateTime)
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
        post_modified = db.Column(db.DateTime)
        post_modified_gmt = db.Column(db.DateTime)
        post_content_filtered = db.Column(db.Text)
        post_parent = db.Column(db.BigInteger)
        guid = db.Column(db.String(255))
        menu_order = db.Column(db.Integer)
        post_type = db.Column(db.String(20))
        post_mime_type = db.Column(db.String(100))
        comment_count = db.Column(db.BigInteger)

    return WPPost

def generate_user_class(db):
    """
    table : wp_users;
    +---------------------+---------------------+------+-----+---------------------+----------------+
    | Field               | Type                | Null | Key | Default             | Extra          |
    +---------------------+---------------------+------+-----+---------------------+----------------+
    | ID                  | bigint(20) unsigned | NO   | PRI | NULL                | auto_increment |
    | user_login          | varchar(60)         | NO   | MUL |                     |                |
    | user_pass           | varchar(255)        | NO   |     |                     |                |
    | user_nicename       | varchar(50)         | NO   | MUL |                     |                |
    | user_email          | varchar(100)        | NO   | MUL |                     |                |
    | user_url            | varchar(100)        | NO   |     |                     |                |
    | user_registered     | datetime            | NO   |     | 0000-00-00 00:00:00 |                |
    | user_activation_key | varchar(255)        | NO   |     |                     |                |
    | user_status         | int(11)             | NO   |     | 0                   |                |
    | display_name        | varchar(250)        | NO   |     |                     |                |
    +---------------------+---------------------+------+-----+---------------------+----------------+
    """
    class WPUser(db.Model):
        __bind_key__ = "wordpress"
        __tablename__ = "wp_users"
        ID = db.Column(db.BigInteger, primary_key=True)
        user_login = db.Column(db.String(60))
        user_pass = db.Column(db.String(255))
        user_nicename = db.Column(db.String(50))
        user_email = db.Column(db.String(100))
        user_url = db.Column(db.String(100))
        user_registered = db.Column(db.DateTime)
        user_activation_key = db.Column(db.String(255))
        user_status = db.Column(db.Integer)
        display_name = db.Column(db.String(250))

    return WPUser

def generate_comment_class(db):
    """
    table : wp_comments;
    +----------------------+---------------------+------+-----+---------------------+----------------+
    | Field                | Type                | Null | Key | Default             | Extra          |
    +----------------------+---------------------+------+-----+---------------------+----------------+
    | comment_ID           | bigint(20) unsigned | NO   | PRI | NULL                | auto_increment |
    | comment_post_ID      | bigint(20) unsigned | NO   | MUL | 0                   |                |
    | comment_author       | tinytext            | NO   |     | NULL                |                |
    | comment_author_email | varchar(100)        | NO   | MUL |                     |                |
    | comment_author_url   | varchar(200)        | NO   |     |                     |                |
    | comment_author_IP    | varchar(100)        | NO   |     |                     |                |
    | comment_date         | datetime            | NO   |     | 0000-00-00 00:00:00 |                |
    | comment_date_gmt     | datetime            | NO   | MUL | 0000-00-00 00:00:00 |                |
    | comment_content      | text                | NO   |     | NULL                |                |
    | comment_karma        | int(11)             | NO   |     | 0                   |                |
    | comment_approved     | varchar(20)         | NO   | MUL | 1                   |                |
    | comment_agent        | varchar(255)        | NO   |     |                     |                |
    | comment_type         | varchar(20)         | NO   | MUL |                     |                |
    | comment_parent       | bigint(20) unsigned | NO   | MUL | 0                   |                |
    | user_id              | bigint(20) unsigned | NO   |     | 0                   |                |
    +----------------------+---------------------+------+-----+---------------------+----------------+
    """
    class WPComment(db):
        __bind_key__ = "wordpress"
        __tablename__ = "wp_comments"
        comment_ID = db.Column(db.BigInteger, primary_key=True)
        comment_post_ID = db.Column(db.BigInteger)
        comment_author = db.Column(db.Text)
        comment_author_email = db.Column(db.String(100))
        comment_author_url = db.Column(db.String(200))
        comment_author_IP = db.Column(db.String(100))
        comment_date = db.Column(db.DateTime)
        comment_date_gmt = db.Column(db.DateTime)
        comment_content = db.Column(db.Text)
        comment_karma = db.Column(db.Integer)
        comment_approved = db.Column(db.String(20))
        comment_agent = db.Column(db.String(255))
        comment_type = db.Column(db.String(20))
        comment_parent = db.Column(db.BigInteger)
        user_id = db.Column(db.BigInteger)

    return WPComment