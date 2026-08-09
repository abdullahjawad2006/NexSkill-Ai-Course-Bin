import numpy as np
price,acre_lot,street,zip_code=np.genfromtxt("RealEstate-USA.csv",delimiter=',',usecols=(2,5,6,9),unpack=True,dtype=None,skip_header=1)
print(price)
print(acre_lot)
print(street)
print(zip_code)

print(np.min(price))
print("USA Real Estate Price mean:",np.mean(price))
print("USA Real Estate Price average:",np.average(price))
print("USA Real Estate Price average:",np.average(price))
print("USA Real Estate Price std:",np.std(price))
print("USA Real Estate Price mod:",np.median(price))
print("USA Real Estate Price percentile-25:",np.percentile(price,25))
print("USA Real Estate percentile -75:",np.percentile(price,75))
print("USA Real Estate percentile-3:",np.percentile(price,3))
print("USA Real Estate Price min;",np.min(price))
print("USA Real Estate Price max:",np.max(price))

print("USA Real Estate Price square:",np.square(price))
print("USA Real Estate sqrt:",np.sqrt(price))
print("USA Real Estate Price pow:",np.power(price,price))
print("USA Real Estate abs:",np.abs(price))

addition=street + zip_code
subtraction=street - zip_code
multiplication=street * zip_code
division=street/zip_code

print('USA Real Estate - street - zipcode - Addition:',addition)
print("USA Real Estate - street - zipcode - Subtraction: ",subtraction)
print("USA Real Estate - street - zipcode - Multiplication:",multiplication)
print("USA Real Estate - street - zipcode Division:",division)

pricePie=(price/np.pi) + 1 
sin_values=np.sin(pricePie)
cosine_values=np.cos(pricePie)
tangent_values=np.tan(pricePie)

print("USA Real Estate Price - div - pie - Sine values:",sin_values)
print("USA Real Estate Price - div - pie - Cosine values:",cosine_values)
print("USA Real Estate Price - div - pie - Tangent values:",tangent_values)

print('USA Real Estate Price - div - pie - Exponential values:',np.exp(pricePie))

log_array=np.log(pricePie)
log10_array=np.log10(pricePie)

print("USA Real Estate Price - div - pie - Natural logarithm values:", log_array)
print("USA Real Estate Price - div - pie=Base-10 lograrithm values: ",log10_array)

sin_values=np.sinh(pricePie)
print("USA Real Estate Price - div - pie - Hyperbolic Sine values:",sin_values)

cosh_values=np.cosh(pricePie)
print('USA Real Estate Price - div - pie - Hyperbolic Cosine values:',cosh_values)

tanh_values=np.tanh(pricePie)
print('USA Real Estate Price - div - pie - Hyperbolic Tangent values:',tanh_values)

asinh_values=np.arcsin(pricePie)
print("USA Real Estate - div - pie - Inverse Hyperbolic Sine values:",asinh_values)

acosh_values=np.arccosh(pricePie)
print("USA Real Estate Price - div - pie - Inverse Hyperbolic Cosine values:",acosh_values)

D2streetzipcode=np.array([street,zip_code])
print("USA Real Estate street Plus zipcode - 2 dimentional array-",D2streetzipcode)

print("USA Real Estate street PLus zipcode - 2 dimentional array - dimension,",D2streetzipcode.ndim)

print("USA Real Esate street Plus zipcode - 2 dimentional array - total number of elements",D2streetzipcode.size)

print("USA Real Estate street Plus zipcode - 2 dimentional array - gives size of array in each dimension",D2streetzipcode.shape)

print("USA Real Estate street Plus zipcode - 2 dimentional array - data type",D2streetzipcode.dtype)

D2streetzipcodeSlice=D2streetzipcode[0:1:1, 1:5:1]
print('USA Real Estate street Plus zipcode - 2 dimentional array - Splicing array - D2[:1,:5]',D2streetzipcodeSlice)

D2streetzipcodeSlice2=D2streetzipcode[:1,4:15:4]
print("USA Real Estate street Plus zipcode - 2 dimentional array - Splicing array - D2streetzipcode[:1, 4:15:4]",D2streetzipcodeSlice2)

D2streetzipcodeSliceItemOnly=D2streetzipcodeSlice[0,1]
print("USA Real Estate street PLus zipcode - 2 dimentional array - Index array - D2streetzipcodeSlice[1,5]",D2streetzipcodeSliceItemOnly)
D2streetzipcodeSliceItemOnly=D2streetzipcodeSlice[0,2]
print('USA Real Estate street Plus zipcode - 2 dimentional array - index array - D2streetzipcode[0,2]',D2streetzipcodeSliceItemOnly)

for elem in np.nditer(D2streetzipcode):
    print(elem)

for index,elem in np.ndenumerate(D2streetzipcode):
    print(index,elem)

D2streetzipcode1TO298=np.reshape(D2streetzipcode,(20,40))
print("USA Real Estate street Plus zipcode - 2 dimentioanl array - np.reshape (D2streetzipcode,(1,298)):",D2streetzipcode1TO298)

print("USA Real Estate street PLus zipcode - 2 dimentional array - np.reshpe(D2streetzipcode,(1,298)):Size",D2streetzipcode1TO298.size)

print("USA Real Estate street PLus zipcode - 2 dimentional array -np.reshape(D2streetzipcode,(1,298)):shape",D2streetzipcode1TO298.ndim)

print("USA Real Estate street PLus zipcode - 2 dimentional array - np.reshape(D2streetzipcode,(1,298)):shape",D2streetzipcode1TO298.shape)

print()




