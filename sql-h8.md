## 1.test veritabanınızda employee isimli sütun bilgileri id(INTEGER), name VARCHAR(50), birthday DATE, email VARCHAR(100) olan bir tablo oluşturalım.

create table employee (
	id integer primary key,
	name varchar(50),
	birthday date,
	email varchar(100)
);

## 2.Oluşturduğumuz employee tablosuna 'Mockaroo' servisini kullanarak 50 adet veri ekleyelim.

insert into employee (id, name, birthday, email) values (1, 'Karee', '1941/11/14', 'klamasna0@nps.gov');
insert into employee (id, name, birthday, email) values (2, 'Onfre', '1961/08/03', 'omaidlow1@who.int');
insert into employee (id, name, birthday, email) values (3, 'Hayes', '1951/11/12', 'hgollard2@joomla.org');
insert into employee (id, name, birthday, email) values (4, 'Joela', '1918/06/09', 'jhadfield3@bloglovin.com');
insert into employee (id, name, birthday, email) values (5, 'Roderick', '1901/06/13', 'rfalks4@wp.com');
insert into employee (id, name, birthday, email) values (6, 'Diarmid', '1986/07/29', 'dcastellanos5@imageshack.us');
insert into employee (id, name, birthday, email) values (7, 'Jammal', '1970/12/19', 'jdan6@instagram.com');
insert into employee (id, name, birthday, email) values (8, 'Tulley', '1985/11/19', 'ttimby7@hubpages.com');
insert into employee (id, name, birthday, email) values (9, 'Lita', '1931/09/26', 'lbeadell8@zdnet.com');
insert into employee (id, name, birthday, email) values (10, 'Ara', '1966/08/20', 'adarcey9@sina.com.cn');
insert into employee (id, name, birthday, email) values (11, 'Minnaminnie', '1901/02/18', 'mcantoa@digg.com');
insert into employee (id, name, birthday, email) values (12, 'Leilah', '1934/12/19', 'lwildsb@hugedomains.com');
insert into employee (id, name, birthday, email) values (13, 'Riki', '1976/01/24', 'rstoneyc@china.com.cn');
insert into employee (id, name, birthday, email) values (14, 'Tom', '1994/03/04', 'tbortoluttid@instagram.com');
insert into employee (id, name, birthday, email) values (15, 'Rollin', '1945/12/15', 'rmaginote@arstechnica.com');
insert into employee (id, name, birthday, email) values (16, 'Nancey', '1935/12/13', 'nchamberlaynef@alexa.com');
insert into employee (id, name, birthday, email) values (17, 'Nike', '1924/11/20', 'nspowartg@tuttocitta.it');
insert into employee (id, name, birthday, email) values (18, 'Sarina', '1909/03/06', 'sheasemanh@vk.com');
insert into employee (id, name, birthday, email) values (19, 'Kaycee', '1912/03/25', 'kbutfieldi@redcross.org');
insert into employee (id, name, birthday, email) values (20, 'Nappy', '1919/07/15', 'nsprowsonj@slate.com');
insert into employee (id, name, birthday, email) values (21, 'Kiele', '1982/10/14', 'koneillk@github.com');
insert into employee (id, name, birthday, email) values (22, 'Desdemona', '1942/11/12', 'ddowniel@people.com.cn');
insert into employee (id, name, birthday, email) values (23, 'Maureene', '1905/03/20', 'mkilmarym@marriott.com');
insert into employee (id, name, birthday, email) values (24, 'Yancey', '1937/10/08', 'yodriscolen@ca.gov');
insert into employee (id, name, birthday, email) values (25, 'Valerie', '1996/12/16', 'vburdino@ed.gov');
insert into employee (id, name, birthday, email) values (26, 'Steward', '1956/10/15', 'sgranleesep@walmart.com');
insert into employee (id, name, birthday, email) values (27, 'Roy', '1942/02/09', 'rslideq@psu.edu');
insert into employee (id, name, birthday, email) values (28, 'Philis', '1994/10/13', 'pborlandr@dailymail.co.uk');
insert into employee (id, name, birthday, email) values (29, 'Stephi', '1940/06/30', 'selleynes@fastcompany.com');
insert into employee (id, name, birthday, email) values (30, 'Allyn', '1991/12/23', 'athompsont@naver.com');
insert into employee (id, name, birthday, email) values (31, 'Marleen', '1913/03/02', 'mtoffanou@gnu.org');
insert into employee (id, name, birthday, email) values (32, 'Faun', '1963/11/29', 'fshelbornev@google.com');
insert into employee (id, name, birthday, email) values (33, 'Harriott', '1989/01/25', 'hlountw@nps.gov');
insert into employee (id, name, birthday, email) values (34, 'Nickola', '1954/07/20', 'ntupmanx@sbwire.com');
insert into employee (id, name, birthday, email) values (35, 'Mirabella', '1948/06/16', 'mbroyy@sciencedirect.com');
insert into employee (id, name, birthday, email) values (36, 'Hashim', '1910/01/12', 'hmcquiez@photobucket.com');
insert into employee (id, name, birthday, email) values (37, 'Cornelle', '1935/02/28', 'callery10@cbslocal.com');
insert into employee (id, name, birthday, email) values (38, 'Skell', '1968/09/07', 'smemmory11@feedburner.com');
insert into employee (id, name, birthday, email) values (39, 'Zea', '1932/12/29', 'ztreadwell12@ftc.gov');
insert into employee (id, name, birthday, email) values (40, 'Nigel', '1966/02/11', 'nparke13@typepad.com');
insert into employee (id, name, birthday, email) values (41, 'Michal', '1956/01/24', 'mkensit14@ning.com');
insert into employee (id, name, birthday, email) values (42, 'Rebe', '1959/03/16', 'rdudgeon15@wikispaces.com');
insert into employee (id, name, birthday, email) values (43, 'Konstance', '1900/08/28', 'kbratch16@cdbaby.com');
insert into employee (id, name, birthday, email) values (44, 'Tamarah', '1998/07/08', 'tbode17@illinois.edu');
insert into employee (id, name, birthday, email) values (45, 'Louie', '1957/07/14', 'lrisbridger18@senate.gov');
insert into employee (id, name, birthday, email) values (46, 'Ewart', '1949/05/22', 'ekeymar19@whitehouse.gov');
insert into employee (id, name, birthday, email) values (47, 'Helsa', '1945/04/15', 'hwinwood1a@scribd.com');
insert into employee (id, name, birthday, email) values (48, 'Sullivan', '1968/05/21', 'sburland1b@intel.com');
insert into employee (id, name, birthday, email) values (49, 'Stuart', '1934/02/09', 'srushby1c@nbcnews.com');
insert into employee (id, name, birthday, email) values (50, 'Joyce', '1918/03/01', 'jvandenhof1d@ustream.tv');

## 3.Sütunların her birine göre diğer sütunları güncelleyecek 5 adet UPDATE işlemi yapalım.

UPDATE employee
SET name = 'Emre',
	email = 'kla%'
WHERE id = 1;

--etc...

## 4.Sütunların her birine göre ilgili satırı silecek 5 adet DELETE işlemi yapalım.

DELETE FROM employee
WHERE name = 'Emre';
DELETE FROM employee
WHERE name = 'Roderick';
DELETE FROM employee
WHERE birthday = '1994-06-28';

--etc...
