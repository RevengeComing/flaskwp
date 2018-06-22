def generate_template_tags(fwp):
    flask_wp_filters = {}
    
    def get_latest_posts(count=10):
        return fwp.Post.query.fitler_by(
            post_type="post",post_status="publish"
        ).order_by(fwp.Post.post_date.desc()).limit(count)
    flask_wp_filters['get_lates_posts'] = get_lates_posts

    def get_featured_posts(count=10):
        


    return flask_wp_filters