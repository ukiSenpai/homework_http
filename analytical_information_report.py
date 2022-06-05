# Задача №1
# Кто самый умный супергерой? Есть API по информации о супергероях. Нужно определить кто самый умный(intelligence) из
# трех супергероев- Hulk, Captain America, Thanos. Для определения id нужно использовать метод /search/name
#
# Токен, который нужно использовать для доступа к API: 2619421814940190.
# Таким образом, все адреса для доступа к API должны начинаться с https://superheroapi.com/api/2619421814940190/.
#
# -> ⚠️ Недавно сервис SuperHero API переехал на заблокированный Роскомнадзором IP-адрес,
# из-за чего некоторые интернет-провайдеры заблокировали к нему доступ, он может быть недоступен.
# В таком случае решайте это задание на REPL.it — оттуда всё должно быть доступно.


import requests

API_URL = "https://superheroapi.com/api/2619421814940190"
FIND_ID_PREFIX = "/search/"


def get_hero_params(name: str) -> list:
    resp = requests.get(f"{API_URL}{FIND_ID_PREFIX}{name}")
    return resp.json()['results']

def find_more_intelligens_hero(hero_list:list)-> str:
    hero_list.sort( key=lambda hero:int(hero['powerstats']['intelligence']),reverse=True)
    return hero_list[0]['name']

def main():
    heroes = {'Hulk': dict(), 'Captain America': dict(), 'Thanos': dict()}
    for hero in heroes:
        heroes[hero] = get_hero_params(hero)

    heroes_list = []
    for hero, param in heroes.items():
        heroes_list.extend(param)
    more_int_hero = find_more_intelligens_hero(heroes_list)
    print(more_int_hero)

if __name__ == '__main__':
    main()
