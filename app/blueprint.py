from flask import Blueprint
import views

blueprint = Blueprint('lightshow', __name__)
blueprint.add_url_rule('/', view_func=views.IndexView.as_view('Home'))
blueprint.add_url_rule('/index', view_func=views.IndexView.as_view('Index'))
blueprint.add_url_rule('/playShow', view_func=views.PlayView.as_view('Play'))
