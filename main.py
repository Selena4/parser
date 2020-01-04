#-*- coding: utf-8 -*-

import vk_api,json, os, time, random

ids = [
47949197,
86886389,
54014337,
27720440,
33796840,
161440075,
93566453,
106761812,
132658506,
144854311,
57396876,
28015161,
86395110]

login,password = '',''
vk_session = vk_api.VkApi(login, password)
vk_session.auth()
vk = vk_session.get_api()
def get_last_post(owner_id):
    wall = vk.wall.get(owner_id = -1 * owner_id, count = 3)
    for item in wall['items']:
        if 'is_pinned' in item.keys():
            continue
        else:
            return item['id'] 

def create_comment(owner_id, post_id,msg):
    print(vk.wall.createComment(owner_id = -1*owner_id, post_id = post_id, attachments = 'photo568498616_457282031',message = msg))
if 'data.json' not in os.listdir('.'):
    lasts_posts = {}
    for pub in ids:
        wall = vk.wall.get(owner_id = -1 * pub, count = 3)
        for item in wall['items']:
            if 'is_pinned' in item.keys():
                continue
            else:
                lasts_posts[pub] = item['id'] 
                break
    json.dump(lasts_posts, open("data.json", "w"))
    print('data loaded')
else:
    lasts_posts = json.load(open('data.json','r'))
    print('data loaded')
while True:
    for owner_id in ids:
        try:
            if get_last_post(owner_id) != lasts_posts[str(owner_id)]:
                last_post = get_last_post(owner_id)
                try:
                    print('new_comment: https://vk.com/public{}?w=wall-{}_{}'.format(str(owner_id),str(owner_id),get_last_post(owner_id)))
                    msg = '> '
                    for i in range(20):msg = msg + random.choice('QWERTYUIOPASDFGHJKLZXCVBNM,./qwertyuiopasdfghjklzxcvbnm1234567890йцукенгшщзфывапролджячсмитьЙЦУКЕНГШЩЗФЫВАПРОЛДЯЧСМИТЬБ') 
                    create_comment(owner_id,last_post, msg)
                    print('sleeping 300s...')
                    time.sleep(300)
                except:
                    print('error')
                lasts_posts[str(owner_id)] = last_post
                json.dump(lasts_posts, open("data.json", "w"))
        except:
            print(str(owner_id) + ' - blacklist')
    print('sleeping 60s...')
    time.sleep(60)
    print('starting new loop')
