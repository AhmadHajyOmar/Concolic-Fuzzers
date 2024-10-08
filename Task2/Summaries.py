import string

import z3
import fuzzingbook.ConcolicFuzzer
from fuzzingbook.ConcolicFuzzer import zstr, zint, zbool, fresh_name

class zint(zint):
    def __abs__(self) -> zint:
     # TODO: Implement me
     name = '__abs__%d' % fresh_name()
     concrete_result = self.v.__abs__()
     result = zint.create(self.context, name, concrete_result)
     sym_constraint = z3.is_to_int(self.z)
     self.context[1].append(sym_constraint == result.z)
     return result

class zstr(zstr):
    def __len__(self): # Do not change me
        return self._len

    def __contains__(self, m: str) -> zbool:
         # TODO: Implement me
         name = '__contains__%d' % fresh_name()
         concrete_result = self.v.__contains__(m)
         result = zbool.create(self.context, name, concrete_result)
         sym_constraint = z3.Contains(self.z, m)
         self.context[1].append(sym_constraint == result.z)
         return result

    def capitalize(self) -> zstr:
        pass # TODO: Implement me

    def endswith(self, other: zstr, start: int = None, stop: int = None) -> zbool:
        assert start is None, 'No need to handle this parameter'
        assert stop is None, 'No need to handle this parameter'

        name = 'endswith_%d' % fresh_name()
        concrete_result = self.v.endswith(other, None, None)
        result = zbool.create(self.context, name, concrete_result)
        sym_constraint = z3.SuffixOf(other, self.z)
        self.context[1].append(sym_constraint == result.z)
        return result

    def isalnum(self) -> zbool:
      charset = z3.Union([z3.Re(z3.StringVal(c)) for c in string.ascii_letters + string.digits])
      template = z3.Star(charset)
      name = 'isalnum_%d' % fresh_name()
      concrete_result = self.v.isalnum()
      result = zbool.create(self.context, name, concrete_result)
      sym_constraint = z3.And(z3.Length(self.z) > 0, z3.InRe(self.z, template))
      self.context[1].append(sym_constraint == result.z)
      return result

    def isdecimal(self) -> zbool:
        charset = z3.Union([z3.Re(z3.StringVal(c)) for c in string.hexdigits])
        template = z3.Star(charset)
        name = 'isdecimal_%d' % fresh_name()
        concrete_result = self.v.isdecimal()
        result = zbool.create(self.context, name, concrete_result)
        sym_constraint = z3.And(z3.Length(self.z) > 0, z3.InRe(self.z, template))
        self.context[1].append(sym_constraint == result.z)
        return result

    def isdigit(self) -> zbool:
        charset = z3.Union([z3.Re(z3.StringVal(c)) for c in string.digits])
        template = z3.Star(charset)
        name = 'isdigit_%d' % fresh_name()
        concrete_result = self.v.isdigit()
        result = zbool.create(self.context, name, concrete_result)
        sym_constraint = z3.And(z3.Length(self.z) > 0, z3.InRe(self.z, template))
        self.context[1].append(sym_constraint == result.z)
        return result

    def islower(self) -> zbool:
      charset = z3.Union([z3.Re(z3.StringVal(c)) for c in string.ascii_lowercase])
      template = z3.Star(charset)
      name = 'islower_%d' % fresh_name()
      concrete_result = self.v.islower()
      result = zbool.create(self.context, name, concrete_result)
      sym_constraint = z3.And(z3.Length(self.z) > 0, z3.InRe(self.z, template))
      self.context[1].append(sym_constraint == result.z)
      return result

    def isnumeric(self) -> zbool:
        charset = z3.Union([z3.Re(z3.StringVal(c)) for c in string.digits])
        template = z3.Star(charset)
        name = 'isnumeric_%d' % fresh_name()
        concrete_result = self.v.isnumeric()
        result = zbool.create(self.context, name, concrete_result)
        sym_constraint = z3.And(z3.Length(self.z) > 0, z3.InRe(self.z, template))
        self.context[1].append(sym_constraint == result.z)
        return result

    def isprintable(self) -> zbool:
        charset = z3.Union([z3.Re(z3.StringVal(c)) for c in string.printable])
        template = z3.Star(charset)
        name = 'isprintable_%d' % fresh_name()
        concrete_result = self.v.isprintable()
        result = zbool.create(self.context, name, concrete_result)
        sym_constraint = z3.And(z3.Length(self.z) > 0, z3.InRe(self.z, template))
        self.context[1].append(sym_constraint == result.z)
        return result

    def isspace(self) -> zbool:
        charset = z3.Union([z3.Re(z3.StringVal(c)) for c in string.capwords(' ', ' ')])
        template = z3.Star(charset)
        name = 'isspace_%d' % fresh_name()
        concrete_result = self.v.isspace()
        result = zbool.create(self.context, name, concrete_result)
        sym_constraint = z3.And(z3.Length(self.z) > 0, z3.InRe(self.z, template))
        self.context[1].append(sym_constraint == result.z)
        return result

    def isupper(self) -> zbool:
        charset = z3.Union([z3.Re(z3.StringVal(c)) for c in string.ascii_uppercase])
        template = z3.Star(charset)
        name = 'isupper_%d' % fresh_name()
        concrete_result = self.v.isupper()
        result = zbool.create(self.context, name, concrete_result)
        sym_constraint = z3.And(z3.Length(self.z) > 0, z3.InRe(self.z, template))
        self.context[1].append(sym_constraint == result.z)
        return result


    def rfind(self, sub: str, start: int = None, stop: int = None) -> zint:
        assert start is None, 'No need to handle this parameter'
        assert stop is None, 'No need to handle this parameter'
        # TODO: Implement me
        name = 'rfind_%d' % fresh_name()
        concrete_result = self.v.rfind(sub, None, None)
        result = zint.create(self.context, name, concrete_result)
        sym_constraint = z3.LastIndexOf(self.z, sub)
        self.context[1].append(sym_constraint == result.z)
        return result

    def swapcase(self) -> zstr:
         pass # TODO: Implement me


    def title(self) -> zstr:
        pass # TODO: Implement me




def setup_summary():
    fuzzingbook.ConcolicFuzzer.__dict__['zstr'] = zstr
    fuzzingbook.ConcolicFuzzer.__dict__['zint'] = zint
    fuzzingbook.ConcolicFuzzer.Z3_OPTIONS = '-T:5' # Set solver timeout to 5 seconds. Might be possible to reduce this given a strong CPU, or must be increased with a weak CPU.
