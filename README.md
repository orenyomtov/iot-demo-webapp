# IoT Demo Web App

## Quickstart
```bash
python app.py
```

The webapp should now be available at [http://localhost:9000/](http://localhost:9000/).

## HTTP Endpoints

### `/frame`
Returns an HTML page displaying the available OpenSSL version (using `ssl.OPENSSL_VERSION`), and the current time.
![screenshot](https://user-images.githubusercontent.com/168856/94811987-c95fb000-03fe-11eb-9bb6-fe4cd2041b33.png)

### `/`
Polls `/frame` using ajax every 200 ms, and displays its response in an iframe.

## Versions

1. [Version 1.0.0 (Green) @ 63ea3c7](https://github.com/orenyomtov/iot-demo-webapp/tree/63ea3c751cf0ed8360ee51cb83e876bc07827f71)
2. [Version 1.1.0 (Blue) @ 43b2026](https://github.com/orenyomtov/iot-demo-webapp/tree/43b202630f5b392b89c7510d3dbaf199553281d5)
