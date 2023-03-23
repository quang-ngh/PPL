from Visitor import Visitor
from StaticError import *
from AST import *
from Utils import Utils
from functools import reduce
import sys

sys.path.append('../../../../target/main/mp/parser')

class StaticChecker(Visitor, Utils):
    glob_envs = []

    def __init__(self, astTree):
        self.astTree = astTree
    
    def check(self):
        Checker.init()
        return self.visit(self.astTree, StaticChecker.glob_envs)
    
    def visitProgram(self, ast):
        pass
    
    ###################     VISIT TYPES     #################
    def visitIntegerType(self, ast):
        pass

    def visitFloatType(self, ast):
        pass
    
    def visitBooleanType(self, ast):
        pass

    def visitStringType(self, ast):
        pass
        
    def visitArrayType(self, ast):
        pass

    def visitAutoType(self, ast):
        pass

    def visitVoidType(self, ast):
        pass
    ###########################################################

    """ Visit Expressions """
    def visitBinExpr(self, ast):
        pass

    def visitUnExpr(self, ast):
        pass

    def visitId(self, ast):
        pass

    def visitArrayCell(self, ast):
        pass

    def visitIntegerLit(self, ast):
        pass

    def visitFloatLit(self, ast):
        pass

    def visitStringLit(self, ast):
        pass

    def visitBooleanLit(self, ast):
        pass

    def visitArrayLit(self, ast):
        pass

    def visitFuncCall(self, ast):
        pass

    """ Visit Statements """
    def visitAssignStmt(self, ast):
        pass

    def visitBlockStmt(self, ast):
        pass

    def visitIfStmt(self, ast):
        pass

    def visitForStmt(self, ast):
        pass

    def visitWhileStmt(self, ast):
        pass

    def visitDoWhileStmt(self, ast):
        pass

    def visitBreakStmt(self, ast):
        pass

    def visitContinueStmt(self, ast):
        pass

    def visitReturnStmt(self, ast):
        pass

    def visitCallStmt(self, ast):
        pass

    """ Visit Declarations """
    def visitVarDecl(self, ast):
        pass
    
    def visitParamDecl(self, ast):
        pass

    def visitFuncDecl(self, ast):
        pass