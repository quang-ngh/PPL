
import sys
sys.path.append('../utils')
sys.path.append('../../../../target/main/mp/parser')
from Visitor import Visitor
from StaticError import *
from AST import *
from Utils import Utils
from functools import reduce
class ExpHelper:
    @staticmethod
    def isNaNType(expType):
        return type(expType) not in [IntegerType, FloatType]

    @staticmethod
    def isOpForNumber(operator):
        """
        Add, Sub, Divide, Mul
        Modulo
        NotEqual, Equal, Greater, Smaller, GEQ, SEQ
        """
        return str(operator).lower() in ['+', '-', '*', '/', '%', '>', '<', '>=', '<=']

    @staticmethod
    def isOpForStr(operator):
        """String concat: ::"""
        return str(operator).lower() == '::'

    @staticmethod
    def isOpforBool(operator):
        return str(operator).lower() in ['!', '&&', '||', '==', '!=']

    @staticmethod
    def mergeNumberType(lType, rType):
        return FloatType() if FloatType in [type(x) for x in [lType, rType]] else IntegerType()

class FType:
    """
    FType: type of function declaration
    param_type:     List[Type()]
    return_type:    List[Type()]
    """
    def __init__(self, param_type, return_type):
        self.param_type     = param_type
        self.return_type    = return_type
    
    def __str__(self):
        return 'FType([' + ','.join([str(i) for i in self.param_type]) + '],' + str(self.return_type) + ')'

class Symbol:
    """
    name: string
    mtype:  FType
            AtomicType:  IntegerType, FloatType, BooleanType, StringType
            ArrayType
            AutoType
            VoidType
    value: ???
    kind: Function() | Procedure() | Parameter() | Variable()
    isGlobal: boolean
    """

    # Default Declare Type is Function Declare - kind Function
    def __init__(self, name, ftype, value=None, kind=Function(), isGlobal: bool = False,  isInherit: bool = False):
        self.name       = name
        self.ftype      = ftype
        self.value      = value
        self.kind       = kind
        """Boolean for global symbol"""
        self.isGlobal   = isGlobal       
        self.isInherit  = isInherit 

    def __str__(self):
        return 'Symbol(' + self.name + ',' + str(self.ftype) + ',' + str(self.kind) + ')'

    def getKind(self):
        return self.kind if type(self.mtype) is FType else Identifier()

    def toTuple(self):
        """
        Return a tuple contains name and the corresponding kind
        Example:
            (asfasf, Function)
        """
        return (str(self.name).lower(), type(self.getKind()))

    def toTupleString(self):
        """
        Return a tuple contains name and corresponding type
        Example:

        """
        return (str(self.name).lower(), str(self.ftype))

    def toParam(self):
        self.kind = Parameter()
        return self

    def toVar(self):
        self.kind = Variable()
        return self

    def toGlobal(self):
        self.isGlobal = True
        return self

    def toInherit(self):
        self.toInherit = True
        return self

    # compare function between 2 instances
    @staticmethod
    def cmp(symbol):
        return str(symbol.name).lower()

    @staticmethod
    def fromParamDecl(decl: ParamDecl):
        return Symbol(decl.name, decl.typ, kind=Parameter(), isInherit=decl.inherit)

    @staticmethod
    def fromVarDecl(decl: VarDecl):
        return Symbol(decl.name, decl.typ, kind=Variable())

    @staticmethod
    def fromFuncDecl(decl: FuncDecl):
        kind = Function() 
        paramType = [x.typ for x in decl.params]
        return Symbol(decl.name, FType(paramType, decl.return_type), kind=kind)

    @staticmethod
    def fromDecl(decl):
        if type(decl) is ParamDecl:
            return Symbol.fromParamDecl(decl)
        return Symbol.fromVarDecl(decl) if type(decl) is VarDecl else Symbol.fromFuncDecl(decl)
class Scope:
    @staticmethod
    def start(section):
        # print("================   " + section + "   ================")
        pass

    @staticmethod
    def end():
        # print("=====================================================")
        pass

    @staticmethod
    def isExisten(listSymbols, symbol):
        """
        args:
            symbol: Symbol(name, ftype, kind, value)
            listSymbols: List[Symbol(name, ftype, kind, value)]
        """
        return len([x for x in listSymbols if str(x.name).lower() == str(symbol.name).lower()]) > 0

    @staticmethod
    def merge(currentScope, comingScope):
        return reduce(lambda lst, sym: lst if Scope.isExisten(lst, sym) else lst+[sym], currentScope, comingScope)

    @staticmethod
    def log(scope): [print(x) for x in scope]


