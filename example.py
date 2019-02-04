from iqueue import iqueue

v = [1,2,'a',1,4.0]

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

print('iq.count(1) = {}'.format(iq.count(1)))

iq.extendleft([3,2,1])
print('iq = {}'.format(iq))

iq.clear()
print('iq = {}'.format(iq))


