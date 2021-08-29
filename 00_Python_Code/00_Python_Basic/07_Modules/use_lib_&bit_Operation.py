#Normal Import You Mast Difine Which Lib You Use --> Can Two Fun in Two Lib Have Same Name So You Must LibName.Fun
import Lib_0

x =Lib_0.add(4,5)
print("SUM-->",x)

# Import My Lib By NikeName
import Lib_0 as kk
x =kk.add(4,5)
print("SUM-->",x)


#Import Only One Fun From Lib
from Lib_0 import div
x =div(10,5)
print("Div-->",x)

#BitWise Operator (  & | ^ >>  <<  )
