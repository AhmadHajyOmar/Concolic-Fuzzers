import z3
from fuzzingbook.ConcolicFuzzer import ConcolicTracer
from RandomGeneration import random_int, random_string

def Not(x: bool):
    return not x

class RandomConcolicTracer(ConcolicTracer):
    def reval(self, attempts: int):

        assert attempts > 0
        print("..............................attempts..............................")
        print(attempts)
        #return 'unsat', {}
        # TODO: Implement me
        out = ()
        
        if attempts <= 0:

            return 'unsat', {}
        else:
            stop_searching = False
            while not stop_searching:
                if attempts == 0:
                    return 'unsat', {}
                for i in self.decls:
                    # print(i)
                    if self.decls[i] == "Int":
                        # print(self.decls[i])
                        globals()[i] = random_int()
                        #print(globals()[i])
                    else:
                        if self.decls[i] == "String":
                            globals()[i] = random_string()
                and_bool = True
                # print(globals()[2])


                for cc in self.path:
                    ##print(cc)

                    if not eval(str(cc), globals()):
                        and_bool = False

                if and_bool:
                    stop_searching = True
                    parm_dtype = {i: (globals()[i], self.decls[i]) for i in self.decls}
                    #print(parm_dtype)
                    output = list()
                    output.append('sat')
                    output.append(parm_dtype)

                    out = tuple(output)
                    #print(type(out))
                    #print(out)
                    return out
                    #return 'sat', {i: (globals()[i], self.decls[i]) for i in self.decls}
                attempts = attempts - 1




