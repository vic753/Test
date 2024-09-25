def affiche_triangle(x:int):
   for i in range (x):
     print(" " * (x - i) + "*" * (i+1))
affiche_triangle(5)