class MT22Checker:
    utils = Utils()

    @staticmethod
    def checkRedeclared(current_scope, list_symbols):

        """
        Loop all the symbol in the current scope and lookup the duplicate one
        Return:
            newScope: List[Symbol] if there is no duplicate symbol
        """
        #   Copy scope
        newScope    = current_scope.copy()
        for x in list_symbols:
            
            f = MT22Checker.utils.lookup(Symbol.cmp(x), list_symbols, Symbol.cmp)

            if f is not None:
                raise Redeclared(x.kind, x.name)
            newScope.append(x)

        return newScope

    @staticmethod
    def checkUndeclared(vis_scope, name, kind, notGlobal=False):
        """
        Check the undeclared of any kind: Function/Param/Var
        Return:
            result: Tuple(kind: Kind(), name: str) 
            if a tuple(name, kind) exist in the scope

            lambda x: x.toTuple(): return (x.kind, x.name) 
            x: Symbol object
        """
        scope   = vis_scope if not notGlobal else [x for x in vis_scope if not x.isGlobal]
        result  = MT22Checker.utils.lookup((str(name), type(kind)), scope, lambda x: x.toTuple()) 
        if result is None:
            raise Undeclared(kind, name)
        return result

    @staticmethod
    def checkMatchedArrayType(a, b):
        """
        a: AST.ArrayType(dimensions, typ)
        b: AST.ArrayType(dimensions, type)
        """
        return a==b and a.typ == b.type
    
    @staticmethod
    def matchedType(pattern, param):
        pass

    @staticmethod
    def checkParamType(pattern, params):
        if len(pattern) != len(params):
            return False
        return all([MT22Checker.matchedType(a,b) for a, b in zip(pattern, params)])

    @staticmethod
    def handleReturnStmts(stmts):
        """
        stmts: List[Stmt]
        """
        return None if stmts == [] else stmts[-1][1]

    @staticmethod
    def isReturnTypeFunction(return_type):
        """// Types that functions can return
        function_type: BOOLEAN | INTEGER | FLOAT | STRING | AUTO | VOID | array_type;		
        """
        return type(return_type) in [BooleanType, IntegerType, FloatType, StringType, AutoType, VoidType, ArrayType]

    @staticmethod
    def isReturnType(return_type):
        return MT22Checker.isReturnTypeFunction(return_type)

    @staticmethod
    def isStopTypeStmt(return_type):
        return MT22Checker.isReturnType(return_type) or type(return_type) in [BreakStmt, ContinueStmt]
class Graph:
    """
        For check the unreachable statements in the code
    """
    pass
