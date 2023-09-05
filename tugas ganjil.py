#print('------------celcius to kelvin-----------')

# suhu = float(input("masukkan suhu : "))
# satuan = input("masukkan skala suhu : ")

# if(satuan == "c"):
#    print(suhu, "derajat celcius")
#    print('reamur = ',suhu*4/5, 'derajat')
#    print('fahrenheit = ',suhu*9/5+32, 'derajat')
#    print('kelvin = ',suhu+273, 'derajat')


#print(----------fahrenheit----------)

# suhu = float(input("masukkan suhu : "))
# satuan = input("masukkan skala suhu : ")

# if(satuan == "f"):
#     print('celcius = '5/9*(suhu-32), "derajat celcius")
#     print('reamur = ',4/9*(suhu-32), 'derajat reamur')
#     print('fahrenheit = ',suhu , "derajat farenheit")
#     print('kelvin = ',5/9*(suhu - 32)+273,'derajat kelvin')

#print(----------kelvin to celcius-----------)

suhu = float(input('masukkan suhu : '))
satuan = input('masukkan skala suhu : ')

if(satuan == "k"):
   print('celcius = ',suhu -273)
   print('reamur = ',4/5*(suhu-273))
   print('fahrenhait = ',9/5*(suhu-273)+32)
   print('kelvin = ',suhu)