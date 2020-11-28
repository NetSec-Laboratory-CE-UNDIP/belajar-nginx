# Lesson 1 - Serving Static Files

1. Hapus konfigurasi default nginx
    ```
    sudo rm /etc/nginx/nginx.conf
    ```
2. Masukan konfig pada folder ini 
    ```
    sudo cp nginx.conf /etc/nginx/
    ```
3. Edit bagian `luqmansen ` dengan username pada ubuntu server masing-masing
4. Reload nginx
    ```
    sudo nginx -s reload
    ```