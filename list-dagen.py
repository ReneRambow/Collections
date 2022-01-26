dagen = ['Maandag', 'Dinsdag', 'Woensdag', 'Donderdag', 'Vrijdag', 'Zaterdag', 'Zondag']

print('Alle Dagen:\n')
for alledagen in dagen:
    print(alledagen)

print('\nWerkdagen:\n')
for werkdagen in dagen[:-2]:
    print(werkdagen)

print('\nWeekenddagen:\n')
print(dagen [-2])
print(dagen [-1])

print('\nAlle Dagen |reversed|:\n')
for alledagen in reversed(dagen):
    print(alledagen)

print('\nWerkdagen |reversed|:\n')
for werkdagen in reversed(dagen [:-2]):
    print(werkdagen)

print('\nWeekenddagen |reversed|:\n')
print(dagen[-1])
print(dagen[-2])