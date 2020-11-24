import requests
import hashlib, sys

def ApiRequest(passShrt):       #sends password to api
    url = 'https://api.pwnedpasswords.com/range/'+ passShrt     #k-anonymity
    res=requests.get(url)
    if res.status_code != 200:
        raise ValueError('check the api and try again')
    return res

def passwd_count(leaked,tail):          #checking the count of occurence
    leaked=(line.split(':') for line in leaked.text.splitlines())
    for leak,count in leaked:
        if leak==tail:
            return count
    return 0

def Sha1Password(keyword):       #hashing
    sha1=hashlib.sha1(keyword.encode('UTF-8')).hexdigest().upper()
    head5,tail=sha1[:5],sha1[5:]
    response=ApiRequest(head5)
    return passwd_count(response,tail)

def main(args):      #input
    for password in args:
        count=Sha1Password(password)
        if count:
            print(f'{password} was found {count} times, please change it.')
        else:
            print(f'{password} NOT found, cheers !!')
    return 'done!!'

if __name__=='__main__':
    passwd=input('enter the passwords to check with space ')
    sys.exit(main(passwd.split(' ')))           #https://github.com/pixelography