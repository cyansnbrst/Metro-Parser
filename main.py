import json
import requests

MOSCOW_SHOP_ID = 10  # Москва, Ул. Ленинградское шоссе, д. 71Г (м. Речной вокзал)
SPB_SHOP_ID = 15  # Санкт-Петербург, Ул. Комендантский пр-т, д. 3, лит. А (м. Комендантский пр-т)


def get_metro_data():
    cookies = {
        '_slid_server': '6626de7f42256d6ea0078c0c',
        '_slsession': 'BA0E3D73-B78A-4C6B-BA17-E35A347C0084',
        'active_order': '1',
        '_slid': '6626de7f42256d6ea0078c0c',
        '_ga': 'GA1.1.1007961831.1713823362',
        '_slfreq': '633ff97b9a3f3b9e90027740%3A633ffa4c90db8d5cf00d7810%3A1713830563%3B64a81e68255733f276099da5%3A64abaf645c1afe216b0a0d38%3A1713830563',
        'tmr_lvid': '6c24eca6c61b7c9742031ec7bc431707',
        'tmr_lvidTS': '1713823363367',
        '_ym_uid': '171382336361713651',
        '_ym_d': '1713823363',
        '_gcl_au': '1.1.728499439.1713823363',
        'metro_api_session': 'Z8MoKPJopQQO0hefNRnqpnQpslSX6ERNBnrzFv6n',
        '_ym_isad': '1',
        'metro_user_id': 'e7c8208bcd42729642457f1828f70e6f',
        '_ym_visorc': 'b',
        'uxs_uid': '0cc91660-00f4-11ef-90f2-4b037dffef76',
        'mindboxDeviceUUID': 'c961a8fc-29b7-4ba7-a051-a02c904e430e',
        'directCrm-session': '%7B%22deviceGuid%22%3A%22c961a8fc-29b7-4ba7-a051-a02c904e430e%22%7D',
        '_slfs': '1713823393365',
        'mp_5e1c29b29aeb315968bbfeb763b8f699_mixpanel': '%7B%22distinct_id%22%3A%20%22%24device%3A18f07d531ff1ad7-0a11969d07a6a3-26001d51-144000-18f07d531ff1ad7%22%2C%22%24device_id%22%3A%20%2218f07d531ff1ad7-0a11969d07a6a3-26001d51-144000-18f07d531ff1ad7%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fonline.metro-cc.ru%2F%22%2C%22%24initial_referring_domain%22%3A%20%22online.metro-cc.ru%22%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fonline.metro-cc.ru%2F%22%2C%22%24initial_referring_domain%22%3A%20%22online.metro-cc.ru%22%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%7D',
        'mp_88875cfb7a649ab6e6e310368f37a563_mixpanel': '%7B%22distinct_id%22%3A%20%22%24device%3A18f07d532051adc-0aac46d26968d2-26001d51-144000-18f07d532051adc%22%2C%22%24device_id%22%3A%20%2218f07d532051adc-0aac46d26968d2-26001d51-144000-18f07d532051adc%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fonline.metro-cc.ru%2F%22%2C%22%24initial_referring_domain%22%3A%20%22online.metro-cc.ru%22%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fonline.metro-cc.ru%2F%22%2C%22%24initial_referring_domain%22%3A%20%22online.metro-cc.ru%22%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%7D',
        '_ga_VHKD93V3FV': 'GS1.1.1713823361.1.1.1713823457.0.0.0',
    }

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,es;q=0.6',
        'content-type': 'application/json',
        'origin': 'https://online.metro-cc.ru',
        'priority': 'u=1, i',
        'referer': 'https://online.metro-cc.ru/',
        'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    }

    json_data = {
        "query": "\n  query Query($storeId: Int!, $slug: String!, $attributes:[AttributeFilter], $filters: [FieldFilter], $from: Int!, $size: Int!, $sort: InCategorySort, $in_stock: Boolean, $eshop_order: Boolean, $is_action: Boolean, $priceLevelsOnline: Boolean) {\n    category (storeId: $storeId, slug: $slug, inStock: $in_stock, eshopAvailability: $eshop_order, isPromo: $is_action, priceLevelsOnline: $priceLevelsOnline) {\n      products(attributeFilters: $attributes, from: $from, size: $size, sort: $sort, fieldFilters: $filters)  "
                 "{\n        id\n        name\n        url\n        stocks {\n          prices {\n            price\n            old_price\n          }\n        }\n        manufacturer {\n          name\n        }\n      }\n    }\n  }\n",
        "variables": {
            "storeId": SPB_SHOP_ID,
            "sort": "default",
            "size": 500,
            "from": 0,
            "filters": [
                {
                    "field": "main_article",
                    "value": "0"
                }
            ],
            "attributes": [],
            "in_stock": True,
            "eshop_order": True,
            "allStocks": False,
            "slug": "makaronnye-izdeliya"
        }
    }

    response = requests.post('https://api.metro-cc.ru/products-api/graph',
                             cookies=cookies, headers=headers, json=json_data)

    return response.json()


def save_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def process_metro_data(json_data):
    if "data" in json_data:
        json_data = json_data["data"]
    if "category" in json_data:
        json_data = json_data["category"]

    for product in json_data["products"]:
        if "manufacturer" in product:
            product["brand_name"] = product.pop("manufacturer")["name"]
        if "stocks" in product and product["stocks"]:
            stocks = product.pop("stocks")[0]
            product["prices"] = stocks["prices"]

    return json_data


if __name__ == "__main__":
    metro_data = get_metro_data()
    metro_data = process_metro_data(metro_data)
    save_to_json(metro_data, 'spb-metro.json')
