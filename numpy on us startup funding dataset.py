import numpy as np
industry,investment,valuation,country=np.genfromtxt("startup_growth_investment_data.csv",delimiter=',',usecols=(1,3,4,6),unpack=True,dtype=None,skip_header=1)
print(industry)
print(investment)
print(valuation)
print(country)

print(np.min(investment))

#statistics operations
print("Startup Investment mean:",np.mean(investment))
print("Startup Investment average:",np.average(investment))
print("Startup Investment mod:",np.median(investment))
print("Startup Investment percentile-25:",np.percentile(investment,25))
print("Startup Investment percentile-75:",np.percentile(investment,75))
print("Startup Investment min:",np.min(investment))
print("Startup Investment max;",np.max(investment))

print("Startup Investment square:",np.square(investment))
print("Startup Investment sqrt:",np.sqrt(investment))
print("Startup Investment pow:",np.power(investment,investment))
print("Startup Investment abs:",np.abs(investment))

#basic arithmetic operations 
addition=investment + valuation
subtraction=investment - valuation
multiplication=investment * valuation
divison=investment/valuation

print("Startup Investment - Valuation addition:",addition)
print("Startup Investment - Valuation subtraction:",subtraction)
print("Startup Investment - Valuation multiplication:",multiplication)
print("Startup Investment - Valuation division:",divison)

#Trigonometric Functions 
investmentpie=(investment/np.pi) + 1
sine_values=np.sin(investmentpie)
cosine_values=np.cos(investmentpie)
tangent_values=np.tan(investmentpie)

print("Startup Investment sine values:",sine_values)
print("Startup Investment cosine values:",cosine_values)
print("Startup Investment tangent values:",tangent_values)

log_array=np.log(investmentpie)
log10_array=np.log10(investmentpie)

print("Startup Investment log value:",log_array)
print("Startup Investment log 10 values:",log10_array)

sinh_values=np.sinh(investmentpie)
print("Startup Investment sine hyperbolic values:",sinh_values)
cosh_values=np.cosh(investmentpie)
print("Startup Investment cosine hyperbolic values:",cosh_values)
tanh_values=np.tanh(investmentpie)
print("Startup Investment tangent hyperbolic values:",tangent_values)

asinh_values=np.arcsinh(investmentpie)
print("Startup Investment inverse hyperbolic sine values:",sinh_values)
acosh_values=np.arccosh(investmentpie)
print("Startup Investment inverse hyperbolic cosine values:",acosh_values)

D2investvalue=np.array([investment,valuation])
print("Startup Invest - Value 2D array:",D2investvalue)

print("Startup Invest - value 2D array dimension:",D2investvalue.ndim)

print("Startup Invest - Value 2D array size;",D2investvalue.size)

print("Startup Invest - Value 2D array shape:",D2investvalue.shape)

print("Startup Invest - Value 2D array data type:",D2investvalue.dtype)

D2investvalueSlice=D2investvalue[0:1,1:50]
print("Startup Invest - Value Slicing of D2investvalue1",D2investvalueSlice)

D2investvalueSlice2=D2investvalue[1:2,1:101]
print("Startup Invest - Value Slicing of D2investvalue2",D2investvalueSlice2)

D2investvalueSliceItemOnly=D2investvalueSlice[0,30]
print("Startup Invest - Value indexing of D2investvalueSlice:",D2investvalueSliceItemOnly)
D2investvalueSlice2itemonly=D2investvalueSlice2[0,50]
print('StartUp Invest - Value indexing of D2investvalueSlice2:',D2investvalueSlice2itemonly)

for elem in np.nditer(D2investvalue):
    print(elem)

for index,elem in np.ndenumerate(D2investvalue):
    print(index,elem)

D2investvaluereshape=np.reshape(D2investvalue,(400,25))
print("Startup Invest - Value rehsape of D2investvalue:",D2investvaluereshape)
print("Startup Invest - Value size of D2investvalue:",D2investvaluereshape.size)
print("Startup Invest - Value ndim of D2investvaluereshape:",D2investvaluereshape.ndim)









