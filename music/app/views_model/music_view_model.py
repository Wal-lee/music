import re


class MusicViewModel:
    @classmethod
    def music_detial(cls, data1, data2, keyword):
        returned = cls.__cut_music_data1(data1, keyword).copy()
        returned.update(cls.__cut_music_data2(data2))
        return returned

    @classmethod
    def __cut_music_data1(cls, data1, keyword):
        music_part1 = {
            'song_name': keyword,
            'hashcode': cls.get_hash(data1)[0]
        }
        # print(music_part1)
        return music_part1
    
    @classmethod
    def __cut_music_data2(cls, data2):
        music_part2 = {
            'author_name': data2['data']['author_name'],
            'play_url': data2['data']['play_url'],
            'img': data2['data']['img']
        }
        # print(music_part2)
        return music_part2

    @classmethod
    def get_hash(cls, data):
        hash_list = re.findall('"FileHash":"([A-Z0-9]*)"', data)
        # print(hash_list)
        return hash_list
    
    @classmethod
    def get_album_id(cls, data):
        albumid_list = re.findall('"AlbumID":"([0-9]*)"', data)
        # print(albumid_list)
        return albumid_list
