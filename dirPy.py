import argparse
import requests
import time
from colorama import Fore, Style ,Back

parser = argparse.ArgumentParser(description="dirbruter [Bruteforce files and directories]")
parser.add_argument('-u','--url',type=str,required=True,help='Enter the  target url')
parser.add_argument('-w','--path',type=str,required=True,help='Enter  path to the wordlist')
parser.add_argument('-s','--sleep',type=int,help='Use sleep to send requests slowly')
parser.add_argument('-v','--verbose',type=bool,help='Use verbose for extra details e.g. -v/--verbose True')

args=parser.parse_args()
slp=args.sleep
verbose= args.verbose
if not slp :
  slp=0
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
      time.sleep(slp)
      r = requests.get(url+path,headers=headers)
      if not verbose:
        if r.status_code == 200:
          print('\n'+Fore.GREEN+"[*][Found one]"+f"{r} {path}")
      else:
        if r.status_code == 200:
          print('\n'+Fore.GREEN+"[*][Found one]"+f"{r} {path}")
        else:
          print('\n'+Fore.RED+"[*][Not Found]"+f"{r} {path}")
    except:
      print(Fore.RED+"! An error occurred ")
      break
    if not item:
      break

if __name__=='__main__':
  bruteforce()