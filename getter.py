import requests as r
import shutil
"""from seleniumwire import webdriver
import requests as r

driver = webdriver.Chrome("C:\\Users\\clone\\Desktop\\chromedriver.exe")

driver.get("https://twist.moe/a/ookami-to-koushinryou/2")

file = open("vid.mpv", "w")

for req in driver.requests:
    print(req)"""

headers = {"authority": "edge-23.cdn.bunny.sh",
            "method": "GET",
            "path": "/anime/itainowalyananodebougyoryokunikyokufurishitaitoomoimasu/[HorribleSubs]%20Itai%20no%20wa%20Iya%20nano%20de%20Bougyoryoku%20ni%20Kyokufuri%20Shitai%20to%20Omoimasu%20-%2009%20[1080p].mp4",
            "scheme": "https",
            "accept": "*/*",
            "accept-encoding": "identity;q=1, *;q=0",
            "accept-language": "en-US,en;q=0.9",
            "range": "bytes=0-",
            "referer": "https://twist.moe/a/itai-no-wa-iya-nano-de-bougyoryoku-ni-kyokufuri-shitai-to-omoimasu/9",
            "sec-fetch-dest": "video",
            "sec-fetch-mode": "no-cors",
            "sec-fetch-site": "cross-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}


"""with r.get("https://edge-23.cdn.bunny.sh/anime/itainowalyananodebougyoryokunikyokufurishitaitoomoimasu/[HorribleSubs]%20Itai%20no%20wa%20Iya%20nano%20de%20Bougyoryoku%20ni%20Kyokufuri%20Shitai%20to%20Omoimasu%20-%2009%20[1080p].mp4",
              headers=headers, stream=True) as vid:
    with open("C:\\Users\\clone\\Downloads\\hurt.mp4", "wb") as file:
        shutil.copyfileobj(vid.raw, file)

print("Done!")"""

class getter():
    def __init__(self, site, headersF, referer, location):



        self.site = site
        self.rawHeader = headersF
        self.referer = referer

        self.clean = {"authority": self.auth(headersF),
                    "method": "GET",
                    "path": self.path(site),
                    "scheme": "https",
                    "accept": "*/*",
                    "accept-encoding": "identity;q=1, *;q=0",
                    "accept-language": "en-US,en;q=0.9",
                    "range": "bytes=0-",
                    "referer": referer,
                    "sec-fetch-dest": "video",
                    "sec-fetch-mode": "no-cors",
                    "sec-fetch-site": "cross-site",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}

        print(self.clean)

        self.requester(site, self.clean, location)

    def auth(self, rawH):
        return rawH["Host"]

    def path(self, site):
        site = site.split("/")
        site = site[len(site) - 3] + "/" + site[len(site) - 2] + "/" + site[len(site) - 1]
        return site

    def requester(self, site, headers, location):
        with r.get(site, headers=headers, stream=True) as vid:
            print(vid)
            a = open(location,"wb")
            print(a)
            with a  as file:
                shutil.copyfileobj(vid.raw, file)