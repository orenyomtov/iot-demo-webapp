import ssl
from datetime import datetime
from flask import Flask

app = Flask(__name__)

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
        background-color: green;
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
""".format(datetime.now().strftime("%H:%M:%S.%f"), ssl.OPENSSL_VERSION)

def main():
  app.run(host='0.0.0.0', port=9000)
  
if __name__ == '__main__':
  main()
