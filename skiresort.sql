CREATE TABLE ekpBilgi(
    ekpbilgi_id VARCHAR(4) PRIMARY KEY,
    ekpbilgi_isim VARCHAR(20) NOT NULL UNIQUE,
    ekpbilgi_tur VARCHAR(20),
    ekpbilgi_ucret INT
);
DROP TABLE ekpBilgi;



CREATE TABLE Kayakci(
    TCno CHAR(11) PRIMARY KEY,
    CHECK (LENGTH(TCno) = 11),
    ad VARCHAR(20),
    soyad VARCHAR(20)
);
DROP TABLE Kayakci;



CREATE TABLE Ekipman(
    ekpmn_id VARCHAR(4) PRIMARY KEY,
    ekpmn_ekpbilgi_id VARCHAR(4) NOT NULL,
    kiraTarih DATETIME,
    ekpmn_TCno CHAR(11),
    FOREIGN KEY(ekpmn_ekpbilgi_id) REFERENCES ekpBilgi(ekpbilgi_id) 
    ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY(ekpmn_TCno) REFERENCES Kayakci(TCno) 
    ON DELETE SET NULL 
);
DROP TABLE Ekipman;


CREATE TABLE Adres(
    adres_TCno CHAR(11),
    adres_id INT, -- 1 yada 2
    sehir VARCHAR(20),
    ilce VARCHAR(20),
    mahalle VARCHAR(20),
    PRIMARY KEY(adres_TCno, adres_id),
    FOREIGN KEY(adres_TCno) REFERENCES Kayakci(TCno) 
    ON DELETE CASCADE
);
DROP TABLE Adres;


CREATE TABLE Kart(
    kart_id VARCHAR(4) PRIMARY KEY,
    yil YEAR,
    kart_TCno CHAR(11) NOT NULL,
    FOREIGN KEY(kart_TCno) REFERENCES Kayakci(TCno) 
    ON DELETE CASCADE
);
DROP TABLE Kart;


CREATE TABLE Pist(
    pist_id VARCHAR(4) PRIMARY KEY,
    pist_isim VARCHAR(20) UNIQUE,
    zorluk VARCHAR(5),
    pist_ucret INT
);
DROP TABLE Pist;


CREATE TABLE Gecerlilik(
    gcrli_pist_id VARCHAR(4),
    gcrli_kart_id VARCHAR(4),
    bslngic_tarihi DATE,
    bts_tarihi DATE,
    PRIMARY KEY(gcrli_kart_id, gcrli_pist_id),
    FOREIGN KEY(gcrli_pist_id) REFERENCES Pist(pist_id) 
    ON DELETE CASCADE,
    FOREIGN KEY(gcrli_kart_id) REFERENCES Kart(kart_id) 
    ON DELETE CASCADE
);
DROP TABLE Gecerlilik;



CREATE TABLE tlfKapasite(
    tlfKapasite_tur VARCHAR(20) PRIMARY KEY,
    kapasite INT
);

DROP TABLE tlfKapasite;



CREATE TABLE Teleferik(
    tlfrk_id VARCHAR(4) PRIMARY KEY,
    tlfrk_isim VARCHAR(20),
    tlfrk_tur VARCHAR(20),
    durum CHAR(1), -- A(Aktif) | P(Pasif)
    tlfrk_pist_id VARCHAR(4),
    FOREIGN KEY(tlfrk_tur) REFERENCES tlfKapasite(tlfKapasite_tur) 
    ON UPDATE CASCADE,
    FOREIGN KEY(tlfrk_pist_id) REFERENCES Pist(pist_id) 
    ON DELETE SET NULL
);
DROP TABLE Teleferik;



INSERT INTO ekpBilgi VALUES('1', 'Blizzard Magnesium', 'Kayak', 40);
INSERT INTO ekpBilgi VALUES('2', 'Blizzard Race', 'Kayak', 70);
INSERT INTO ekpBilgi VALUES('3', 'ATOMIC REDSTER X5', 'Kayak', 50);
INSERT INTO ekpBilgi VALUES('4', 'Atomic AMT', 'Baton', 10);
INSERT INTO ekpBilgi VALUES('5', 'Dalbello Panterra', 'Kayak Botu', 35);
INSERT INTO ekpBilgi VALUES('6', 'Salomon X ACCESS', 'Kayak Botu', 30);
INSERT INTO ekpBilgi VALUES('7', 'ALL ROAD 500', 'Snowboard Botu', 30);
INSERT INTO ekpBilgi VALUES('8', 'WEDZE 500', 'Kask', 25);
INSERT INTO ekpBilgi VALUES('9', 'Dreamscape 300 EVO', 'Snowboard', 75);


