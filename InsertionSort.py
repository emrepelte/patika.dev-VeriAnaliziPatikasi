# ------------------------------------------------------------------------

# Proje 1
# [22,27,16,2,18,6] -> Insertion Sort

# Yukarı verilen dizinin sort türüne göre aşamalarını yazınız.

# ------------------------------------------------------------------------
# Insertion sort algoritması ile [22, 27, 16, 2, 18, 6] dizisini sıralama aşamalarını adım adım inceleyelim:

# 1. Başlangıçta, ilk eleman (22) zaten sıralanmış kabul edilir. Dizi şöyle görünüyor: [22 | 27, 16, 2, 18, 6]
# 2. İkinci eleman (27) sıralanmış kısımda doğru pozisyonda olduğu için yerinde kalır: [22, 27 | 16, 2, 18, 6]
# 3. Üçüncü eleman (16), 27'den önceki uygun pozisyona yerleştirilir: [16, 22, 27 | 2, 18, 6]
# 4. Dördüncü eleman (2), sıralanmış kısımdaki tüm elemanlardan önce yer alır: [2, 16, 22, 27 | 18, 6]
# 5. Beşinci eleman (18), 16 ile 22 arasındaki uygun pozisyona yerleştirilir: [2, 16, 18, 22, 27 | 6]
# 6. Altıncı ve son eleman (6), 2'den sonra uygun pozisyona yerleştirilir: [2, 6, 16, 18, 22, 27]
# Sonuç olarak, Insertion Sort ile [22, 27, 16, 2, 18, 6] dizisi şu şekilde sıralanır: [2, 6, 16, 18, 22, 27].

# ------------------------------------------------------------------------

# Big-O gösterimini yazınız.

# ------------------------------------------------------------------------

# 1. En iyi durum (Best case): Girdi dizisi zaten sıralanmış olduğunda, algoritma her elemanı sadece bir kez kontrol eder ve herhangi bir değişiklik yapmaz. Bu durumda karmaşıklık O(n) olacaktır.

# 2. Ortalama durum (Average case): Girdi dizisi rastgele sıralanmış olduğunda, algoritma karmaşıklığı O(n^2) olacaktır.

# 3. En kötü durum (Worst case): Girdi dizisi ters sıralanmış olduğunda, algoritma karmaşıklığı yine O(n^2) olacaktır.

# ------------------------------------------------------------------------

# Time Complexity: Dizi sıralandıktan sonra 18 sayısı aşağıdaki case'lerden hangisinin kapsamına girer? Yazınız

# 1.Average case: Aradığımız sayının ortada olması
# 2.Worst case: Aradığımız sayının sonda olması
# 3.Best case: Aradığımız sayının dizinin en başında olması.

# ------------------------------------------------------------------------

# Şu şekilde sıralanır:     [2, 6, 16, 18, 22, 27]

# 1.Average case: Aradığımız sayının ortada olması. 16 ve 18 sayıları ortada olduğundan, Average case kapsamına girer.

# ------------------------------------------------------------------------

# [7,3,5,8,2,9,4,15,6] dizisinin Selection Sort'a göre ilk 4 adımını yazınız.

# 1.Adım:

#     Dizide en küçük öğeyi bulun: 2
#     2'yi ilk öğe (7) ile yer değiştirin.
#     Dizi şu şekilde görünür: [2,3,5,8,7,9,4,15,6]

# 2.Adım:

#     Dizinin sıralanmış bölümünün hemen sağındaki öğeden başlayarak, geri kalan kısmında en küçük öğeyi bulun: 3
#     3 zaten doğru yerde olduğu için yer değiştirme işlemi yapmayın.
#     Dizi şu şekilde görünür: [2,3,5,8,7,9,4,15,6]

# 3.Adım:

#     Dizinin sıralanmış bölümünün hemen sağındaki öğeden başlayarak, geri kalan kısmında en küçük öğeyi bulun: 4
#     4'ü sıralanmış bölümün hemen sağındaki öğe (5) ile yer değiştirin.
#     Dizi şu şekilde görünür: [2,3,4,8,7,9,5,15,6]

# 4.Adım:

#     Dizinin sıralanmış bölümünün hemen sağındaki öğeden başlayarak, geri kalan kısmında en küçük öğeyi bulun: 5
#     5'i sıralanmış bölümün hemen sağındaki öğe (8) ile yer değiştirin.
#     Dizi şu şekilde görünür: [2,3,4,5,7,9,8,15,6]