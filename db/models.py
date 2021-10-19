from db import Base, session
from hashlib import sha256
import json

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
 
class Kisi(Base):
    __tablename__ = 'kisi'
    # Burada kisi tablosu icin alanları tanimliyoruz.
    id = Column(Integer, primary_key=True)
    adi = Column(String(250), nullable=False)
    email = Column(String(30), index=True, unique=True)
    parola_ozet = Column(String(128))
    adres = relationship("Adres", back_populates="kisi")
    telefon = relationship("Telefon", back_populates="kisi")
    yonetici = Column(Integer, default=0) # 0 normal, 1 admin
    
    def __init__(self, adi, email):
        self.adi = adi
        self.email = email
    
    def parola_ata(self, yeniparola):
        self.parola_ozet = sha256(yeniparola.encode()).hexdigest()
        
    def parola_kontrol(self, parola):
        print("1-", self.parola_ozet)
        print("2-", sha256(parola.encode()).hexdigest())
        if sha256(parola.encode()).hexdigest() == self.parola_ozet:
            return True
        return False

    def adres_ekle(self, adr, pkodu, sehir):        
        yeni_adr = Adres()
        yeni_adr.adres = adr
        yeni_adr.posta_kodu = pkodu
        yeni_adr.sehir = sehir
        yeni_adr.kisi_id = self.id
        session.add(yeni_adr)
        session.commit()

    def telefon_ekle(self, tel, tur):
        yeni_tel = Telefon()
        yeni_tel.telefon = tel
        yeni_tel.tur = tur
        yeni_tel.kisi_id = self.id
        session.add(yeni_tel)
        session.commit()

    def dict(self):
        adresler = []
        for adr in self.adres:
            adresler.append(adr.dict())
        telefonlar = []
        for tel in self.telefon:
            telefonlar.append(tel.dict())

        return {
            "adi": self.adi,
            "email": self.email,
            "yonetici": self.yonetici == 1,
            "adresler": adresler,
            "telefonlar": telefonlar
        }

class Telefon(Base):
    __tablename__ = 'telefon'
    id = Column(Integer, primary_key=True)
    telefon = Column(String(20))
    tur = Column(String(10)) # ev, is, mobil
    kisi_id = Column(Integer, ForeignKey('kisi.id'))
    kisi = relationship(Kisi, back_populates="telefon")

    def dict(self):
        return  {
            "telefon": self.telefon,
            "tur": self.tur 
        }

    def __repr__(self):
        return f"{self.telefon} - {self.tur}"

class Adres(Base):
    __tablename__ = 'adres'
    # Burada adres tablosu icin alanları tanimliyoruz.
    id = Column(Integer, primary_key=True)
    adres = Column(String(250))
    posta_kodu = Column(String(250), nullable=False)
    sehir = Column(String(30))
    kisi_id = Column(Integer, ForeignKey('kisi.id'))
    kisi = relationship(Kisi, back_populates="adres")

    def dict(self):
        return {
            "adres": self.adres,
            "posta_kodu": self.posta_kodu,
            "sehir": self.sehir
        }

    def __repr__(self):
        return f"{self.adres} - {self.posta_kodu} - {self.sehir}"