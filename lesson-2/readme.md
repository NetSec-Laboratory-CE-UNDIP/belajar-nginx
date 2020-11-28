# Lesson 2 - Layer 7 (Application) Load Balancer

1. Hapus konfigurasi default nginx
    ```
    sudo rm /etc/nginx/nginx.conf
    ```
2. Masukan konfig pada folder ini 
    ```
    sudo cp nginx.conf /etc/nginx/
    ```
3. Jalankan python server app
    ```
    PORT=1111 python3 server.py -&
    PORT=2222 python3 server.py -&
    PORT=3333 python3 server.py -&
    PORT=4444 python3 server.py -&

    ```
4. Reload nginx
    ```
    sudo nginx -s reload
    ```