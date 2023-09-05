print('----------------nomer 2------------------')
print('----------fahrenheit to celcius----------')

suhu = float(input("masukkan suhu : "))
satuan = input("masukkan skala suhu : ")

if(satuan == "f"):
    print('celcius = ',5/9*(suhu-32), "derajat celcius")
    print('reamur = ',4/9*(suhu-32), 'derajat reamur')
    print('fahrenheit = ',suhu , "derajat farenheit")
    print('kelvin = ',5/9*(suhu - 32)+273,'derajat kelvin')