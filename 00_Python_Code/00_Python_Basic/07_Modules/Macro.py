# BitWise Operator (  &-->(*) |-->(+) ^-->(True When Have Diff) >>  <<  )


# Set Bit
def Set_Bit(Copy_Var, Copy_BitNum):
    Copy_Var |= 1<<Copy_BitNum
    return Copy_Var


# Clear Bit
def Clear_Bit(Copy_Var, Copy_BitNum):
    Copy_Var &= ~(1 << Copy_BitNum)
    return Copy_Var


# Toggle Bit
def Toggle_Bit(Copy_Var, Copy_BitNum):
    Copy_Var ^= (1 << Copy_BitNum)
    return Copy_Var


# Get Bit
def Get_Bit(Copy_Var, Copy_BitNum):
    x= (Copy_Var>>Copy_BitNum)&1
    return x
