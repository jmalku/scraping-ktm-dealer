import requests
import pandas as pd


list_results = []
def get_data(country):
    req_url = f'https://www.ktm.com/content/websites/ktm-com/middle-east/ae/en/dealer-search/jcr:content/root/responsivegrid_1_col/dealersearch.dealers.json?latitude=55.378051&longitude=-3.435973&country={country}&qualification='
    resp = requests.get(req_url)
    json_data = resp.json()
    # print(resp.status_code)
    # print(json_data)
    get_data = json_data['data']
    # print(get_data)
    # print(len(get_data))
    count = 0
    if len(get_data) == 0:
        print('skip no data')
    else:
        for i in get_data:
            count += 1
            country = i['country']
            name = i['name']
            phone = i['phone']
            try:
                email = i['email']
            except KeyError:
                email = ''
            dealerNo = i['dealerNo']
            geoCodeLongitude = i['geoCodeLongitude']
            geoCodeLatitude = i['geoCodeLatitude']
            postcode = i['postcode']
            town = i['town']
            street = i['street']
            try:
                region = i['region']
            except KeyError:
                region = ''
            # openingHour = i['openingHour']
            fax = i['fax']
            websiteFullUrl = i['websiteFullUrl']

            goal_data = {
                'country': country,
                'name': name,
                'phone': phone,
                'email': email,
                'dealerNo': dealerNo,
                'geoCodeLongitude': geoCodeLongitude,
                'geoCodeLatitude': geoCodeLatitude,
                'postcode': postcode,
                'town': town,
                'street': street,
                'region': region,
                # 'openingHour': openingHour,
                'fax': fax,
                'websiteFullUrl': websiteFullUrl
            }

            list_results.append(goal_data)
            print(f'{count}. {goal_data}')

# get_data('BE')
list_country = ['AF', 'AX', 'AL', 'DZ', 'AS', 'AD', 'AO', 'AI', 'AQ', 'AG', 'AR', 'AM', 'AW', 'AU', 'AT', 'AZ', 'BS',
                'BH', 'BD', 'BB', 'BY', 'BE', 'BZ', 'BJ', 'BM', 'BT', 'BO', 'BQ', 'BA', 'BW', 'BV', 'BR', 'IO', 'BN',
                'BG', 'BF', 'BI', 'CV', 'KH', 'CM', 'CA', 'KY', 'CF', 'TD', 'CL', 'CN', 'CX', 'CC', 'CO', 'KM', 'CD',
                'CG', 'CK', 'CR', 'CI', 'HR', 'CU', 'CW', 'CY', 'CZ', 'DK', 'DJ', 'DM', 'DO', 'EC', 'EG', 'SV', 'GQ',
                'ER', 'EE', 'SZ', 'ET', 'FK', 'FO', 'FJ', 'FI', 'FR', 'GF', 'PF', 'TF', 'GA', 'GM', 'GE', 'DE', 'GH',
                'GI', 'GR', 'GL', 'GD', 'GP', 'GU', 'GT', 'GG', 'GN', 'GW', 'GY', 'HT', 'HM', 'VA', 'HN', 'HK', 'HU',
                'IS', 'IN', 'ID', 'IR', 'IQ', 'IE', 'IM', 'IL', 'IT', 'JM', 'JP', 'JE', 'JO', 'KZ', 'KE', 'KI', 'KP',
                'KR', 'KW', 'KG', 'LA', 'LV', 'LB', 'LS', 'LR', 'LY', 'LI', 'LT', 'LU', 'MO', 'MK', 'MG', 'MW', 'MY',
                'MV', 'ML', 'MT', 'MH', 'MQ', 'MR', 'MU', 'YT', 'MX', 'FM', 'MD', 'MC', 'MN', 'ME', 'MS', 'MA', 'MZ',
                'MM', 'NA', 'NR', 'NP', 'NL', 'NC', 'NZ', 'NI', 'NE', 'NG', 'NU', 'NF', 'MP', 'NO', 'OM', 'PK', 'PW',
                'PS', 'PA', 'PG', 'PY', 'PE', 'PH', 'PN', 'PL', 'PT', 'PR', 'QA', 'RE', 'RO', 'RU', 'RW', 'BL', 'SH',
                'KN', 'LC', 'MF', 'PM', 'VC', 'WS', 'SM', 'ST', 'SA', 'SN', 'RS', 'SC', 'SL', 'SG', 'SX', 'SK', 'SI',
                'SB', 'SO', 'ZA', 'GS', 'SS', 'ES', 'LK', 'SD', 'SR', 'SJ', 'SE', 'CH', 'SY', 'TW', 'TJ', 'TZ', 'TH',
                'TL', 'TG', 'TK', 'TO', 'TT', 'TN', 'TR', 'TM', 'TC', 'TV', 'UG', 'UA', 'AE', 'GB', 'UM', 'US', 'UY',
                'UZ', 'VU', 'VE', 'VN', 'VG', 'VI', 'WF', 'EH', 'YE', 'ZM', 'ZW']
count_cntry = 0
for x in range(0, len(list_country)):
    count_cntry += 1
    cd = list_country[x]
    print(f'{count_cntry}. Country: {cd}')
    get_data(cd)
    df = pd.DataFrame(list_results)
    df.to_csv(f'ktm_dealer.csv', index=False)
