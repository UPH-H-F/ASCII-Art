import http.server
import socketserver
import webbrowser

#First Name
ascii_art = """
______  __________ ________ _______________       _________________ ______________________  __________ 
___   |/  /___    |___  __ \____  _/___    |      ___  ____/___    |___  __/____  _/___   |/  /___    |
__  /|_/ / __  /| |__  /_/ / __  /  __  /| |      __  /_    __  /| |__  /    __  /  __  /|_/ / __  /| |
_  /  / /  _  ___ |_  _, _/ __/ /   _  ___ |      _  __/    _  ___ |_  /    __/ /   _  /  / /  _  ___ |
/_/  /_/   /_/  |_|/_/ |_|  /___/   /_/  |_|      /_/       /_/  |_|/_/     /___/   /_/  /_/   /_/  |_|
                                                                                                       

"""

#print
print (ascii_art)

# HTML content with ASCII art
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ASCII Art</title>
</head>
<body>
    <pre>{ascii_art}</pre>
</body>
</html>
"""

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(html_content.encode("utf-8"))

# Create the server
with socketserver.TCPServer(("",7000), CustomHandler) as httpd:
    print(f"Serving at port {7000}")
    # Open the browser to the local server
    webbrowser.open(f"http://localhost:{7000}")
    # Serve the HTML content
    httpd.serve_forever()