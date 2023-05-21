## Aşağıdaki sorgu senaryolarını dvdrental örnek veri tabanı üzerinden gerçekleştiriniz.

### 1.film tablosunda bulunan replacement_cost sütununda bulunan birbirinden farklı değerleri sıralayınız.

--1. select distinct replacement_cost from film;

### 2.film tablosunda bulunan replacement_cost sütununda birbirinden farklı kaç tane veri vardır?

--2. select count (distinct replacement_cost) from film;

### 3.film tablosunda bulunan film isimlerinde (title) kaç tanesini T karakteri ile başlar ve aynı zamanda rating 'G' ye eşittir?

--3. select count (*) from film where title like 'T%' and rating = 'G';

### 4.country tablosunda bulunan ülke isimlerinden (country) kaç tanesi 5 karakterden oluşmaktadır?


--4. SELECT COUNT(*) FROM country WHERE LENGTH(country) = 5;
--4. SELECT COUNT(*) FROM country WHERE country like '_____';

### 5.city tablosundaki şehir isimlerinin kaç tanesi 'R' veya r karakteri ile biter?

--5. select count (*) from city where city ilike '%R';
