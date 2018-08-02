from flask import request, jsonify,render_template
import json
from . import web
from music.app.forms.form_music import Keyword_Music
from music.app.libs.search_music import Search_Music
from music.app.views_model.music_view_model import MusicViewModel
from lib.weather import weather, weather_viewmodel
import random

@web.route('/music/search')
def music1():
    form = Keyword_Music(request.args)

    w = weather.Weather()
    w_d = weather_viewmodel.Weather_data()
    w_d.fill(w.get_weather_data()['weatherinfo'])

    if form.validate():
        keyword = form.q.data
        # print(keyword)
        response1 = Search_Music.search_by_keyword(keyword)
        hashcode = MusicViewModel.get_hash(response1)[0]
        album_list = MusicViewModel.get_album_id(response1)
        album_id=album_list[0]
        response2 = json.loads(Search_Music.deal_hashcode(hashcode, album_id))
        music_detial = MusicViewModel.music_detial(response1, response2, keyword) 
        # print(music_detial) #歌曲的信息
        # return jsonify(music_detial)
        author_name = music_detial['author_name']
        img = music_detial['img']
        play_url = music_detial['play_url']
        song_name = music_detial['song_name']

        return render_template('music.html', img=img, author_name=author_name, song_name=song_name, play_url=play_url, city=w_d.city, temp1=w_d.temp1, temp2=w_d.temp2, weather=w_d.weather)

