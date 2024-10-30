print("Arzaba Diaz April")
print("1173")
print("3W")
def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)
        print(result)  # Imprime el resultado en cada paso de la recursión
    else:
        result = 0
    return result

print("\n\nRecursion Example Results")
tri_recursion(6)
