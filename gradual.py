# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 19:39:47 2018

@author: aboe
"""

class Ty:
    pass

class Bool(Ty):
    def __init__(self):
        pass
    
class Fun(Ty):
    def __init__(self,t1,t2):
        self.t1 = t1
        self.t2 = t2
    def tequal(self,t1,t2):
        if (t1 == Bool() & t2 == Bool()):
            return True
        if (isinstance(t1,Fun) and isinstance(t2,Fun)):
            return tequal(t1.t1,t2.t1) and tequal(t1.t2,t2.t2)
        return False
        
class Empty(Ty):
    def __init__(self):
        pass
    
class Unit(Ty):
    def __init__(self):
        pass

class Sum(Ty):
    def __init__(self, t1,t2):
        self.t1 = t1
        self.t2 = t2

class Prod(Ty):
    def __init__(self):
        pass

class QuestionMark(Ty):
    def __init__(self):
        pass
    
class Gamma(Ty):
    def __init__(self):
        pass
        
### Expressions ###
class Exp():
    pass
        
class T(Exp):
    def __init__(self):
        pass
    def infer(self, tenv):
        return Bool()
    
class F(Exp):
    def __init__(self, t):
        self.t = t
    def infer(self):
        return Bool()
        
class if_(Exp):
    def __init__(self, e1, e2, e3):
        self.e1 = e1
        self.e2 = e2
        self.e3 = e3
    def infer(self, tenv):
        t1 = self.e1.infer(tenv)
        t2 = self.e2.infer(tenv)
        t3 = self.e3.infer(tenv)
        if(t1 == Bool() & t2 == t3):
            return t2

class Var(Exp): # or GVar
    def __init__(self, e1):
        self.e1 = e1
    def infer(self, tenv):
        t1 = self.e1.infer(tenv)
        return t1

class Const(Exp):
    def __init__(self, c):
        self.c = c
    def infer(self, tenv):
        t = self.c.infer(tenv)
        return t

class Lam(Exp): # or GLam
    def __init__(self, x, t1, e):
        self.x = x
        self.t1 = t1
        self.e = e
    def infer(self, tenv):
        t2 = self.e.infer(tenv)
        return Fun(self.t1,t2)


class App(Exp):
    def __init__(self, e1, e2):
        self.e1 = e1
        self.e2 = e2
    def infer(self, tenv):
        t1 = self.e1.infer(tenv)
        t2 = self.e1.infer(tenv)
        if(isinstance(t1, Fun)):
            if(t1.t1 == t2):
                return t2
            
class Absurd(Exp):
    def __init__(self,e,t):
        self.e = e
        self.t = t
    def infer(self, tenv):
        tp = self.e.infer(tenv)
        if(isinstance(tp,Empty)):
            return self.t

class Inl(Exp):
    def __init__(self, e, tp):
        self.e = e
        self.tp = tp
    def infer(self, tenv):
        t = self.e.infer(tenv)
        if(isinstance(self.tp, Sum)):
            if (self.tp.t1 == t):
                return self.tp

class Inr(Exp):
    def __init__(self, e, tp):
        self.e = e
        self.tp = tp
    def infer(self, tenv):
        t = self.e.infer(tenv)
        if(isinstance(self.tp, Sum)):
            if (self.tp.t2 == t):
                return self.tp

class Case(Exp):
    def __init__(self, e1, x2, e2, x3, e3):
        self.e1 = e1
        self.x2 = x2
        self.e2 = e2
        self.x3 = x3
        self.e3 = e3
    def infer(self, tenv):
        t1 = self.e1.infer(tenv)
        if(isinstance(t1,Sum)):
            t2 = self.e2.infer(tenv)
            t3 = self.e3.infer(tenv)
            if (t2 == t3):
                return t2

class Pair(Exp):
    def __init__(self,e1, e2):
        self.e1 = e1
        self.e2 = e2
    def infer(self, tenv):
        t1 = self.e1.infer(tenv)
        t2 = self.e2.infer(tenv)
        return Prod(t1,t2)

class Projl(Exp):
    def __init__(self, e):
        self.e = e
    def infer(self, tenv):
        t = self.e.infer(tenv)
        if (isinstance(t, Prod)):
            return t.t1
        
class Projr(Exp):
    def __init__(self, e):
        self.e = e
    def infer(self, tenv):
        t = self.e.infer(tenv)
        if (isinstance(t, Prod)):
            return t.t2
    
class GApp1(Exp):
    def __init__(self,e1,e2):
        self.e1 = e1
        self.e2 = e2
    def infer(self, tenv):
        t1 = self.e1.infer(tenv)
        if(isinstance(t1,QuestionMark)):
            return QuestionMark()

def CheckConsistency(t1, t2):
    if(t1 == t2):
        return True
    elif(isinstance(t1, QuestionMark) or isinstance(t2, QuestionMark)):
        return True
    elif(isinstance(t1, Fun) and isinstance(t2, Fun)):
        if(CheckConsistency(t1.t1,t2.t1) and CheckConsistency(t1.t2, t2.t1)):
            return True
        else:
            return False
    else:
        return False

class GApp2(Exp):
    def __init__(self, e1, e2):
        self.e1 = e1
        self.e2 = e2
    def infer(self, tenv):
        t1 = self.e1.infer(tenv)
        t2 = self.e2.infer(tenv)
        if(isinstance(t1,Fun) and CheckConsistency(t2, t1)):
            return t1.t2
        
        
        
def TestFunction():
    tenv = 
    truetest = T()
    falsetest = F()
    iftest = if_(truetest, falsetest, Sum(Bool(), Bool()))
    tenv = []
    if truetest.infer(tenv)



    