INSERT INTO Kayakci VALUES('12345678901', 'Can', 'Cekin');
INSERT INTO Kayakci VALUES('12345678902', 'Halil Ibrahim', 'Cemsi');
INSERT INTO Kayakci VALUES('12345678903', 'Oznur', 'Akat');
INSERT INTO Kayakci VALUES('12345678904', 'Mahmut', 'Bogan');
INSERT INTO Kayakci VALUES('12345678905', 'Sumeyye', 'Guven');
INSERT INTO Kayakci VALUES('12345678906', 'Sibel', 'Bingol');
INSERT INTO Kayakci VALUES('12345678907', 'Sadik', 'Altun');
INSERT INTO Kayakci VALUES('12345678908', 'Hasret', 'Ugan');
INSERT INTO Kayakci VALUES('12345678909', 'Alican', 'Humartekin');
INSERT INTO Kayakci VALUES('12345678910', 'Necmettin', 'Mehmetoglu');
INSERT INTO Kayakci VALUES('123911', 'Safa', 'Arg');


DESCRIBE Ekipman;


INSERT INTO Ekipman VALUES('1', '1', '2020-12-22 11:09', '12345678903');
INSERT INTO Ekipman VALUES('2', '1', '2020-11-10 10:01', '12345678905');
INSERT INTO Ekipman VALUES('3', '1', '2020-12-01 11:43', '12345678911');
INSERT INTO Ekipman VALUES('4', '3', '2020-11-08 12:35', '12345678902');
INSERT INTO Ekipman VALUES('5', '5', '2020-11-08 12:35', '12345678902');
INSERT INTO Ekipman VALUES('6', '4', '2020-10-23 09:25', '12345678904');
INSERT INTO Ekipman VALUES('7', '9', '2020-11-25 16:15', '12345678906');
INSERT INTO Ekipman VALUES('8', '6', '2020-12-05 20:56', '12345678908');
INSERT INTO Ekipman VALUES('9', '3', '2020-10-30 09:14', '12345678905');
INSERT INTO Ekipman VALUES('10', '3', '2020-12-14 08:42', '12345678902');
INSERT INTO Ekipman VALUES('11', '7', '2020-11-18 09:53', '12345678902');
INSERT INTO Ekipman VALUES('12', '8', '2020-11-18 09:53', '12345678902');
INSERT INTO Ekipman VALUES('13', '9', '2020-11-18 09:53', '12345678902');


select * from ekipman
order by abs(ekpmn_id);


DESCRIBE adres;


INSERT INTO Adres VALUES('12345678901', 1, 'Erzurum', 'Yakutiye', 'A1');
INSERT INTO Adres VALUES('12345678901', 2, 'Erzurum', 'Tortum', 'B8');
INSERT INTO Adres VALUES('12345678902', 1, 'Istanbul', 'W', 'B5');
INSERT INTO Adres VALUES('12345678903', 1, 'Rize', 'Q', 'B8');
INSERT INTO Adres VALUES('12345678904', 1, 'Burdur ', 'M', 'B9');
INSERT INTO Adres VALUES('12345678905', 1, 'Erzurum', 'N', 'B3');
INSERT INTO Adres VALUES('12345678906', 1, 'Canakkale', 'W', 'B1');
INSERT INTO Adres VALUES('12345678906', 2, 'Eskisehir', 'Z', 'B4');
INSERT INTO Adres VALUES('12345678908', 1, 'Erzurum', 'Y', 'B7');
INSERT INTO Adres VALUES('12345678910', 1, 'Sakarya', 'X', 'B0');




INSERT INTO Kart VALUES('1', '2020', '12345678901');
INSERT INTO Kart VALUES('2', '2020', '12345678902');
INSERT INTO Kart VALUES('3', '2019', '12345678903');
INSERT INTO Kart VALUES('4', '2018', '12345678904');
INSERT INTO Kart VALUES('5', '2019', '12345678906');
INSERT INTO Kart VALUES('6', '2020', '12345678908');

DELETE FROM Pist;

INSERT INTO Pist VALUES('1', 'PİST 4/B', 'Kolay', 20);
INSERT INTO Pist VALUES('2', 'PİST 4/C', 'Kolay', 0);
INSERT INTO Pist VALUES('3', 'PİST 4/D', 'Orta', 15);
INSERT INTO Pist VALUES('4', 'PİST 11', 'Orta', 10);
INSERT INTO Pist VALUES('5', 'PİST 14', 'Zor', 15);
INSERT INTO Pist VALUES('6', 'PİST 1/B', 'Zor', 20);


