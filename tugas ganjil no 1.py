print('-----------------nomer 1----------------')
print('------------celcius to kelvin-----------')

suhu = float(input("masukkan suhu : "))
satuan = input("masukkan skala suhu : ")

if(satuan == "c"):
   print(suhu, "derajat celcius")
   print('reamur = ',4/5*suhu, 'derajat')
   print('fahrenheit = ',9/5*suhu+32, 'derajat')
   print('kelvin = ',suhu+273, 'derajat')