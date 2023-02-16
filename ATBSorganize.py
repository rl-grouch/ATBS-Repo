#! python
# ATBSorganize.py - search pdf text for filenames, move matches to folder

# ch.1 start pg. 50
import bs4, requests, lxml, os, shutil

# get list of .py files in automatestuff folder
pyFiles = []
folderPath = 'C:\\users\\steve\\python\\projects\\automatestuff'
for file in os.listdir(folderPath):
    if file.endswith('.py'):
        pyFiles.append(file)


#navigate to website, parse text
res = requests.get('https://automatetheboringstuff.com/')
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'lxml')

#find chapter links
chapters = soup.select('html body div.main main div ul li a') #returns chapter object list
#ex. <a href="/2e/chapter0/">Introduction</a>, <a href="/2e/chapter1/">Chapter  1 – Python Basics</a>

for chapter in chapters:
    chPage = requests.get('https://automatetheboringstuff.com' + chapter['href'])
    chPage.raise_for_status()
    
    #TODO: search page for text that matches filename in automatestuff folder
    chSoup = bs4.BeautifulSoup(chPage.text, 'lxml') #parse each chapter page
    textSearch = chSoup.select('.calibre p') #search for text
    for item in textSearch:
        for file in pyFiles:
            if file in item.text:
                dest = os.path.join(folderPath, chapter.text)
                os.makedirs(dest, exist_ok=True)
                shutil.copy(os.path.join(folderPath, file), dest)
                print(f'Copied {file} to {dest}...')



## program failed on ch. 20 , not sure why --- otherwise successful
# Traceback (most recent call last):
#   File "C:\Users\steve\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 174, in _new_conn   
#     conn = connection.create_connection(
#   File "C:\Users\steve\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\connection.py", line 72, in create_connection
#     for res in socket.getaddrinfo(host, port, family, socket.SOCK_STREAM):
#   File "C:\Users\steve\AppData\Local\Programs\Python\Python310\lib\socket.py", line 955, in getaddrinfo
#     for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
# socket.gaierror: [Errno 11001] getaddrinfo failed

# During handling of the above exception, another exception occurred:

# Traceback (most recent call last):
#   File "C:\Users\steve\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 703, in urlopen 
#     httplib_response = self._make_request(
#   File "C:\Users\steve\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 386, in _make_request
#     self._validate_conn(conn)
#   File "C:\Users\steve\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 1042, in _validate_conn
#     conn.connect()
#   File "C:\Users\steve\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 358, in connect     
#     self.sock = conn = self._new_conn()
#   File "C:\Users\steve\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 186, in _new_conn   
#     raise NewConnectionError(
# urllib3.exceptions.NewConnectionError: <urllib3.connection.HTTPSC
# d
#     resp = conn.urlopen(
#   File "C:\Users\steve\AppData\Local\Programs\Python\Python310\lib\site-packages\urllrllib3\connectionpool.py", line 787, in urlopen
#     retries = retries.increment(
#   File "C:\Users\steve\AppData\Local\Programs\Python\Python310\lib\site-packages\urllrllib3\util\retry.py", line 592, in increment
#     raise MaxRetryError(_pool, url, error or ResponseError(cause))
# urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='automatetheboringstuff.co.comhttps', port=443): Max retries exceeded with url: //www.nostarch.com/download/omaAutomate_the_Boring_Stuff_onlinematerials.zip (Caused by NewConnectionError('<urllnneib3.connection.HTTPSConnection object at 0x000001D5F43D6890>: Failed to establish nec
# a new connection: [Errno 11001] getaddrinfo failed'))

# During handling of the above exception, another exception occurred:

# Traceback (most recent call last):
#   File "c:\Users\steve\python\projects\automatestuff\ATBS repo\ATBSorganize.py", lineine 26, in <module>
#     chPage = requests.get('https://automatetheboringstuff.com' + chapter['href'])    
#   File "C:\Users\steve\AppData\Local\Programs\Python\Python310\lib\site-packages\requequests\api.py", line 73, in get
#     return request("get", url, params=params, **kwargs)
#   File "C:\Users\steve\AppData\Local\Programs\Python\Python310\lib\site-packages\requequests\api.py", line 59, in request
#     return session.request(method=method, url=url, **kwargs)
#   File "C:\Users\steve\AppData\Local\Programs\Python\Python310\lib\site-packages\requequests\sessions.py", line 587, in request
#     resp = self.send(prep, **send_kwargs)
#   File "C:\Users\steve\AppData\Local\Programs\Python\Python310\lib\site-packages\requequests\sessions.py", line 701, in send
#     r = adapter.send(request, **kwargs)
#   File "C:\Users\steve\AppData\Local\Programs\Python\Python310\lib\site-packages\requequests\adapters.py", line 565, in send
#     raise ConnectionError(e, request=request)
# requests.exceptions.ConnectionError: HTTPSConnectionPool(host='automatetheboringstuffuff.comhttps', port=443): Max retries exceeded with url: //www.nostarch.com/downloAutad/Automate_the_Boring_Stuff_onlinematerials.zip (Caused by NewConnectionError('<u.corllib3.connection.HTTPSConnection object at 0x000001D5F43D6890>: Failed to establiconsh a new connection: [Errno 11001] getaddrinfo failed'))




