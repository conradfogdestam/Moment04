#UPPGIFT A


s1 = int(input("ange rektangelns första sida: "))
s2 = int(input("ange rektangelns andra sida: ")) #int inputs

if s1 == s2:
    print(f'Rektangeln har sidorna {s1} och {s2} vilket gör att arean är {s1*s2}')
    print('Eftersom bägge sidorna är lika långa så är denna rektangel en kvadrat', "\n")

else:
    print(f'Rektangeln har sidorna {s1} och {s2} vilket gör att arean är {s1 * s2}', "\n")

print("Höjd | Volym")  # en liten ghetto "formatering" så att printen ska se bra ut
print("-------------")
for h in range(1,11):    # for loopen som loopar 10 ggr och en print med höjd (h) som adderar 1 varje loop
    print(h," |",s1*s2*h )

