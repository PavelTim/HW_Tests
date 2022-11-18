import requests


class YaDiskDel:

    def __init__(self, token):
        ''' Обряд инициации. Пляски с токеном. '''
        self.token = token
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {token}'
        }


    # тестируемые функции
    # -------------------------------------------------------------------------
    def dirinfo(self, path, allfields=False):
        ''' Проверяет наличие каталога на яндекс диске.
        404 папки не существует
        200 папка существует
        '''
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        params = {'path': path}
        if not allfields:
            params['fields'] = 'type'
        res = requests.get(url, headers=self.headers, params=params)
        return res.status_code


    def createdir(self, path):
        ''' создает папку на яндекс диске.
        201 Success папка создана
        409 Success папка цже существует '''
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        params = {'path': path}
        res = requests.put(url, headers=self.headers, params=params)
        return res.status_code


    def deletedir(self, path):
        ''' создает папку на яндекс диске.
        201 Success папка создана
        409 Success папка цже существует '''
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        params = {'path': path}
        res = requests.delete(url, headers=self.headers, params=params)
        return res.status_code
     # ---------------------------------------------------------------------


    def diskinfo(self, allfields=False):
        ''' Возвращает информацию о диске. '''
        url = 'https://cloud-api.yandex.net/v1/disk'
        if allfields:
            params = {'fields': 'total_space, used_space'}
            res = requests.get(url, headers=self.headers, params=params)
        else:
            res = requests.get(url, headers=self.headers)
        res.raise_for_status()
        if res.status_code == 200:
            print(f'diskinfo Success, allfiels = {allfields}')
        return res.json()


    def linkupload(self, path, overwrite=True):
        ''' Дает url ссылку для загрузки на яндекс диск файла с компьютера пользователя.
        Для наших целей не используется. '''
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        params = {'path': path, 'overwrite': overwrite}
        res = requests.get(url, headers=self.headers, params=params)
        res.raise_for_status()
        if res.status_code == 200:
            print(f'linkupload Success, res.status_code = {res.status_code}')
            return res.json().get('href', "")
        print(f'linkupload Непонятная ошибка. status: {res.status_code}')

    def urlupload(self, url, path, overwrite=True):
        ''' Загружает картинку по ссылки в папку на яндекс диске.
        path - папка на яндекс диске,
        url -  ссылка на картинку в интернете. '''
        url_upload = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        params = {'path': path, 'url': url, 'overwrite': overwrite}
        res = requests.post(url_upload, headers=self.headers, params=params)
        res.raise_for_status()

        if res.status_code == 202:
            print(f'linkupload Success, res.status_code = {res.status_code}')
            return res.json().get('href', "")
        print(f'urlupload Непонятная ошибка. status: {res.status_code}')
        return res.json().get('href', "")

    def gedonism(self):
        ''' В каждом классе обязательно есть функция,
        которой никто никогда не пользуется и никто не знает, зачем она нужна.
        Эта функция получает удовольствие сама для себя, просто потому, что она существует. '''
        self.gedonism.message = "Я существую, а следовательно я получаю удовольствие."
        self.gedonism.count = 0
        for i in range(1000):
            self.gedonism.count += 1
            pass


if __name__ == "__main__":
    pass