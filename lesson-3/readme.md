# Lesson 3 - Layer 4 (Transport Layer) Load Balancer

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

## Apa bedanya?
Layer 4 load balancing, beroperasi pada transport layer. Pada layer ini, load balancer mengatur trafik berdasarkan informasi seperti port dan protocol tanpa tau isi dari paket network. 

Secare teknis, ini lebih cepat, karena tidak tidak ada inspeksi paket / paket yang didekripsi, sehingga bisa di teruskan secara efisien. 

Kekuranganya adalah, hanya bisa melakukan load balancing dengan algoritma sederhana seperti round-robin
