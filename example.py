
import iqueue

v = [1,2,3,4]

iq = iqueue.iqueue(v)

iq.append(1)
iq.append(7)

print(iq)


iq.prepend('x')
iq.prepend('hello')

print(iq.pop_front())

print(iq)