class StaticChecker(Visitor, Utils):
    glob_envs = [
        Symbol("readInteger", FType([], IntegerType())),
        Symbol("printInteger", FType([IntegerType()], VoidType(), kind = Function())),
        Symbol("readFloat", FType([], FloatType())),
        Symbol("writeFloat", FType([FloatType()], VoidType()), kind=Function()),
        Symbol("readBoolean", FType([], BooleanType())),
        Symbol("printBoolean", FType([BooleanType()], VoidType()), kind=Function()),
        Symbol("readString", FType([], StringType())) 
        Symbol("printString", FType([StringType()], VoidType()), kind=Function()),
        Symbol("super", FType([Expr()], VoidType()), kind=Function())
        Symbol("preventDefault", FType([], VoidType()), kind=Function())

    ]

    def __init__(self, astTree):
        self.astTree = astTree
    
    def check(self):
        return self.visit(self.astTree, StaticChecker.glob_envs)
    
    def visitProgram(self, ast: Program, globalEnv):
        Scope.start("Program")
        
        #   Check redeclared    Variable/Parameter/Function
        symbols = [Symbol.fromDecl(x).toGlobal() for x in ast.decls]
        scope   = MT22Checker.checkRedeclared(globalEnv, symbols)

        #   Check no entry point
        entry_point = Symbol("main", FType([], VoidType()), kind = Function())
        res         = self.lookup(entry_point.toTupleString(), symbols, lambda x: x.toTupleString())
        if res is None:
            raise NoEntryPoint()

        Scope.end()
        return [] 
    
    def visitVarDecl(self, ast: VarDecl, param): pass
    def visitParamDecl(self, ast: ParamDecl, param): pass
    def visitFuncDecl(self, ast: FuncDecl, param): pass

    #####################   Visit Types     ####################################        Done
    def visitIntegerType(self, ast, param): return IntegerType()
    def visitFloatType(self, ast, param):   return FloatType()
    def visitBooleanType(self, ast, param): return BooleanType()
    def visitStringType(self, ast, param):  return StringType()
    def visitArrayType(self, ast: ArrayType, param): 
        typ = self.visit(ast.typ, param)
        return ArrayType(ast.dimensions, typ)
    def visitAutoType(self, ast, param):    return AutoType()
    def visitVoidType(self, ast, param):    return VoidType()

    ####################    Visit Expressions and Literal   #####################
    def visitBinExpr(self, ast: BinExpr, param): 
        """
        Check type compatible for several binary operators:
        Arithmetics: + - * / % => IntegerType/FloatType
        Logical:     ||, && => IntegerType/BooleanType
        Relational:  >, <, =>, <=  --> IntegerType/FloatType
        String:     ::

        TypeMisMatchInExpression:
            *) LHS or RHS is not Int/Float if operator is arithemtics or relational
            *) LHS or RHS are not both IntType when operator is modulo %
            *) LHS and RHS are not string when operator is ::
            *) LHS or RHS are neither BooleanType when operator is [&&, ||]
            *) LHS or RHS are neither IntType/BooleanType when operator is [==, !=]
        """
        scope, func_name = param
        op = str(ast.op).lower()
        left_type   = self.visit(ast.left, (scope, func_name))          #   Get left type
        right_type  = self.visit(ast.right, (scope, func_name))         #   Get right type
        
        #   Check type compatible for number
        #   This only have the FloatType or IntegerType in both LHS and RHS
        if ExpHelper.isOpForNumber(op):                                 
            if ExpHelper.isNaNType(left_type) or ExpHelper.isNaNType(right_type):           #   LHS or RHS is not number
                raise TypeMismatchInExpression(ast)
            
            if op == '%':                                                                   #   Modulo cannot perform on floating number
                if FloatType in [type(left_type), type(right_type)]:
                    raise TypeMismatchInExpression(ast)
                return IntegerType()
            if op in ['+', '-', '*']:
                return ExpHelper.mergeNumberType(left_type, right_type)                     #   Return Float if either side is float, other wise return Int
            
            if op == '/':
                return FloatType()
            return BooleanType()

        #   Check type compatible for string
        if ExpHelper.isOpForStr(op):
            if False in [type(x) is StringType for x in [left_type, right_type]]:
                raise TypeMismatchInExpression(ast)
            return StringType()

        #   Check type compatible for boolean
        if str(op).lower() in ['&&', '||']:
            if False in [type(x) is BooleanType for x in [left_type, right_type]]:
                raise TypeMismatchInExpression(ast)
        if str(op).lower() in ['==', '!=']:
            if False in [type(x) is BooleanType or type(x) is IntegerType for x in [left_type, right_type]]:
                raise TypeMismatchInExpression(ast) 
        return BooleanType()

    def visitUnExpr(self, ast: UnExpr, param): 
        scope, func_name = param
        op = str(ast.op)
        exp_type = self.visit(ast.val, (scope, func_name))

        if op == '-':
            if ExpHelper.isNaNType(exp_type):
                raise TypeMismatchInExpression(ast)
        if op == '!':
            if type(exp_type) is not BooleanType:
                raise TypeMismatchInExpression(ast)
        if op == ',':
            if type(exp_type) is not IntegerType:
                raise TypeMismatchInExpression(ast)
        return exp_type

    def visitId(self, ast: Id, param): pass
    def visitArrayCell(self, ast: ArrayCell, param): pass
    def visitArrayLit(self, ast: ArrayLit, param): pass
    def visitFuncCall(self, ast: FuncCall, param): pass

    def visitIntegerLit(self, ast, param):  return IntegerType()
    def visitFloatLit(self, ast, param):    return FloatType()
    def visitStringLit(self, ast, param):   return StringType()
    def visitBooleanLit(self, ast, param):  return BooleanType()
    
    ###################     Visit Statements    ##################################
    def visitAssignStmt(self, ast: AssignStmt, param): pass
    def visitBlockStmt(self, ast: BlockStmt, param): pass
    def visitIfStmt(self, ast: IfStmt, param): pass
    def visitForStmt(self, ast: ForStmt, param): pass
    def visitWhileStmt(self, ast: WhileStmt, param): pass
    def visitDoWhileStmt(self, ast: DoWhileStmt, param): pass
    def visitBreakStmt(self, ast: BreakStmt, param): pass
    def visitContinueStmt(self, ast: ContinueStmt, param): pass
    def visitReturnStmt(self, ast: ReturnStmt, param): pass
    def visitCallStmt(self, ast: CallStmt, param): pass

    

    