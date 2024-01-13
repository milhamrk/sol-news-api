from bs4 import BeautifulSoup
from requests import get

base_url = 'https://www.cnnindonesia.com'

class CNN:
    """
    Mengambil berbagai berita dari website cnnindonesia.com
    
    Contoh:
        - mengambil berita internasional
        from src import cnn

        print(cnn.berita_internasional())
    """

    def query(self, url):
        """
        Mengambil data dari body berita
        
        :param url: url yang datanya ingin diambil
        :return: list dictionaries.
        """
        datas = get(url)
        soup = BeautifulSoup(datas.text, 'html.parser')
        articles = soup.find_all('article', class_='flex-grow')
        data = []

        for article in articles:
            try:
                link_tag = article.find('a', href=True)
                title = article.find('h2').text.strip()
                link = link_tag['href'].strip()
                image_tag = article.find('img')
                image_src = image_tag['src'].strip() if image_tag else None

                data.append({
                    "judul": title,
                    "link": link,
                    "poster": image_src,
                })
            except Exception as e:
                print(f"Error processing article: {e}")

        return data

    def index(self):
        """
        It returns the result of the query of the home news from cnn's site
        :return: The response object.
        """
        return self.query('{}/'.format(base_url))

    def berita_nasional(self):
        """
        Mengambil berita nasional

        :return: list dictionary
        """
        return self.query('{}/nasional'.format(base_url))

    def berita_internasional(self):
        """
        Mengambil berita internasional / luar negeri
        
        :return: list dictionary
        """
        return self.query('{}/internasional'.format(base_url))

    def berita_ekonomi(self):
        """
        Mengambil berita ekonomi
        
        :return: list dictionary
        """
        return self.query('{}/ekonomi'.format(base_url))

    def berita_olahraga(self):
        """
        Mengambil berita olahraga
        
        :return: list dictionary
        """
        return self.query('{}/olahraga'.format(base_url))

    def berita_teknologi(self):
        """
        Mengambil berita teknologi
        
        :return: list dictionary
        """
        return self.query('{}/teknologi'.format(base_url))

    def berita_hiburan(self):
        """
        Mengambil berita hiburan
        
        :return: list dictionary
        """
        return self.query('{}/hiburan'.format(base_url))

    def berita_social(self):
        """
        Mengambil berita sosial
        
        :return: list dictionary
        """
        return self.query('{}/gaya-hidup'.format(base_url))

    def detail(self, url):
        """
        Mengambil detail berita
        :args:
            url : string -> url berita
        :example:
            url : string -> https://www.cnnindonesia.com/teknologi/20220921153459-190-850830/cara-menghapus-data-iphone-sebelum-dijual
        :return: list dictionary
        """
        data = []
        try:
            req = get(url)
            soup = BeautifulSoup(req.text, 'html.parser')
            tag = soup.find('div', class_="detail_text")
            gambar = soup.find('div', class_='media_artikel').find('img').get('src')
            judul = soup.find('h1', class_='title').text
            body = tag.text
            data.append({
                "judul": judul,
                "poster": gambar,
                "body": body,
            })
        except:
            data.append({
                "message": "network error",
            })

        return data

    def search(self,q):
        """
        Mencari berita spesifik berdasarkan query

        :args:
            q : string -> query atau berita yang ingin dicari
        :returns: list dictionary
        """

        return self.query('{}/search/?query={}'.format(base_url, q))

if __name__ != '__main__':
    cnn = CNN()