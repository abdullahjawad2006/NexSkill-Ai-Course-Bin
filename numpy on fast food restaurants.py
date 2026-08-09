#FastFoodRestaurants.csv
import numpy as np
address,latitude,longitude,name=np.genfromtxt("FastFoodRestaurants.csv",delimiter=',',usecols=(0,4,5,6),unpack=True,dtype=('U100','f8','f8','U100'),encoding='utf-8',skip_header=1,invalid_raise=False)
print(address)
print(latitude)
print(longitude)
print(name)

print(np.min(longitude))

#FastFoodRestaurants - statistics operations 
print("Fast Food Restaurants Longitude mean:",np.mean(longitude))
print("Fast Food Restaurants Longitude average:",np.average(longitude))
print("Fast Food Restaurants Longitiude std:",np.std(longitude))
print("Fast Food Restaurants Longitude median:",np.median(longitude))
print("Fast Food Restaurants Percentile-25:",np.percentile(longitude,25))
print("Fast Food Restaurants Longitude percentile-75:",np.percentile(longitude,75))
print("Fast Food Restaurants percentile-3:",np.percentile(longitude,3))
print("Fast Food Restaurants Longitude min:",np.min(longitude))
print("Fast Food Restaurants Longitude max:",np.max(longitude))

#Fast Food Restaurants - maths operations 
print("Fast Food Restaurants square:",np.square(longitude))
print("Fast Food Restaurants sqrt:",np.sqrt(longitude))
print("Fast Food Restaurants Longitude pow:",np.power(longitude,longitude))
print("Fast Food Restaurants abs:",np.abs(longitude))

#Perfrom basic arithmetic operations 
addition=longitude + latitude
subtraction=longitude - latitude
multiplication=longitude*latitude
division=longitude/latitude

print("Fast Food Restaurants - Longitude - Latitude - addition:",addition)
print("Fast Food Restaurants - Longitude - Latitude - subtraction:",subtraction)
print("Fast Food Restaurants - Longitude - Latitude - multiplication:",multiplication)
print("Fast Food Restaurants - Longitude - Latitude division:",division)

#Trigonometric Functions 
longitudepie=(longitude/np.pi) + 1
#Calculate sine,cosine, and tangent 
sine_values=np.sin(longitude)
cos_values=np.cos(longitude)
tan_values=np.tan(longitude)

print("Fast Food Restaurants - Longitude - div - pie - sine values:",sine_values)
print("Fast Food Restaurants - Longitude - div - pie - cosine values:",cos_values)
print("Fast Food Restaurants - Longitude - div - pie - tangent values:",tan_values)

print("Fast Food Restaurants Longitude - div - pie - Exponential values:",np.exp(longitudepie))

#Calculate the natural logarithm and base-10 logarithm 
log_array=np.log(longitudepie)
log10_array=np.log10(longitudepie)

print("Fast Food Restaurants Longitude - div - pie - natural logarithm values:",log_array)
print("Fast Food Restaurants Longitude - div - pie - base 10 logarithm values:",log10_array)

#Calculate the hyperbolic sine of each element 
sinh_values=np.sinh(longitudepie)
print("Fast Food Restaurants Longitude - div - pie - hyperbolic sine values:",sinh_values)

#Calculate the hyperbolic cosine of each element 
cosh_values=np.cosh(longitudepie)
print("Fast Food Restaurants Longitude - div - pie - hyperbolic cosine values:",cosh_values)

#Calculate the hyperbolic tangent of each element 
tanh_values=np.tanh(longitudepie)
print("Fast Food Restaurants Longitude - div - pie - hyperbolic tangent values:",tanh_values)

#Calculate the inverse hyperbolic sine of each element 
asinh_values=np.arcsinh(longitudepie)
print("Fast Food Restaurants Longitude - div - pie hyperbolic sine values:",asinh_values)
#Calculate the inverse hyperbolic cosine of each element 
acosh_values=np.arccosh(longitudepie)
print("Fast Food Restaurants Longitude - div - pie hyperbolic cosine values:",acosh_values)

#Fast Food Restaurant Longitude plus latitude - 2 dimentional array 
D2longLat=np.array([longitude,latitude])
print("Fast Food Restaurant Longitude plus Latitude - 2 dimentional array -",D2longLat)

#check the dimension of array1
print("Fast Food Restaurant Longitude plus latitude - 2 dimentional array - dimension",D2longLat.ndim)
#return total number of elements in array1
print("Fast Food Restaurants Longitude plus Latitude - total number of elements",D2longLat.size)

#returns a tuple that gives size of each dimension
print("Fast Food Restaurants Longitude plus Latitude - gives size of array in each dimension",D2longLat.size)

#check the data type of array1
print("Fast Food Restaurants Longitude plus Latitude - 2 dimentional array - data type",D2longLat.dtype)

#Splicing array 
D2longLatslice=D2longLat[0:5:1,1:10]
print("Fast Food Restaurants Longitude plus Latitude - 2 dimentional array - splicing array - D2LongLat",D2longLatslice)

D2longLatslice2=D2longLat[:1,4:15]
print("Fast Food Restaurants Longitude plus Latitude - 2 dimentional array - Splicing array - D2longlat:",D2longLatslice2)

#Indexing array
D2longLatsliceitemonly=D2longLatslice[0,1]
print("Fast Food Restaurants Longitude plus Latitude - 2 dimentional array - index array - D2longLatslice:",D2longLatsliceitemonly)

D2longLatslice2itemonly=D2longLatslice2[0,2]
print("Fast Food Restaurants Longitude plus Latitude - 2 dimentional array - index array -D2longlatslice2:",D2longLatslice2itemonly)

for elem in np.nditer(D2longLat):
      print(elem)

#If you need indexes as a tuple for 2D table,then:
for index,elem in np.ndenumerate(D2longLat):
      print(index,elem)
D2longlatreshape=np.reshape(D2longLat,(999,20))
print("Fast Food Restaurants Longitude plus Latitude - 2 dimentional array - np.reshape(D2longlat,(2500,40)):",D2longlatreshape)
print("Fast Food Restaurants Longitude plus Latitude - 2 dimentional array -ndim - D2longlatreshape:",D2longlatreshape.ndim)
print("Fast Food Restaurants Longitude plus Latitude - 2 dimentional array - size of D2longlatreshape:",D2longlatreshape.size)
print()




