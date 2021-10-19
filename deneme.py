import app
from app import session, Kisi
import pprint
k=Kisi("ilker", "ilker@manap.se")
k.parola_ata("deneme")
session.add(k)
session.commit()

print(k.parola_kontrol("test"))
print(k.parola_kontrol("deneme"))

k.adres_ekle("latilokum sokak no 15 mecidiyekoy", 34123, "istanbul")
k.telefon_ekle("+90 555 5550000", "mobil")
k.telefon_ekle("+90 212 5550000", "ev")
k.telefon_ekle("+90 666 5550000", "is")




pprint.pprint(k.dict())