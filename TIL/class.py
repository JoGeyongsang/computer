a, b = map( int, input().split() )
print(a, b)

print('{}-{}-{}'.format(day, month, year))

id1 = '000907-1121112'
id2 = id1.split('-')
id2[0] + id2[1]
''.join(id2)
id1.replace('-', '')

print(*strs, sep='\n')

print(date[0:2], date[2:4], date[4:])

'17:23:57'.split(':')[1]
print( read.split(':')[1] )

a, b = map(int, '123 -123'.split())
print( a + b )

'{:x}'.format(10)
f'{10:x}'

a = int( input() )
print( hex(a)[2:] )
a = int( input() )
print( f'{a:x}' )

a = int( input() )
print( hex(a)[2:].upper() )

a = 'a'
next = ord(a) + 1
print( chr(next) )


