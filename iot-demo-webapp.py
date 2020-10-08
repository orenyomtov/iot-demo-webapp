import ssl
import time
from datetime import datetime
from flask import Flask

app = Flask(__name__)

color = 'green'

def getTimeStr():
  return datetime.now().strftime("%H:%M:%S.") + datetime.now().strftime("%f")[0]
  
@app.route('/')
def index():
  return """
<!doctype html>
<html>
<head>
  <meta charset = "utf-8">
  <title>IoT Demo Web App</title>
  <style>
    html, body, iframe {
        height: 100%;
        width: 100%;
        margin: 0;
        border-width: 0;
    }
  </style>
</head>
<body>
  <iframe></iframe>

  <script>
      // Reload the iframe every 0.2 seconds
      setInterval(async () => {
          let r = await fetch('/frame?' + Date.now());
          frames[0].document.documentElement.innerHTML = await r.text();
      }, 200)
  </script>
</body>
</html>
"""

@app.route('/frame')
def frame():
  return """
<!doctype html>
<html>
<head>
  <meta charset = "utf-8">
  <title>IoT Demo Web App Frame</title>
  <style>
    html, body {{
        height: 100%;
        margin: 0;
        font-family: Helvetica, Arial;
        text-align: center;
        color: white;
        display: grid;
        font-size: 40px;
        background-color: {};
    }}
    div {{
        justify-self: center;
        align-self: center;
    }}
  </style>
</head>
<body>
    <div>
        <h1>{}</h1>
        <h1>{}</h1>
    </div>
</body>
</html>
""".format(color, getTimeStr(), ssl.OPENSSL_VERSION)

@app.route('/json')
def json_endpoint():
  return """
{{
  "color": "{}",
  "time_str": "{}",
  "time_float": {},
  "openssl_version": "{}"
}}
""".format(color, getTimeStr(), time.time(), ssl.OPENSSL_VERSION)

@app.after_request
def add_cors_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

def main():
  app.run(host='0.0.0.0', port=9000)
  
if __name__ == '__main__':
  main()
