from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *


class ASTGeneration(MT22Visitor):
    
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        return Program([])

    def visitDecl(self, ctx:MT22Parser.DeclContext):
        return self.visitChildren(ctx)

    def visitAtomic_type(self, ctx: MT22Parser.Atomic_typeContext):
       
        if ctx.BOOLEAN():   return BooleanType()
        if ctx.INTEGER():   return IntegerType()
        if ctx.FLOAT()  :   return FloatType()
        if ctx.STRING() :   return StringType()

    def visitFunction_type(self, ctx: MT22Parser.Function_typeContext):
        
        if ctx.BOOLEAN()    :   return BooleanType()
        if ctx.INTEGER()    :   return IntegerType()
        if ctx.FLOAT()      :   return FloatType()
        if ctx.STRING()     :   return StringType()
        if ctx.AUTO()       :   return AutoType()
        if ctx.VOID()       :   return VoidType()
        if ctx.array_type() :   return ctx.array_type().accept(self)
        
    def visitInclude_auto_type(self, ctx: MT22Parser.Include_auto_typeContext):
        
        if ctx.BOOLEAN()    :   return BooleanType()
        if ctx.INTEGER()    :   return IntegerType()
        if ctx.FLOAT()      :   return FloatType()
        if ctx.STRING()     :   return StringType()
        if ctx.AUTO()       :   return AutoType()
        if ctx.array_type() :   return ctx.array_type().accept(self)

    def visitVardecl(self, ctx: MT22Parser.VardeclContext):        
        pass

    # def visitFull_format_decl(self, ctx: MT22Parser.Full_format_declContext):
    #     pass

    def visitList_of_ids(self, ctx: MT22Parser.List_of_idsContext):
        if ctx.another_id_list():
            return [Id(ctx.IDENTIFIERS().getText())] + ctx.another_id_list().accept(self)
        return [Id(ctx.IDENTIFIERS().getText())]

    def visitAnother_id_list(self, ctx: MT22Parser.Another_id_listContext):
        return ctx.list_of_ids().accept(self)    

    def visitArray_type(self, ctx: MT22Parser.Array_typeContext):
        return ArrayType(ctx.dimensions().accept(self), ctx.atomic_type().accept(self))

    def visitDimensions(self, ctx: MT22Parser.DimensionsContext):
        if ctx.COMMA():
            return [ctx.INTLIT().getText()] + ctx.dimensions().accept(self)
        return [ctx.INTLIT().getText()]

    def visitArray_literal(self, ctx: MT22Parser.Array_literalContext):
        return ArrayLit(ctx.expr_list().accept(self))

    def visitExpr_list(self, ctx: MT22Parser.Expr_listContext) -> list():
        if ctx.list_of_exprs():
            return ctx.list_of_exprs().accept(self)
        return []

    def visitList_of_exprs(self, ctx: MT22Parser.List_of_exprsContext) -> list():
        if ctx.list_of_exprs():
            return [ctx.expr().accept(self)] + ctx.list_of_exprs().accept(self)
        return [ctx.expr().accept(self)]

    def visitArray_indexing(self, ctx: MT22Parser.Array_indexingContext):
        return ArrayCell(ctx.IDENTIFIERS().getText(), ctx.indexop_expr().accept(self))

    def visitIndexop_expr(self, ctx: MT22Parser.Indexop_exprContext) -> list():
        if ctx.indexop_expr:
            return [ctx.expr().accept(self)] + ctx.indexop_expr().accept(self)
        return [ctx.expr().accept(self)]
    
    def visitFuncdecl(self, ctx: MT22Parser.FuncdeclContext):
        pass

    def visitFunction_prototype(self, ctx: MT22Parser.Function_prototypeContext):
        if ctx.INHERIT():
            ans = [
                ctx.IDENTIFIERS(0).getText(),
                ctx.function_type().accept(self),
                ctx.func_params().accept(self),
                ctx.INHERIT().getText(),
                ctx.IDENTIFIERS(1).getText(),
            ]
        return  [
                ctx.IDENTIFIERS().getText(),
                ctx.function_type().accept(self),
                ctx.func_params().accept(self),
                ctx.INHERIT().getText(),
            ]
            
    def visitFunction_body(self, ctx: MT22Parser.Function_bodyContext):
        return ctx.block_statement().accept(self)

    def visitFunc_params(self, ctx: MT22Parser.Func_paramsContext) -> list():
        if ctx.paramlist():
            return ctx.paramlist().accept(self)
        return []

    def visitParamlist(self, ctx: MT22Parser.ParamlistContext) -> list():
        if ctx.COMMA():
            return [ctx.paramone().accept(self)] + ctx.paramlist().accept(self)
        return [ctx.paramone().accept(self)]

    def visitParamone(self, ctx: MT22Parser.ParamoneContext):
        pass

    def visitFunction_call(self, ctx: MT22Parser.Function_callContext):
        return FuncCall(ctx.IDENTIFIERS().getText(), ctx.arg_list().accept(self))

    def visitArg_list(self, ctx: MT22Parser.Arg_listContext) -> list:
        if ctx.arg_list_params():
            return ctx.arg_list_params().accept(self)
        return []

    def visitArg_list_params(self, ctx: MT22Parser.Arg_list_paramsContext):
        pass

    def visitLiteral(self, ctx: MT22Parser.LiteralContext):
        if ctx.array_literal(): return ctx.array_literal().accept(self)
        if ctx.INTLIT():        return IntegerLit(int(ctx.INTLIT().getText()))
        if ctx.FLOATLIT():      return FloatLit(float(ctx.FLOATLIT().getText()))
        if ctx.INTLIT():        return BooleanLit(bool(ctx.BOOLIT().getText()))  
        if ctx.INTLIT():        return StringLit(str(ctx.STRINGLIT().getText()))
    
    def visitSub_expr(self, ctx: MT22Parser.Sub_exprContext):
        return ctx.sub_expr().accept(self)

    # def visitExpr(self, ctx: MT22Parser.ExprContext):
    #     pass

    # def visitExpr1(self, ctx: MT22Parser.Expr1Context):
    #     pass
    
    # def visitExpr2(self, ctx: MT22Parser.Expr2Context):
    #     pass

    # def visitExpr3(self, ctx: MT22Parser.Expr3Context):
    #     pass
    
    # def visitExpr4(self, ctx: MT22Parser.Expr4Context):
    #     pass
    
    # def visitExpr5(self, ctx: MT22Parser.Expr5Context):
    #     pass

    # def visitExpr6(self, ctx: MT22Parser.Expr6Context):
    #     pass

    # def visitExpr7(self, ctx: MT22Parser.Expr7Context):
    #     pass

    def visitStmt(self, ctx: MT22Parser.StmtContext):
        return ctx.getChild().accept(self)

    def visitNoblock_statement(self, ctx: MT22Parser.Noblock_statementContext):
        return ctx.getChild().accept(self)

    def visitAssign_statement(self, ctx: MT22Parser.Assign_statementContext):
        pass

    def visitIf_statement(self, ctx: MT22Parser.If_statementContext):
        pass
    
    def visitFor_statement(self, ctx: MT22Parser.For_statementContext):
        pass

    def visitWhile_statement(self, ctx: MT22Parser.While_statementContext):
        pass

    def visitDo_while_statement(self, ctx: MT22Parser.Do_while_statementContext):
        pass
    
    def visitBreak_statement(self, ctx: MT22Parser.Break_statementContext):
        return ctx.BREAK().getText()

    def visitContinue_statement(self, ctx:  MT22Parser.Continue_statementContext):
        return ctx.CONTINUE().getText()

    def visitReturn_statement(self, ctx: MT22Parser.Return_statementContext):
        return ReturnStmt(ctx.expr().accept(self))

    def visitBlock_statement(self, ctx: MT22Parser.Block_statementContext):
        ans = []

        return ans

    def visitCall_statement(self, ctx: MT22Parser.Call_statementContext):
        return 

