import os, requests, folium

def get_info_by_ip(ip):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        data = {
            '[IP]': response.get('query'),
            '[Int prov]': response.get('isp'),
            '[Org]': response.get('org'),
            '[Country]': response.get('country'),
            '[Region Name]': response.get('regionName'),
            '[City]': response.get('city'),
            '[ZIP]': response.get('zip'),
            '[Lat]': response.get('lat'),
            '[Lon]': response.get('lon'),
        }
        
        location = response.get('city')

        if os.path.isfile(f"data/{location}.txt"):
            print('Файл с таким именем уже создан.')
        else:

            with open(f"data/txt/{location}.txt", mode='a', encoding='utf-8') as f:
                for target, info in data.items():
                    f.write(f'{target} : {info}\n')

            area = folium.Map(location=[response.get('lat'), response.get('lon')])
            area.save(f"data/html/{response.get('query')}_{location}.html")
            print('Файл успешно создан.')

    except requests.exceptions.ConnectionError:
        print('[!] Please check')

def main():
    ip = input('Plese enter a target IP: ')
    get_info_by_ip(ip=ip)

if __name__ == '__main__':
    main()