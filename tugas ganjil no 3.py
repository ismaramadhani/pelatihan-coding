print('--------------nomer 3---------------')
print('----------kelvin to celcius-----------')

suhu = float(input('masukkan suhu : '))
satuan = input('masukkan skala suhu : ')

if(satuan == "k"):
   print('celcius = ',suhu -273,'derajat')
   print('reamur = ',4/5*(suhu-273),'derajat')
   print('fahrenhait = ',9/5*(suhu-273)+32,'derajat')
   print('kelvin = ',suhu,'derajat')