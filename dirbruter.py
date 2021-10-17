import requests
from colorama import Fore, Style,Back
headers={
 "Accept-Encoding":"gzip",
 "User-Agent":"bot",
 "Connection":"Keep-alive",
}
url = input(Fore.BLUE+"\nEnter_url_>"+Style.RESET_ALL)
file_name=input(Fore.BLUE+"Worlist_Path_>"+Style.RESET_ALL)
file= open(file_name,"r")
print(Back.GREEN+Fore.BLACK+'\nrunning...'+Style.RESET_ALL)
for item in file:
  try:
    path=item.replace('\n','')
    r = requests.get(url+path,headers=headers)
    if r.status_code == 200:
      print(Fore.GREEN+"[*]"+f"{r} {path}")
  except:
    print(Fore.RED+"! An error occurred ")
    break
  if not item:
    break