import ply.yacc as yacc
from Tree.Tree import Tree
from Parser.lexer import LexParser


class Parser:
    tokens = LexParser().tokens

    def __init__(self):
        self.lexer = LexParser()
        self.parser = yacc.yacc(module=self)
        self.proc_names = []
        self.var_names = []
        self.errors = []

    def parse(self, d):
        result = self.parser.parse(d, debug=False)
        # print(self.errors)
        return result, self.proc_names, self.errors

    @staticmethod
    def p_program(p):
        """program : sentence_groups"""
        p[0] = Tree('Program Start', child=[p[1], Tree('Program End')], lineno=p.lineno(1))

    @staticmethod
    def p_sentence_groups(p):
        """sentence_groups : EOS OPBR EOS sentence_group CLBR EOS
                           | OPBR EOS sentence_group CLBR EOS
                           | OPBR EOS sentence_group CLBR
                           | EOS OPBR EOS sentence_group CLBR
                           | sentence"""
        if len(p) > 5:
            p[0] = p[4]
        elif len(p) > 2:
            p[0] = p[3]
        else:
            p[0] = p[1]

    @staticmethod
    def p_sentence_group(p):
        """sentence_group : sentence_group sentence
                          | sentence"""
        if len(p) == 3:
            p[0] = Tree('sentence_group', child=[p[1], p[2]], lineno=p.lineno(1))
        else:
            p[0] = p[1]

    @staticmethod
    def p_sentence(p):
        """sentence : definition EOS
                    | if
                    | while
                    | if_err
                    | while_err
                    | procedure
                    | call_procedure EOS
                    | robot_command EOS
                    | map_setting EOS
                    | error"""
        p[0] = p[1]

    @staticmethod
    def p_type(p):
        """type : INT
                | BOOLEAN"""
        p[0] = Tree('type', value=p[1], lineno=p.lineno(1))

    def p_sizeof(self, p):
        """sizeof : SIZEOF OPBR type CLBR
                  | SIZEOF OPBR VARIABLE CLBR"""
        print(p)
        if len(p) != 5:
            self.errors.append(f"Line: {p.lineno(1)} Error: specify element to getting size")
        else:
            p[0] = Tree('size of', value=p[1], child=[p[3]], lineno=p.lineno(1))

    @staticmethod
    def p_definition(p):
        """definition : type VARIABLE ASSIGN math_expr
                      | type VARIABLE ASSIGN logic_expr
                      | VARIABLE ASSIGN math_expr
                      | VARIABLE ASSIGN logic_expr
                      | MAP VARIABLE"""
        if len(p) == 5:
            p[0] = Tree('definition', value=p[1],
                        child=[Tree('variable', value=p[2], lineno=p.lineno(2)), p[4]], lineno=p.lineno(1))
        elif len(p) == 4:
            p[0] = Tree('assign', child=[Tree('variable', value=p[1], lineno=p.lineno(1)), p[3]],
                        lineno=p.lineno(1))
        else:
            p[0] = Tree('definition', value=p[1], child=[Tree('variable', value=p[2], lineno=p.lineno(2))],
                        lineno=p.lineno(1))

    @staticmethod
    def p_math_expr(p):
        """math_expr : math_first INC math_second
                     | math_first DEC math_second
                     | math_first MULT math_second
                     | math_first DIV math_second
                     | math_cmd empty
                     | VARIABLE
                     | number empty
                     | number"""
        if len(p) == 4:
            p[0] = Tree('math_expr', value=p[2], child=[p[1], p[3]], lineno=p.lineno(1))
        elif len(p) == 3:
            p[0] = p[1]
            print('ghj')
        else:
            p[0] = Tree('variable', value=p[1], lineno=p.lineno(1))

    @staticmethod
    def p_number(p):
        """number : NUM"""
        p[0] = Tree('number', value=p[1], lineno=p.lineno(1))

    @staticmethod
    def p_bool(p):
        """bool : TRUE
                | FALSE"""
        p[0] = Tree('bool', value=p[1], lineno=p.lineno(1))

    @staticmethod
    def p_math_first(p):
        """math_first : math_expr
                     | call_procedure"""
        p[0] = p[1]

    @staticmethod
    def p_math_second(p):
        """math_second : math_first
                      | logic_expr"""
        p[0] = p[1]

    @staticmethod
    def p_logic_expr(p):
        """logic_expr : NOT logic_expr
                      | NOT call_procedure
                      | or_elem OR or_elem
                      | math_expr EQUAL math_expr
                      | logic_expr EQUAL logic_expr
                      | math_expr GT math_expr
                      | math_expr LT math_expr
                      | logic_cmd
                      | bool"""
        if len(p) == 3:
            p[0] = Tree('logic_expr', value=p[1], child=[p[2]], lineno=p.lineno(1))
        elif len(p) == 4:
            p[0] = Tree('logic_expr', value=p[2], child=[p[1], p[3]], lineno=p.lineno(1))
        else:
            p[0] = p[1]

    @staticmethod
    def p_or_elem(p):
        """or_elem : logic_expr
                   | call_procedure"""
        p[0] = p[1]

    def p_procedure(self, p):
        """procedure : PROC VARIABLE OPSQBR varlist CLSQBR sentence_groups"""
        if p[2] not in self.proc_names:
            self.proc_names.append(p[2])
        else:
            # sys.stderr.write("Error procedure with same name already declared")
            self.errors.append(f"Line: {p.lineno(1)} Error: Procedure '{p[1]}' already declared")
        p[0] = Tree('procedure', value=p[2], child=[p[4], p[6]], lineno=p.lineno(1))

    def p_call_procedure(self, p):
        """call_procedure : VARIABLE OPSQBR varlist CLSQBR"""
        if p[1] not in self.proc_names:
            # sys.stderr.write("Error procedure wasn't declared")
            self.errors.append(f"Line: {p.lineno(1)} Error: Procedure '{p[1]}' wasn't declared")
        p[0] = Tree('call_procedure', value=p[1], child=[p[3]], lineno=p.lineno(1))

    @staticmethod
    def p_varlist(p):
        """varlist : varlist VARIABLE
                   | VARIABLE"""
        if len(p) == 3:
            p[0] = Tree('varlist', child=[p[1], Tree('variable', value=p[2], lineno=p.lineno(1))],
                        lineno=p.lineno(1))
        else:
            p[0] = Tree('variable', value=p[1], lineno=p.lineno(1))

    def p_if_err(self, p):
        """if_err : IF error sentence_groups ELSE sentence_groups
                  | IF error sentence_groups"""
        self.errors.append(f"Line: {p.lineno(2)} Error: Wrong IF condition: {p[2].value}")
        if len(p) == 5:
            p[0] = Tree('er_if_else', lineno=p.lineno(1))
        else:
            p[0] = Tree('er_if', lineno=p.lineno(1))

    def p_while_err(self, p):
        """while_err : WHILE error DO sentence_groups
                     | WHILE error"""
        if len(p) == 5:
            self.errors.append(f"Line: {p.lineno(2)} Error: Wrong WHILE condition: {p[2].value}")
            p[0] = Tree('while_err', child=[p[4]], lineno=p.lineno(1))
        else:
            self.errors.append(f"Line: {p.lineno(2)} Error: Wrong WHILE declaration: {p[2].value}")
            p[0] = Tree('while_err', lineno=p.lineno(1))

    @staticmethod
    def p_if(p):
        """if : IF logic_expr sentence_groups ELSE sentence_groups
              | IF logic_expr sentence_groups"""
        if len(p) == 5:
            p[0] = Tree('if_else', child=[p[2], p[3], p[5]], lineno=p.lineno(1))
        else:
            p[0] = Tree('if', child=[p[2], p[3]], lineno=p.lineno(1))

    @staticmethod
    def p_while(p):
        """while : WHILE logic_expr DO sentence_groups"""
        p[0] = Tree('while', child=[p[2], p[4]], lineno=p.lineno(1))

    @staticmethod
    def p_robot_command(p):
        """robot_command : logic_cmd
                         | rot_dir
                         | math_cmd"""
        p[0] = p[1]

    @staticmethod
    def p_rot_dir(p):
        """rot_dir : BACK
                   | RIGHT
                   | LEFT"""
        p[0] = Tree('cmd_rot', value=p[1], lineno=p.lineno(1))

    @staticmethod
    def p_logic_cmd(p):
        """logic_cmd : STEP"""
        p[0] = Tree('cmd_step', value=p[1], lineno=p.lineno(1))

    @staticmethod
    def p_math_cmd(p):
        """math_cmd : LOOK"""
        p[0] = Tree('cmd_look', value=p[1], lineno=p.lineno(1))

    @staticmethod
    def p_map_setting(p):
        """map_setting : BAR OPSQBR VARIABLE VARIABLE math_expr math_expr CLSQBR
                        | EMP OPSQBR VARIABLE VARIABLE math_expr math_expr CLSQBR
                        | SET OPSQBR VARIABLE VARIABLE math_expr math_expr CLSQBR
                        | CLR OPSQBR VARIABLE VARIABLE math_expr math_expr CLSQBR"""
        p[0] = Tree('map_setting', value=p[1], child=[Tree('variable', value=p[3], lineno=p.lineno(3)),
                                                      Tree('variable', value=p[4], lineno=p.lineno(4)), p[5],
                                                      p[6]], lineno=p.lineno(1))

    # @staticmethod
    # def p_print(self, p):
    #     """print : PRINT math_expr
    #              | PRINT logic_expr
    #              | PRINT VARIABLE"""
    #     if len(p) == 3:
    #         p[0] = Tree('print', value=p[1], child=p[2], lineno=p.lineno(1))

    def p_empty(self, p):
        """empty :"""
        pass

    def p_error(self, p):
        try:
            # sys.stderr.write(f"Unknown Error on {p.lineno} line Token: {p}\n")
            self.errors.append(f"Line: {p.lineno(0)} Error: Wrong syntax expression '{p[0].value}' ")
        except Exception as e:
            print(e)
            # sys.stderr.write(f"Unknown ERROR {p}")
            self.errors.append(f"Line: {p.lineno} Error: Wrong syntax expression '{p.value}'")


if __name__ == '__main__':
    with open('check.txt', 'r') as f:
        data = f.read()
    parser = Parser()
    res, proc_names, errors = parser.parse(data)
    print(res)
    print(errors)
