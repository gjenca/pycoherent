import sympy
import coherent
import perm

n=4
ps=[]
cycles_s=[list(range(2,n+1))+[1]]
print(cycles_s)
s=perm.p_to_p2(perm.cyc_to_perm(cycles_s,n=n))
cycles_r=[]
for i in range(n//2+1):
    cyc=list(set([i+1,(-i % n)+1]))
    cycles_r.append(cyc)
print(cycles_r)
r=perm.p_to_p2(perm.cyc_to_perm(cycles_r,n=n))
sq=[(x,y) for x in range(1,n+1) for y in range(1,n+1)]
orbs=perm.orbits([s,r],sq)
print('colors:')
for i,orb in enumerate(orbs):
    print(f'{i}:',orb)
print('inverses:')
print(coherent.inverses(orbs))
print('valencies:')
for i,orb in enumerate(orbs):
    print(f'{i}:',coherent.valency(orb))
O_nondag=coherent.o_matrix_nodag(orbs)
print('O_nondag matrix:')
print(sympy.pretty(O_nondag))
print('Spectrum nondag:')
print(O_nondag.eigenvals())
O_dag=coherent.o_matrix_dag(orbs)
print('O_dag matrix:')
print(sympy.pretty(O_dag))
print('Spectrum dag:')
print(O_dag.eigenvals())
