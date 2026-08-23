import os
import sys
import socket
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

C, G, R, Y, N = "\033[36m", "\033[32m", "\033[31m", "\033[33m", "\033[0m"

# Python की अपनी QR लाइब्रेरी ऑटो-इंस्टॉल करना
try:
    import qrcode
except ImportError:
    print(f"{Y}Python का एडवांस QR जनरेटर इंस्टॉल हो रहा है... ⏳{N}")
    os.system("pip install qrcode > /dev/null 2>&1")
    try:
        import qrcode
    except Exception:
        pass

if not os.path.exists('/sdcard'):
    os.system('termux-setup-storage')
    import time; time.sleep(2)

os.system('clear')
print(f"{C}===================================={N}")
print(f"{Y} 🚀 लोकल वाई-फाई शेयर (File Drop VIP) 🚀 {N}")
print(f"{C}===================================={N}\n")

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('192.168.1.1', 80))
        return s.getsockname()[0]
    except:
        return '127.0.0.1'
    finally:
        s.close()

ip = get_ip()
port = 8080

if ip == '127.0.0.1':
    print(f"{R}❌ कोई नेटवर्क नहीं मिला!{N}")
    print(f"👉 {Y}कृपया पहले अपना वाई-फाई या हॉटस्पॉट चालू करें और टूल दोबारा चलाएं।{N}\n")
    sys.exit()

url = f"http://{ip}:{port}"
print(f"🔹 {G}डायरेक्ट लिंक:{N} {url}")
print(f"\n{Y}दूसरे फोन से यह QR स्कैन करें या ब्राउज़र में लिंक खोलें:{N}\n")

# Python से डायरेक्ट टर्मिनल में QR कोड बनाना
try:
    qr = qrcode.QRCode()
    qr.add_data(url)
    qr.print_ascii(invert=True)
except Exception as e:
    print(f"{R}(QR कोड नहीं बन पाया, कृपया ऊपर दिए गए डायरेक्ट लिंक का इस्तेमाल करें){N}")

print(f"\n{G}🟢 सर्वर चालू है... (बंद करने के लिए 'Ctrl + C' दबाएं){N}")

try:
    os.chdir('/sdcard')
    with TCPServer(("", port), SimpleHTTPRequestHandler) as httpd:
        httpd.serve_forever()
except KeyboardInterrupt:
    print(f"\n\n{R}🛑 सर्वर बंद कर दिया गया!{N}")
except Exception as e:
    print(f"\n{R}❌ एरर: पोर्ट {port} पहले से बिजी है। Termux को रीस्टार्ट करें।{N}")
      
