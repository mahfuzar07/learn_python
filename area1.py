A,B,C = list(map(float,input().split()))
triangle=0.5*A*C
circle=3.14159*C*C
trapezium=(A+B)/2.0*C
square=(pow(B,2))
rectangle=A*B

print(f"TRIANGULO: {triangle:.3f}")
print(f"CIRCULO: {circle:.3f}")
print(f"TRAPEZIO: {trapezium:.3f}")
print(f"QUADRADO: {square:.3f}")
print(f"RETANGULO: {rectangle:.3f}")
