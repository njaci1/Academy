from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# The DB layer
# Flask app
app = Flask(__name__)

# setup sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///artist.db'
db = SQLAlchemy(app)

# Define a class for the Artist table
class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    birth_year = db.Column(db.Integer)
    genre = db.Column(db.String)

# Create the table
#db.create_all()

#####################################################

# Abstraction layer

from marshmallow_jsonapi.flask import Schema
from marshmallow_jsonapi import fields

# Create data abstraction layer
class ArtistSchema(Schema):
    class Meta:
        type_ = 'artist'
        self_view = 'artist_one'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'artist_many'

    id = fields.Integer()
    name = fields.Str(required=True)
    birth_year = fields.Integer(load_only=True)
    genre = fields.Str()

##########################################################
#resource manager layer and endpoints

from flask_rest_jsonapi import Api, ResourceDetail, ResourceList

class ArtistMany(ResourceList):
    schema = ArtistSchema
    data_layer = {'session': db.session,
                  'model': Artist}

class ArtistOne(ResourceDetail):
    schema = ArtistSchema
    data_layer = {'session': db.session,
                  'model': Artist}

api = Api(app)
api.route(ArtistMany, 'artist_many', '/artists')
api.route(ArtistOne, 'artist_one', '/artists/<int:id>')

# main loop to run app in debug mode
if __name__ == '__main__':
    app.run(debug=True)







