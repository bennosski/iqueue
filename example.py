from iqueue import iqueue

v = [1,2,'a',4.0]

iq = iqueue(v)

iq.append('x')

print('iq = {}'.format(iq))
print('iq[3] = {}'.format(iq[3]))

iq.appendleft('a')

print('iq = {}'.format(iq))
print('iq.popleft() = {}'.format(iq.popleft()))
print('iq.pop() = {}'.format(iq.pop()))

print('iq = {}'.format(iq))

print('loop over elements')
for x in iq:
    print(x)



