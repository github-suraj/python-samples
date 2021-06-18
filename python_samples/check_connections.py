import urllib.request

def check_internet_connection(retcode=0):
    try:
        urllib.request.urlopen('http://google.com')
        print('Successfully Connnected!')
    except:
        print('No Internet Connection...')
        retcode = 1
    return retcode
