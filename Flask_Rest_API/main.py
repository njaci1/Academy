from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



class videos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    views = db.Column(db.Integer)
    likes = db.Column(db.Integer)

    def __init__(self, name, views, likes):
        self.name = name
        self.views = views
        self.likes = likes
#db.create_all()


video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video", required=True)
video_put_args.add_argument("views", type=int, help="Views on the video", required=True)
video_put_args.add_argument("likes", type=int, help="Likes on the video", required=True)

videos = {}

def abort_if_video_id_invalid(video_id):
    if video_id not in videos:
        abort(404, message="Invalid video id..")

def abort_if_video_exist(video_id):
    if video_id in videos:
        abort(409, message="Video id exist..")


class Video(Resource):
    def get(self, video_id):
        abort_if_video_id_invalid(video_id)
        return videos[video_id]

    def put(self, video_id):
        abort_if_video_exist(video_id)
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201

    def delete(self,video_id):
        abort_if_video_id_invalid(video_id)
        del videos[video_id]

        return '', 204





api.add_resource(Video, "/video/<int:video_id>")



if __name__ == "__main__":
    app.run(debug=True)