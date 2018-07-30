from wtforms import Form, StringField
from wtforms.validators import Length


class Keyword_Music(Form):
    q = StringField('keyword', validators=[Length(min=0,max=10)])
