tuple=(1,2,3)
value_to_insert=10
pos=2
new_tuple=tuple[:pos]+(value_to_insert,)+tuple[pos:]
print("tuple before insertion is:",tuple)
print("new tuple after insertion is:",new_tuple) 
