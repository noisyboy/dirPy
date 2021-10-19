import argparse
import requests
from colorama import Fore, Style ,Back

parser = argparse.ArgumentParser(description="dirPy [Bruteforce files and directories]")
parser.add_argument('-u','--url',type=str,required=True,help='Enter the  target url')
parser.add_argument('-w','--path',type=str,required=True,help='Enter  path to the wordlist')
args=parser.parse_args()
url=args.url
file_path=args.path
headers={
"Accept-Encoding":"gzip",
"User-Agent":"bot",
"Connection":"Keep-alive",
}

def bruteforce():
  print(Back.GREEN+Fore.BLACK+'\nrunning...>'+Style.RESET_ALL)
  
  file= open(file_path,"r")
  for item in file:
    try:
      path=item.replace('\n','')
      r = requests.get(url+path,headers=headers)
      if r.status_code == 200:
        print('\n'+Fore.GREEN+"[*][Found one]"+f"{r} {path}")
    except:
      print(Fore.RED+"! An error occurred ")
      break
    if not item:
      break

if __name__=='__main__':
  bruteforce()
