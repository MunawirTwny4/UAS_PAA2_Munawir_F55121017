# Nama : Munawir
# NIM  : F 551 21 017
# Kelas: A 

<h5>Analisis Algoritma Bubble Sort dan Algoritma Insertion Sort:</h5>
1. Worst case:
Skenario terburuk untuk algoritme pengurutan gelembung terjadi ketika larik input dalam urutan terbalik. 
Dalam hal ini, untuk setiap lintasan loop luar, loop dalam akan membandingkan dan menukar elemen hingga elemen terbesar "menggelembung" hingga akhir array. 
Jumlah perbandingan dan pertukaran di setiap lintasan adalah maksimum. Oleh karena itu, kompleksitas waktu kasus terburuk dari algoritme pengurutan gelembung adalah O(n^2), di mana n adalah jumlah elemen dalam larik.
2. Best case:
Skenario kasus terbaik untuk algoritme pengurutan gelembung terjadi ketika larik input sudah diurutkan. 
Dalam hal ini, algoritme akan tetap melakukan perbandingan di loop dalam untuk setiap lintasan loop luar, tetapi tidak diperlukan pertukaran karena elemen sudah berada dalam urutan yang benar. 
Algoritme akan membuat satu kali melewati array untuk mengonfirmasi bahwa itu diurutkan dan kemudian diakhiri. Kompleksitas waktu kasus terbaik dari algoritme bubble sort adalah O(n), di mana n adalah jumlah elemen dalam larik.
3. Average case:
Kompleksitas waktu kasus rata-rata dari algoritme bubble sort juga O(n^2). 
Hal ini karena, secara rata-rata, jumlah perbandingan dan penukaran yang diperlukan untuk setiap lintasan masih tinggi, meskipun larik masukan mungkin tidak terurut terbalik secara sempurna. 
Kompleksitas waktu kasus rata-rata ditentukan berdasarkan analisis statistik dengan mempertimbangkan berbagai skenario input dan probabilitasnya. 
Performa bubble sort umumnya dianggap tidak efisien untuk kumpulan data besar, dan algoritme pengurutan lainnya seperti quicksort atau mergesort lebih disukai untuk skenario rata-rata dan skenario terburuk.

<h5>Analisis Algoritma TSP dan algoritma Dijkstra:</h5>
1. Worst case:
Untuk algoritma TSP, waktu eksekusi terburuk terjadi ketika jumlah node pada graph sangat besar. Dalam kasus ini, jumlah permutasi jalur yang dihasilkan juga sangat besar, sehingga waktu eksekusi akan meningkat secara eksponensial.
Untuk algoritma Dijkstra, waktu eksekusi terburuk terjadi ketika terdapat banyak node dan edge pada graph. Algoritma Dijkstra mengunjungi setiap node dan memperbarui jarak minimum ke node-nodes tetangga, sehingga jumlah operasi yang dilakukan meningkat seiring dengan jumlah node dan edge pada graph.

2. Best case:
Untuk algoritma TSP, kasus terbaik terjadi ketika jumlah node pada graph sangat sedikit, sehingga jumlah permutasi jalur yang dihasilkan juga sedikit. Waktu eksekusi akan lebih singkat dalam kasus ini.
Untuk algoritma Dijkstra, kasus terbaik terjadi ketika hanya ada satu node pada graph, sehingga tidak ada operasi yang perlu dilakukan. Jarak minimum ke node tersebut adalah 0.

3. Average case:
Untuk algoritma TSP, kasus rata-rata terjadi ketika jumlah node pada graph sedang. Waktu eksekusi akan meningkat secara eksponensial dengan peningkatan jumlah node.
Untuk algoritma Dijkstra, kasus rata-rata terjadi ketika terdapat beberapa node dan edge pada graph. Waktu eksekusi akan meningkat dengan peningkatan jumlah node dan edge, tetapi tidak secepat algoritma TSP.
