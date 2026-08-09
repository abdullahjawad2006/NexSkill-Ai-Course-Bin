import numpy as np
listyear,assessedvalue,saleamount,propertytype=np.genfromtxt("Real_Estate_Sales_2001-2022_GL-Short.csv",delimiter=',',usecols=(1,5,6,8),unpack=True,dtype=None,skip_header=1,encoding="utf-8",invalid_raise=False)
print(listyear)
print(assessedvalue)
print(saleamount)
print(propertytype)

print(np.min(assessedvalue))

#statistics operations 
print("Real Estate Sales Assessed Value mean:",np.mean(assessedvalue))
print("Real Estate Sales Assessed Value average(assessed value):",np.average(assessedvalue))
print("Real Estate Sales Assessed Value std:",np.std(assessedvalue))
print("Real Estate Sales Assessed Value mod:",np.median(assessedvalue))
print("Real Estate Sales Assessed Value percentile-25:",np.percentile(assessedvalue,25))
print("Real Estate Sales Assessed Value percentile-75:",np.percentile(assessedvalue,75))
print("Real Estate Sales Assessed Value percentile-3:",np.percentile(assessedvalue,3))
print("Real Estate Sales Assessed Value min:",np.min(assessedvalue))
print("Real Estate Sales Assessed Value max:",np.max(assessedvalue))

#maths operations 
print("Real Estate Sales Assessed Value square:",np.square(assessedvalue))
print("Real Estate Sales Assessed Value sqrt:",np.sqrt(assessedvalue))
print("Real Estate Sales Assessed Value pow:",np.power(assessedvalue,assessedvalue))
print("Real Estate Sales Assessed Value abs:",np.abs(assessedvalue))

#basic arithmetic operations 
addition=assessedvalue + saleamount 
subtraction=assessedvalue - saleamount 
multiplication=assessedvalue * saleamount
division=assessedvalue / saleamount

print("Real Estate Sales Assessed Value - Sale Amount addition:",addition)
print('Real Estate Sales Assessed Value - Sales Amount subtraction:',subtraction)
print("Real Estate Sales Assessed Value - Sales Amount multiplication:",multiplication)
print("Real Estate Sales Assessed Value - Sale Amount division:",division)

assessedvaluepie=(assessedvalue/np.pi)+1
sine_values=np.sin(assessedvaluepie)
cosine_values=np.cos(assessedvaluepie)
tangent_values=np.tan(assessedvalue)

print("Real Estate Sales assessedvaluepie - sine values:",sine_values)
print("Real Estate SAles assessedvaluepie - cosine values:",cosine_values)
print("Real Estate Sales assessedvaluepie - tangent values:",tangent_values)

print("Real Estate Sales assessedvaluepie Exponential values:",np.exp(assessedvaluepie))

log_array=np.log(assessedvaluepie)
log10_array=np.log10(assessedvalue)

print("Real Estate Sales assessedvaluepie - Natural logarithm values:",log_array)
print("Real Estate Sales assessedvaluepie - Base10 logarithm values:",log10_array)

sinh_values=np.sinh(assessedvaluepie)
print("Real Estate Sales assessedvaluepie - Hyperbolic Sine values:",sinh_values)

cosh_values=np.cosh(assessedvalue)
print("Real Estate Sales assessedvaluepie - Hyperbolic Cosine values:",cosh_values)

tanh_values=np.tanh(assessedvaluepie)
print("Real Estate Sales assessedvaluepie - Hyperbolic Tangent values:",tanh_values)

asinh_values=np.arcsinh(assessedvaluepie)
print("Real Estate Sales assessedvaluepie Inverse Hyperbolic Sine values:",asinh_values)

acosh_values=np.arccosh(assessedvaluepie)
print("Real Estate Sales Inverse Hyperbolic Cosine values:",acosh_values)

#2D Array 
D2assessedvaluesaleamount=np.array([assessedvalue,saleamount])
print("Real Estate Sales D2assessedvaluesaleamount 2D array:",D2assessedvaluesaleamount)

print("Real Estate Sales D2assessedvaluesaleamount 2D array dimension:",D2assessedvaluesaleamount.ndim)

print("Real Estate Sales D2assessedvaluesaleamount 2D array size:",D2assessedvaluesaleamount.size)

print('Real Estate Sales D2assessedvaluesalesamount 2D array shape',D2assessedvaluesaleamount.shape)

print("Real Estate Sales D2assessedvaluesaleamount 2D array data type:",D2assessedvaluesaleamount.dtype)

D2assessedvaluesaleamountSlice=D2assessedvaluesaleamount[0:1,1:51]
print("Real Estate Sales Slicing of D2assessedvaluesaleamount:",D2assessedvaluesaleamountSlice)

D2assessedvaluesaleamountSlice2=D2assessedvaluesaleamount[1:2,70:121]
print("Real Estate Sales Slicing of D2assessedvaluesaleamount:",D2assessedvaluesaleamountSlice2)

#Indexing array
D2assessedvaluesaleamountitemonly=D2assessedvaluesaleamountSlice[0,30]
print("Real Estate Sales Indexing of D2assessedvlauesaleamountSlice:",D2assessedvaluesaleamountitemonly)

D2assessedvaluesaleamountitemonly2=D2assessedvaluesaleamountSlice2[0,20]
print("Real Estate Sales Indexing of D2assessedvaluesaleamountSlice2:",D2assessedvaluesaleamountitemonly2)

for elem in np.nditer(D2assessedvaluesaleamount):
    print(elem)

for index,elem in np.ndenumerate(D2assessedvaluesaleamount):
    print(index,elem)

D2assessedvaluesaleamount139to2=np.reshape(D2assessedvaluesaleamount,(139,2))
print("Real Estate Sales reshaping of D2assessedvlauesaleamount",D2assessedvaluesaleamount139to2)

print("Real Estate Sales size of D2assessedvaluesaleamount139to2:",D2assessedvaluesaleamount139to2.size)

print("Real Estate Sales ndim of D2assessedvaluesaleamount139to2:",D2assessedvaluesaleamount139to2.ndim)

print("Real Estate Sales shape of D2assessedvaluesaleamount139to2:",D2assessedvaluesaleamount139to2.shape)


