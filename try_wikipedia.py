import sympy
import coherent
import perm

col0=tuple((i,i) for i in range(1,7))
col1=coherent.symmetrize(((1,2),(1,3),(2,3),(4,5),(4,6),(5,6)))
col2=coherent.symmetrize(((1,4),(2,5),(3,6)))
col3=coherent.remainder([col0,col1,col2],6)
colors=[col0,col1,col2,col3]
print('colors:')
for i,color in enumerate(colors):
    print(f'{i}:',color)
print('inverses:')
print(coherent.inverses(colors))
print('valencies:')
for i,color in enumerate(colors):
    print(f'{i}:',coherent.valency(color))
O_nondag=coherent.o_matrix_nodag(colors)
print('O_nondag matrix:')
print(sympy.pretty(O_nondag))
print('Spectrum nondag:')
print(O_nondag.eigenvals())
O_dag=coherent.o_matrix_dag(colors)
print('O_dag matrix:')
print(sympy.pretty(O_dag))
print('Spectrum dag:')
print(O_dag.eigenvals())

