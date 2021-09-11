import requests
import shutil
import datetime
import os

#Base URL for downloading forest information (lat and lon will be added on as a variable query)
base_url = "https://ies-ows.jrc.ec.europa.eu/iforce/tmf_v1/download.py?type=tile&dataset=TransitionMap_MainClasses&"
lon_val = ['E', 'W']
lat_val = ['N', 'S']
c: int = 0

initial_start_time = datetime.datetime.now()

#looping through all lat and lon range on the map
for i in range(0, 40, 10):
    for j in range(0, 180, 10):
        for k in lat_val:
            for l in lon_val:
                after_url = f"lat={k}{i}&lon={l}{j}"
                #requesting content from custom URL
                r = requests.get(f"{base_url}{after_url}", stream=True)
                #cheeking if URL link is valid
                if r.status_code in range(200, 299):
                    begin_time = datetime.datetime.now()
                    print(f"{after_url} MATCHES")
                    c += 1
                    if (os.path.isfile(f"{after_url}.tiff")):
                        print(f"{after_url}.tiff is already downloaded")
                        print(f"{c} tiff file(s) downloaded locally")

                        continue
                    r.raw.decode_content = True
                    with open(f"{after_url}.tiff", 'wb') as f:
                        print('Download starting now (may take a couple of minutes)')
                        #downloaded tiff file from link
                        shutil.copyfileobj(r.raw, f)
                        print(f"successfully downloaded tiff file in {(datetime.datetime.now()-begin_time).total_seconds()} seconds")
                        print(f"{c} tiff file(s) downloaded locally")
                else:
                    print("skip")

print(f'all {c} tiff files downloaded')
print(f"Took a total of {(datetime.datetime.now()-initial_start_time).total_seconds()} seconds")