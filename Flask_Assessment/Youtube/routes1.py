import requests

from flask import Blueprint, current_app, request

main=Blueprint('main', __name__)

@main.route('/<name>', methods=['GET', 'POST'])
def index(name):
    search_url = 'https://www.googleapis.com/youtube/v3/search'
    channel_url = 'https://www.googleapis.com/youtube/v3/channels'

    all_data = []

    if request.method == 'GET':
        id_params = {
            'key': current_app.config['YOUTUBE_API_KEY'],
            'q' : name,
            'part': 'snippet',
            'type': 'channel'
        }
        r = requests.get(search_url, params=id_params)
        results = r.json()['items']
        channel_ids = []
        for result in results:
            channel_ids.append(result['id']['channelId'])

        Channel_params = {
            'key': current_app.config['YOUTUBE_API_KEY'],
            'id' : ','.join(channel_ids),
            'part': 'snippet, contentDetails, statistics',
        }
        r = requests.get(channel_url, params=Channel_params)
        results = r.json()['items'] 
        for result in results:
            channel_data = {
                'id' : result['id'],
                'url' : f'https://www.youtube.com/channel/{result["id"]}',
                'Channel_name' : result['snippet']['title'],
                'thumbnail':result['snippet']['thumbnails']['high']['url'],
                'Channel_stats' : result['statistics'],
            }
            print(result)
            all_data.append(channel_data)

    # return render_template('index1.html', videos=all_data)
    return dict(channels=all_data)