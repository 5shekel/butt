
the linkit 7688 dev boards have a good 3v3 regulator, the [XC6220](http://media.digikey.com/pdf/Data%20Sheets/Torex/XC6220.pdf) 

## low dropout

![]http://i.imgur.com/Kw4ZbtX.jpg

the linkit power draw even under peeks will not surpass the 400mA
and at idle can stablise on 

## 1A max current
this effects the dropout, and temprature. 



### fails
the  MP1583 Step-Down convertor cant hepl as its "4.75V to 23V Operating Input Range", the 


# sensors
## BMP180 pressure sensors
https://cdn-shop.adafruit.com/datasheets/BST-BMP180-DS000-09.pdf

i2c 
Pressure range: 300 ... 1100hPa (+9000m ... -500m relating to sea level)
Supply voltage: 1.8 ... 3.6V (VDD)


##MPU6050

## lols
http://www.penguin.cz/~utx/hardware/Creatic_18650_Power_Bank/CT6201_v1.0.pdf

### charging
no worries, just hook both battary and load on the same line [ladyada](https://learn.adafruit.com/li-ion-and-lipoly-batteries/proper-charging)

[TP4056 1A Linear Li-lon Battery Charger with Thermal](https://dlnmh9ip6v2uc.cloudfront.net/datasheets/Prototyping/TP4056.pdf)

#video streaming
https://iamblue.gitbooks.io/linkit-smart-nodejs/content/en/basic/video_streaming.html

Bus 001 Device 002: ID 1e4e:0110 Cubeternet
https://github.com/foosel/OctoPrint/wiki/Webcams-known-to-work