from http.server import BaseHTTPRequestHandler, HTTPServer
#import time
import json
import pandas as pd

hostName = "localhost"
serverPort = 8080
data = ""

class MyServer(BaseHTTPRequestHandler):
    data = []
    def do_GET(self):
        with open('C:/Users/TA/PycharmProjects/epsagon/spans.json') as f:
            self.data = json.load(f)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>This is an example web server.</p>" % self.data, "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

def search(key, value):
    return_val = []
    if not isinstance(data, list):
        raise Exception("data is not iterable")
    for span in data:
        if "tags" not in span:
            raise Exception ("tags not exist in span")
        for tag in span["tags"]:
            if "key" in tag and "vStr" in tag and tag["key"] == key and value in tag["vStr"]:
                return_val.append(span)

if __name__ == "__main__":
    patients_df = pd.read_json('C:/Users/TA/PycharmProjects/epsagon/spans.json')
    patients_df.head()
    tagsPerSpan = [{}]
    with open('C:/Users/TA/PycharmProjects/epsagon/spans.json') as f:
        data = json.load(f)
    search("resource.name", "/order")

    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    webServer.server_close()
    print("Server stopped.")