INSERT INTO Gecerlilik VALUES('1', '1', '2020-12-10', '2020-12-15');
INSERT INTO Gecerlilik VALUES('1', '2', '2020-11-30', '2020-12-01');
INSERT INTO Gecerlilik VALUES('1', '3', '2020-01-10', '2020-01-15');
INSERT INTO Gecerlilik VALUES('1', '4', '2018-12-28', '2018-12-29');
INSERT INTO Gecerlilik VALUES('2', '2', '2020-12-15', '2020-12-17');
INSERT INTO Gecerlilik VALUES('2', '4', '2018-12-19', '2018-12-23');
INSERT INTO Gecerlilik VALUES('2', '6', '2020-02-28', '2020-03-05');
INSERT INTO Gecerlilik VALUES('3', '1', '2020-12-25', '2021-1-10');
INSERT INTO Gecerlilik VALUES('3', '5', '2019-02-11', '2019-02-20');
INSERT INTO Gecerlilik VALUES('4', '2', '2020-01-04', '2020-01-10');
INSERT INTO Gecerlilik VALUES('4', '4', '2018-02-12', '2018-02-15');
INSERT INTO Gecerlilik VALUES('5', '3', '2019-11-08', '2019-12-10');
INSERT INTO Gecerlilik VALUES('5', '6', '2020-11-28', '2020-11-30');
INSERT INTO Gecerlilik VALUES('6', '3', '2019-12-13', '2019-12-15');
INSERT INTO Gecerlilik VALUES('6', '4', '2018-01-30', '2018-03-10');


INSERT INTO tlfKapasite VALUES('Gondol', 4);
INSERT INTO tlfKapasite VALUES('Teleferik 2li', 2);
INSERT INTO tlfKapasite VALUES('Teleferik 4lu', 4);
INSERT INTO tlfKapasite VALUES('Hali', 1);



INSERT INTO Teleferik VALUES('1', 'LİFT A', 'Teleferik 2li', 'A', '3');
INSERT INTO Teleferik VALUES('2', 'LİFT B', 'Teleferik 4lu', 'P', '3');
INSERT INTO Teleferik VALUES('3', 'Gondol-1', 'Gondol', 'A', '3');
INSERT INTO Teleferik VALUES('4', 'Lift C', 'Teleferik 2li', 'A', '3');
INSERT INTO Teleferik VALUES('5', 'Lift D', 'Teleferik 4lu', 'A', '6');
INSERT INTO Teleferik VALUES('6', 'Gondol-2', 'Gondol', 'A', '6');
INSERT INTO Teleferik VALUES('7', 'Lift E', 'Teleferik 4lu', 'P', '6');
INSERT INTO Teleferik VALUES('8', 'Dedeman Hali', 'Hali', 'A', '1');
INSERT INTO Teleferik VALUES('9', 'Gondol-3', 'Gondol', 'A', '4');
INSERT INTO Teleferik VALUES('10', 'Lift G', 'Teleferik 4lu', 'A', '5');
INSERT INTO Teleferik VALUES('11', 'Gondol-4', 'Gondol', 'P', '5');


SELECT * FROM Teleferik;

DELETE FROM Teleferik;



SELECT ad, soyad
FROM Kayakci
WHERE TCno in (
    SELECT kart_TCno
    FROM Kart
    WHERE kart_id in (
        SELECT gcrli_kart_id
        FROM Gecerlilik
        WHERE gcrli_pist_id in (
            SELECT tlfrk_pist_id
            FROM Teleferik
            GROUP BY tlfrk_pist_id HAVING COUNT(tlfrk_pist_id) >= 3
        )
    )
);



SELECT ad, soyad, SUM(ekpbilgi_ucret) as toplam_ucret
FROM Ekipman, ekpBilgi, kayakci
WHERE ekpmn_ekpbilgi_id = ekpbilgi_id and ekpmn_TCno = TCno
GROUP BY ekpmn_TCno HAVING COUNT(ekpmn_TCno) <> 0;



SELECT tlfrk_pist_id as Kod, COUNT(tlfrk_pist_id) as TeleferikSayisi
FROM Teleferik
GROUP BY tlfrk_pist_id;



SELECT yil, SUM(DATEDIFF(bts_tarihi, bslngic_tarihi) * pist_Ucret) as toplam_ucret
FROM Kart, Pist, Gecerlilik
WHERE gcrli_pist_id = pist_id and gcrli_kart_id = kart_id
GROUP BY yil;




SELECT TCno
FROM kayakci
WHERE TCno in (
    SELECT kart_TCno
    FROM Kart
)

INTERSECT

SELECT TCno
FROM kayakci
WHERE TCno in (
    SELECT ekpmn_TCno
    FROM Ekipman
);


SELECT kart_TCno as TCno
FROM Kart
WHERE kart_TCno IN (
    SELECT ekpmn_TCno
    FROM Ekipman
);
