import requests
import os
from urllib.parse import urlparse
from tqdm import tqdm

def indir(url, klasor="indirilenler"):
    response = requests.get(url, stream=True)
    dosya_adi = os.path.basename(urlparse(url).path)
    kayit_yolu = os.path.join(klasor, dosya_adi)

    if not os.path.exists(klasor):
        os.makedirs(klasor)

    dosya_boyutu = int(response.headers.get("content-length", 0))
    with open(kayit_yolu, "wb") as dosya, tqdm(
        desc=dosya_adi,
        total=dosya_boyutu,
        unit="B",
        unit_scale=True,
        unit_divisor=1024,
    ) as ilerleme_cubugu:
        for veri in response.iter_content(chunk_size=1024):
            dosya.write(veri)
            ilerleme_cubugu.update(len(veri))

    print(f"\n{dosya_adi} dosyası başarıyla indirildi.")

# İndirmek istediğiniz URL'yi buraya girin
url = "http://arioiptv.xyz:8080/movie/tesat/fsafsaf/151219.mkvbrbrbu"

indir(url)
