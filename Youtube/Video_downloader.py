from pytube import *

def downloader(url):
    """
    Burada pytube modülünde bulunan tüm özellikleri buraya aktardık. Bizim için önemli olan Youtube class'ı.
    """
    # Kaydedilecek konum.
    save = "D:/"

    # indirmeye başlamak için ilk adım Youtube class'ına url'yi gönderiyoruz.
    # yt adında bir tane Youtube class'ına ait nesneyi oluşturduk.
    yt = YouTube(url)

    # mp4 değişkenine mp4 niteliğindeki en iyi hem ses hemde görüntü içeriğini beraber indirebilmek için get.. fonksiyonunu kullandık.
    # Her piksel değerine özel itag değeri vardır. akışlara yani streamslerden bunu öğrenebiliriz. "yt.streams"
    # en iyi sonuç 720p' dir ve itag = 22
    mp4 = yt.streams.filter(file_extension="mp4").get_highest_resolution()

    # download özelliğini kullanarak ve içeriğine parametre olarak nereye inmesini istiyorsak konumu (path) vererek indirebiliriz.
    mp4.download(save)

