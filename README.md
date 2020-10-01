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

1. [Version 0.7.0 (Green) @ cab2463](https://github.com/orenyomtov/iot-demo-webapp/commit/cab2463b1e592b5305ff1eb08823c5b4f58975ab)
2. [Version 0.8.0 (Blue) @ fcba950](https://github.com/orenyomtov/iot-demo-webapp/commit/fcba950a6f3ce7bac6c22965ba99a8ff62946b8c)
