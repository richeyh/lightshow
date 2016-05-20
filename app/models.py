from extensions import DB


class LightScript(DB.Model):
    """
    The lightscript object to store to the DB
    script : the script stored in the DB
    color_one : flag to determine if a first color input is required
    color_two : flag to determine if a second color input is required
    speed : flag to determine if speed flag is required
    division : flag to determine if subdivision is required
    """
    __tablename__ = "scripts"
    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String(150))
    script = DB.Column(DB.Text)
    color_one = DB.Column(DB.Boolean())
    color_two = DB.Column(DB.Boolean())
    speed = DB.Column(DB.Boolean())
    division = DB.Column(DB.Boolean())
