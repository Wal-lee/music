from music.app.libs.http import HTTP
import json
import re




# def get_albumid(data):
#     albumid_list = re.findall('"AlbumID":"([0-9]*)"', data)
#     # print(albumid_list)
#     return albumid_list

# def zip_data(data):
#     hash_list = get_hash(data)
#     albumid_list = get_albumid(data)
#     data_list = zip(hash_list, albumid_list)
#     return list(data_list)

# def get_author(data):
#     author_name = data['data']['author_name']
#     return author_name

# def get_play_url(data):
#     play_url = data['data']['play_url']
#     return play_url

# def get_album_name(data):
#     album_name = data['data']['album_name']
#     return album_name

class Search_Music():
    URL = 'http://songsearch.kugou.com/song_search_v2?keyword={}&page=1&pagesize=1&userid=-1&clientver=&platform=WebFilter&tag=em&filter=2&iscorrection=1&privilege_filter=0'
    URL2 = 'http://www.kugou.com/yy/index.php?r=play/getdata&hash={}&album_id={}'
    @classmethod
    def search_by_keyword(cls, keyword):
        response = HTTP.http_get(cls.URL.format(keyword))
        return response
        
    
    @classmethod
    def deal_hashcode(cls, hashcode, album_id):
        response = HTTP.http_get(cls.URL2.format(hashcode, album_id))
        return response
