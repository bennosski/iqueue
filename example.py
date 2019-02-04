from iqueue import iqueue

v = [1,2,3,4]

iq = iqueue(v)

iq.append(1)
iq.append('x')

print('iq = {}'.format(iq))

print('iq[3] = {}'.format(iq[3]))

iq.prepend('a')
iq.prepend('c')
iq.append('b')

print('iq = {}'.format(iq))
print('iq.pop_front() = {}'.format(iq.pop_front()))
print('iq.pop_end() = {}'.format(iq.pop_end()))

print('iq = {}'.format(iq))

print('loop over elements')
for x in iq:
    print(x)



