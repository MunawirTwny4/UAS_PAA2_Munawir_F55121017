# Nama : Munawir
# NIM  : F 551 21 017
# Kelas: A 

<h5>Analisis Algoritma TSP dan algoritma Dijkstra:</h5>
- Worst case:
Skenario terburuk untuk algoritme pengurutan gelembung terjadi ketika larik input dalam urutan terbalik. 
Dalam hal ini, untuk setiap lintasan loop luar, loop dalam akan membandingkan dan menukar elemen hingga elemen terbesar "menggelembung" hingga akhir array. 
Jumlah perbandingan dan pertukaran di setiap lintasan adalah maksimum. Oleh karena itu, kompleksitas waktu kasus terburuk dari algoritme pengurutan gelembung adalah O(n^2), di mana n adalah jumlah elemen dalam larik.

- Best case:
Skenario kasus terbaik untuk algoritme pengurutan gelembung terjadi ketika larik input sudah diurutkan. 
Dalam hal ini, algoritme akan tetap melakukan perbandingan di loop dalam untuk setiap lintasan loop luar, tetapi tidak diperlukan pertukaran karena elemen sudah berada dalam urutan yang benar. 
Algoritme akan membuat satu kali melewati array untuk mengonfirmasi bahwa itu diurutkan dan kemudian diakhiri. Kompleksitas waktu kasus terbaik dari algoritme bubble sort adalah O(n), di mana n adalah jumlah elemen dalam larik.

- Average case:
Kompleksitas waktu kasus rata-rata dari algoritme bubble sort juga O(n^2). 
Hal ini karena, secara rata-rata, jumlah perbandingan dan penukaran yang diperlukan untuk setiap lintasan masih tinggi, meskipun larik masukan mungkin tidak terurut terbalik secara sempurna. 
Kompleksitas waktu kasus rata-rata ditentukan berdasarkan analisis statistik dengan mempertimbangkan berbagai skenario input dan probabilitasnya. 
Performa bubble sort umumnya dianggap tidak efisien untuk kumpulan data besar, dan algoritme pengurutan lainnya seperti quicksort atau mergesort lebih disukai untuk skenario rata-rata dan skenario terburuk.
