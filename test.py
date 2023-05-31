from ohmytmp import Ohmytmp
from ohmytmp_plugins.destination import DstType, VERSION

print(VERSION)

ai = Ohmytmp()
di = DstType('../0dst')
ai.register(di)
# ai.reg_f(lambda x: print(x.to_dict()))

ai.walk('../example')
ai.walk('../core/src')

for i in di.data.items():
    print(*i)
