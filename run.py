# -*- coding: utf-8 -*-

import requests
import re
from wox import Wox


class HelloWorld(Wox):

    def query(self, query):
        results = []

        if re.match("^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", query):
            req = requests.get('http://ip-api.com/json/{}?fields=country,countryCode,regionName,city,district,zip,isp,asname,proxy'.format(query))
            location = req.json()

            if location['proxy'] == True:
                results.append({
                    "Title": "Privacy",
                    "SubTitle": 'Proxy, VPN or Tor exit address',
                    "IcoPath": 'ipstack.png',
                    "ContextData": "ctxData"
                })

            results.append({
                "Title": "{} - {}".format(location['country'], location['countryCode']),
                "SubTitle": location['regionName'],
                "IcoPath": 'ipstack.png',
                "ContextData": "ctxData"
            })
            results.append({
                "Title": "{} {}".format(location['city'], location['district']),
                "SubTitle": 'ZIP Code: {}'.format(location['zip']),
                "IcoPath": 'ipstack.png',
                "ContextData": "ctxData"
            })
            results.append({
                "Title": location['isp'],
                "SubTitle": location['asname'],
                "IcoPath": 'ipstack.png',
                "ContextData": "ctxData"
            })

            return results
        else:
            return


if __name__ == "__main__":
    HelloWorld()
