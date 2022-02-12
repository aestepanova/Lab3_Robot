
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASSIGN BACK BAR BOOLEAN CBOOLEAN CINT CLBR CLR CLSQBR DEC DO ELSE EMP EOS EQUAL FALSE GT IF INC INT LEFT LOOK LT MAP NOT NUM OPBR OPSQBR OR PROC RIGHT SET STEP TRUE VARIABLE WHILEprogram : sentence_groupssentence_groups : EOS OPBR EOS sentence_group CLBR EOS\n                           | OPBR EOS sentence_group CLBR EOS\n                           | OPBR EOS sentence_group CLBR\n                           | EOS OPBR EOS sentence_group CLBR\n                           | sentencesentence_group : sentence_group sentence\n                          | sentencesentence : definition EOS\n                    | if\n                    | while\n                    | if_err\n                    | while_err\n                    | procedure\n                    | call_procedure EOS\n                    | robot_command EOS\n                    | map_setting EOS\n                    | errordefinition : INT VARIABLE EQUAL math_expr\n                      | CINT VARIABLE EQUAL math_expr\n                      | BOOLEAN VARIABLE EQUAL logic_expr\n                      | CBOOLEAN VARIABLE EQUAL logic_expr\n                      | VARIABLE ASSIGN math_expr\n                      | VARIABLE ASSIGN logic_expr\n                      | MAP VARIABLEmath_expr : INC math_first math_second\n                     | DEC math_first math_second\n                     | math_cmd empty\n                     | VARIABLE\n                     | number emptynumber : NUMbool : TRUE\n                | FALSEmath_first : math_expr\n                     | call_proceduremath_second : math_first\n                      | logic_exprlogic_expr : NOT logic_expr\n                      | NOT call_procedure\n                      | OR or_elem or_elem\n                      | GT math_expr math_expr\n                      | LT math_expr math_expr\n                      | logic_cmd\n                      | boolor_elem : logic_expr\n                   | call_procedureprocedure : PROC VARIABLE OPSQBR varlist CLSQBR sentence_groupscall_procedure : VARIABLE OPSQBR varlist CLSQBRvarlist : varlist VARIABLE\n                   | VARIABLEif_err : IF error sentence_groups ELSE sentence_groups\n              | IF error sentence_groupswhile_err : WHILE error DO sentence_groups\n                 | WHILE errorif : IF logic_expr sentence_groups ELSE sentence_groups\n              | IF logic_expr sentence_groupswhile : WHILE logic_expr DO sentence_groupsrobot_command : logic_cmd\n                         | rot_dir\n                         | math_cmdrot_dir : BACK\n                   | RIGHT\n                   | LEFTlogic_cmd : STEPmath_cmd : LOOKmap_setting : BAR OPSQBR VARIABLE VARIABLE math_expr math_expr CLSQBR\n                        | EMP OPSQBR VARIABLE VARIABLE math_expr math_expr CLSQBR\n                        | SET OPSQBR VARIABLE VARIABLE math_expr math_expr CLSQBR\n                        | CLR OPSQBR VARIABLE VARIABLE math_expr math_expr CLSQBRempty :'
    
_lr_action_items = {'EOS':([0,4,6,12,13,14,25,26,27,32,33,34,35,36,37,49,50,51,56,57,58,59,71,72,73,76,77,78,86,87,90,91,94,95,102,104,106,107,108,110,111,113,114,115,116,117,118,119,120,121,129,131,132,133,134,137,148,149,150,151,],[3,38,39,40,41,42,-58,-59,-60,-64,-61,-62,-63,-65,67,-25,3,3,-43,-44,-32,-33,-29,-23,-24,-70,-70,-31,-38,-39,-45,-46,3,3,130,-19,-34,-35,-29,-28,-30,-48,-20,-21,-22,3,3,-40,-41,-42,142,-36,-26,-37,-27,3,-66,-67,-68,-69,]),'OPBR':([0,3,32,36,50,51,56,57,58,59,71,76,77,78,86,87,90,91,94,95,106,107,108,110,111,113,117,118,119,120,121,131,132,133,134,137,],[4,37,-64,-65,4,4,-43,-44,-32,-33,-29,-70,-70,-31,-38,-39,-45,-46,4,4,-34,-35,-29,-28,-30,-48,4,4,-40,-41,-42,-36,-26,-37,-27,4,]),'error':([0,5,7,8,9,10,11,15,22,23,32,36,38,39,40,41,42,50,51,56,57,58,59,61,67,68,69,71,76,77,78,84,85,86,87,90,91,94,95,101,102,103,106,107,108,110,111,113,117,118,119,120,121,122,123,129,130,131,132,133,134,135,136,137,142,143,],[15,-6,-10,-11,-12,-13,-14,-18,51,61,-64,-65,15,-9,-15,-16,-17,15,15,-43,-44,-32,-33,-54,15,15,-8,-29,-70,-70,-31,-56,-52,-38,-39,-45,-46,15,15,15,-4,-7,-34,-35,-29,-28,-30,-48,15,15,-40,-41,-42,-57,-53,-5,-3,-36,-26,-37,-27,-55,-51,15,-2,-47,]),'INT':([0,5,7,8,9,10,11,15,32,36,38,39,40,41,42,50,51,56,57,58,59,61,67,68,69,71,76,77,78,84,85,86,87,90,91,94,95,101,102,103,106,107,108,110,111,113,117,118,119,120,121,122,123,129,130,131,132,133,134,135,136,137,142,143,],[16,-6,-10,-11,-12,-13,-14,-18,-64,-65,16,-9,-15,-16,-17,16,16,-43,-44,-32,-33,-54,16,16,-8,-29,-70,-70,-31,-56,-52,-38,-39,-45,-46,16,16,16,-4,-7,-34,-35,-29,-28,-30,-48,16,16,-40,-41,-42,-57,-53,-5,-3,-36,-26,-37,-27,-55,-51,16,-2,-47,]),'CINT':([0,5,7,8,9,10,11,15,32,36,38,39,40,41,42,50,51,56,57,58,59,61,67,68,69,71,76,77,78,84,85,86,87,90,91,94,95,101,102,103,106,107,108,110,111,113,117,118,119,120,121,122,123,129,130,131,132,133,134,135,136,137,142,143,],[18,-6,-10,-11,-12,-13,-14,-18,-64,-65,18,-9,-15,-16,-17,18,18,-43,-44,-32,-33,-54,18,18,-8,-29,-70,-70,-31,-56,-52,-38,-39,-45,-46,18,18,18,-4,-7,-34,-35,-29,-28,-30,-48,18,18,-40,-41,-42,-57,-53,-5,-3,-36,-26,-37,-27,-55,-51,18,-2,-47,]),'BOOLEAN':([0,5,7,8,9,10,11,15,32,36,38,39,40,41,42,50,51,56,57,58,59,61,67,68,69,71,76,77,78,84,85,86,87,90,91,94,95,101,102,103,106,107,108,110,111,113,117,118,119,120,121,122,123,129,130,131,132,133,134,135,136,137,142,143,],[19,-6,-10,-11,-12,-13,-14,-18,-64,-65,19,-9,-15,-16,-17,19,19,-43,-44,-32,-33,-54,19,19,-8,-29,-70,-70,-31,-56,-52,-38,-39,-45,-46,19,19,19,-4,-7,-34,-35,-29,-28,-30,-48,19,19,-40,-41,-42,-57,-53,-5,-3,-36,-26,-37,-27,-55,-51,19,-2,-47,]),'CBOOLEAN':([0,5,7,8,9,10,11,15,32,36,38,39,40,41,42,50,51,56,57,58,59,61,67,68,69,71,76,77,78,84,85,86,87,90,91,94,95,101,102,103,106,107,108,110,111,113,117,118,119,120,121,122,123,129,130,131,132,133,134,135,136,137,142,143,],[20,-6,-10,-11,-12,-13,-14,-18,-64,-65,20,-9,-15,-16,-17,20,20,-43,-44,-32,-33,-54,20,20,-8,-29,-70,-70,-31,-56,-52,-38,-39,-45,-46,20,20,20,-4,-7,-34,-35,-29,-28,-30,-48,20,20,-40,-41,-42,-57,-53,-5,-3,-36,-26,-37,-27,-55,-51,20,-2,-47,]),'VARIABLE':([0,5,7,8,9,10,11,15,16,18,19,20,21,24,32,36,38,39,40,41,42,44,45,50,51,52,53,54,55,56,57,58,59,61,63,64,65,66,67,68,69,70,71,74,75,76,77,78,79,80,81,84,85,86,87,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,105,106,107,108,109,110,111,112,113,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,],[17,-6,-10,-11,-12,-13,-14,-18,43,46,47,48,49,62,-64,-65,17,-9,-15,-16,-17,71,79,17,17,88,88,71,71,-43,-44,-32,-33,-54,97,98,99,100,17,17,-8,71,-29,108,108,-70,-70,-31,-50,112,71,-56,-52,-38,-39,88,-45,-46,71,71,17,17,79,125,126,127,128,17,-4,-7,108,-34,-35,-29,108,-28,-30,-49,-48,17,17,-40,-41,-42,-57,-53,112,71,71,71,71,-5,-3,-36,-26,-37,-27,-55,-51,17,71,71,71,71,-2,-47,]),'MAP':([0,5,7,8,9,10,11,15,32,36,38,39,40,41,42,50,51,56,57,58,59,61,67,68,69,71,76,77,78,84,85,86,87,90,91,94,95,101,102,103,106,107,108,110,111,113,117,118,119,120,121,122,123,129,130,131,132,133,134,135,136,137,142,143,],[21,-6,-10,-11,-12,-13,-14,-18,-64,-65,21,-9,-15,-16,-17,21,21,-43,-44,-32,-33,-54,21,21,-8,-29,-70,-70,-31,-56,-52,-38,-39,-45,-46,21,21,21,-4,-7,-34,-35,-29,-28,-30,-48,21,21,-40,-41,-42,-57,-53,-5,-3,-36,-26,-37,-27,-55,-51,21,-2,-47,]),'IF':([0,5,7,8,9,10,11,15,32,36,38,39,40,41,42,50,51,56,57,58,59,61,67,68,69,71,76,77,78,84,85,86,87,90,91,94,95,101,102,103,106,107,108,110,111,113,117,118,119,120,121,122,123,129,130,131,132,133,134,135,136,137,142,143,],[22,-6,-10,-11,-12,-13,-14,-18,-64,-65,22,-9,-15,-16,-17,22,22,-43,-44,-32,-33,-54,22,22,-8,-29,-70,-70,-31,-56,-52,-38,-39,-45,-46,22,22,22,-4,-7,-34,-35,-29,-28,-30,-48,22,22,-40,-41,-42,-57,-53,-5,-3,-36,-26,-37,-27,-55,-51,22,-2,-47,]),'WHILE':([0,5,7,8,9,10,11,15,32,36,38,39,40,41,42,50,51,56,57,58,59,61,67,68,69,71,76,77,78,84,85,86,87,90,91,94,95,101,102,103,106,107,108,110,111,113,117,118,119,120,121,122,123,129,130,131,132,133,134,135,136,137,142,143,],[23,-6,-10,-11,-12,-13,-14,-18,-64,-65,23,-9,-15,-16,-17,23,23,-43,-44,-32,-33,-54,23,23,-8,-29,-70,-70,-31,-56,-52,-38,-39,-45,-46,23,23,23,-4,-7,-34,-35,-29,-28,-30,-48,23,23,-40,-41,-42,-57,-53,-5,-3,-36,-26,-37,-27,-55,-51,23,-2,-47,]),'PROC':([0,5,7,8,9,10,11,15,32,36,38,39,40,41,42,50,51,56,57,58,59,61,67,68,69,71,76,77,78,84,85,86,87,90,91,94,95,101,102,103,106,107,108,110,111,113,117,118,119,120,121,122,123,129,130,131,132,133,134,135,136,137,142,143,],[24,-6,-10,-11,-12,-13,-14,-18,-64,-65,24,-9,-15,-16,-17,24,24,-43,-44,-32,-33,-54,24,24,-8,-29,-70,-70,-31,-56,-52,-38,-39,-45,-46,24,24,24,-4,-7,-34,-35,-29,-28,-30,-48,24,24,-40,-41,-42,-57,-53,-5,-3,-36,-26,-37,-27,-55,-51,24,-2,-47,]),'BAR':([0,5,7,8,9,10,11,15,32,36,38,39,40,41,42,50,51,56,57,58,59,61,67,68,69,71,76,77,78,84,85,86,87,90,91,94,95,101,102,103,106,107,108,110,111,113,117,118,119,120,121,122,123,129,130,131,132,133,134,135,136,137,142,143,],[28,-6,-10,-11,-12,-13,-14,-18,-64,-65,28,-9,-15,-16,-17,28,28,-43,-44,-32,-33,-54,28,28,-8,-29,-70,-70,-31,-56,-52,-38,-39,-45,-46,28,28,28,-4,-7,-34,-35,-29,-28,-30,-48,28,28,-40,-41,-42,-57,-53,-5,-3,-36,-26,-37,-27,-55,-51,28,-2,-47,]),'EMP':([0,5,7,8,9,10,11,15,32,36,38,39,40,41,42,50,51,56,57,58,59,61,67,68,69,71,76,77,78,84,85,86,87,90,91,94,95,101,102,103,106,107,108,110,111,113,117,118,119,120,121,122,123,129,130,131,132,133,134,135,136,137,142,143,],[29,-6,-10,-11,-12,-13,-14,-18,-64,-65,29,-9,-15,-16,-17,29,29,-43,-44,-32,-33,-54,29,29,-8,-29,-70,-70,-31,-56,-52,-38,-39,-45,-46,29,29,29,-4,-7,-34,-35,-29,-28,-30,-48,29,29,-40,-41,-42,-57,-53,-5,-3,-36,-26,-37,-27,-55,-51,29,-2,-47,]),'SET':([0,5,7,8,9,10,11,15,32,36,38,39,40,41,42,50,51,56,57,58,59,61,67,68,69,71,76,77,78,84,85,86,87,90,91,94,95,101,102,103,106,107,108,110,111,113,117,118,119,120,121,122,123,129,130,131,132,133,134,135,136,137,142,143,],[30,-6,-10,-11,-12,-13,-14,-18,-64,-65,30,-9,-15,-16,-17,30,30,-43,-44,-32,-33,-54,30,30,-8,-29,-70,-70,-31,-56,-52,-38,-39,-45,-46,30,30,30,-4,-7,-34,-35,-29,-28,-30,-48,30,30,-40,-41,-42,-57,-53,-5,-3,-36,-26,-37,-27,-55,-51,30,-2,-47,]),'CLR':([0,5,7,8,9,10,11,15,32,36,38,39,40,41,42,50,51,56,57,58,59,61,67,68,69,71,76,77,78,84,85,86,87,90,91,94,95,101,102,103,106,107,108,110,111,113,117,118,119,120,121,122,123,129,130,131,132,133,134,135,136,137,142,143,],[31,-6,-10,-11,-12,-13,-14,-18,-64,-65,31,-9,-15,-16,-17,31,31,-43,-44,-32,-33,-54,31,31,-8,-29,-70,-70,-31,-56,-52,-38,-39,-45,-46,31,31,31,-4,-7,-34,-35,-29,-28,-30,-48,31,31,-40,-41,-42,-57,-53,-5,-3,-36,-26,-37,-27,-55,-51,31,-2,-47,]),'STEP':([0,5,7,8,9,10,11,15,22,23,32,36,38,39,40,41,42,44,50,51,52,53,56,57,58,59,61,67,68,69,71,76,77,78,82,83,84,85,86,87,89,90,91,94,95,101,102,103,105,106,107,108,109,110,111,113,117,118,119,120,121,122,123,129,130,131,132,133,134,135,136,137,142,143,],[32,-6,-10,-11,-12,-13,-14,-18,32,32,-64,-65,32,-9,-15,-16,-17,32,32,32,32,32,-43,-44,-32,-33,-54,32,32,-8,-29,-70,-70,-31,32,32,-56,-52,-38,-39,32,-45,-46,32,32,32,-4,-7,32,-34,-35,-29,32,-28,-30,-48,32,32,-40,-41,-42,-57,-53,-5,-3,-36,-26,-37,-27,-55,-51,32,-2,-47,]),'BACK':([0,5,7,8,9,10,11,15,32,36,38,39,40,41,42,50,51,56,57,58,59,61,67,68,69,71,76,77,78,84,85,86,87,90,91,94,95,101,102,103,106,107,108,110,111,113,117,118,119,120,121,122,123,129,130,131,132,133,134,135,136,137,142,143,],[33,-6,-10,-11,-12,-13,-14,-18,-64,-65,33,-9,-15,-16,-17,33,33,-43,-44,-32,-33,-54,33,33,-8,-29,-70,-70,-31,-56,-52,-38,-39,-45,-46,33,33,33,-4,-7,-34,-35,-29,-28,-30,-48,33,33,-40,-41,-42,-57,-53,-5,-3,-36,-26,-37,-27,-55,-51,33,-2,-47,]),'RIGHT':([0,5,7,8,9,10,11,15,32,36,38,39,40,41,42,50,51,56,57,58,59,61,67,68,69,71,76,77,78,84,85,86,87,90,91,94,95,101,102,103,106,107,108,110,111,113,117,118,119,120,121,122,123,129,130,131,132,133,134,135,136,137,142,143,],[34,-6,-10,-11,-12,-13,-14,-18,-64,-65,34,-9,-15,-16,-17,34,34,-43,-44,-32,-33,-54,34,34,-8,-29,-70,-70,-31,-56,-52,-38,-39,-45,-46,34,34,34,-4,-7,-34,-35,-29,-28,-30,-48,34,34,-40,-41,-42,-57,-53,-5,-3,-36,-26,-37,-27,-55,-51,34,-2,-47,]),'LEFT':([0,5,7,8,9,10,11,15,32,36,38,39,40,41,42,50,51,56,57,58,59,61,67,68,69,71,76,77,78,84,85,86,87,90,91,94,95,101,102,103,106,107,108,110,111,113,117,118,119,120,121,122,123,129,130,131,132,133,134,135,136,137,142,143,],[35,-6,-10,-11,-12,-13,-14,-18,-64,-65,35,-9,-15,-16,-17,35,35,-43,-44,-32,-33,-54,35,35,-8,-29,-70,-70,-31,-56,-52,-38,-39,-45,-46,35,35,35,-4,-7,-34,-35,-29,-28,-30,-48,35,35,-40,-41,-42,-57,-53,-5,-3,-36,-26,-37,-27,-55,-51,35,-2,-47,]),'LOOK':([0,5,7,8,9,10,11,15,32,36,38,39,40,41,42,44,50,51,54,55,56,57,58,59,61,67,68,69,70,71,74,75,76,77,78,81,84,85,86,87,90,91,92,93,94,95,101,102,103,105,106,107,108,109,110,111,113,117,118,119,120,121,122,123,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,],[36,-6,-10,-11,-12,-13,-14,-18,-64,-65,36,-9,-15,-16,-17,36,36,36,36,36,-43,-44,-32,-33,-54,36,36,-8,36,-29,36,36,-70,-70,-31,36,-56,-52,-38,-39,-45,-46,36,36,36,36,36,-4,-7,36,-34,-35,-29,36,-28,-30,-48,36,36,-40,-41,-42,-57,-53,36,36,36,36,-5,-3,-36,-26,-37,-27,-55,-51,36,36,36,36,36,-2,-47,]),'$end':([1,2,5,7,8,9,10,11,15,39,40,41,42,61,84,85,102,122,123,129,130,135,136,142,143,],[0,-1,-6,-10,-11,-12,-13,-14,-18,-9,-15,-16,-17,-54,-56,-52,-4,-57,-53,-5,-3,-55,-51,-2,-47,]),'ELSE':([5,7,8,9,10,11,15,39,40,41,42,61,84,85,102,122,123,129,130,135,136,142,143,],[-6,-10,-11,-12,-13,-14,-18,-9,-15,-16,-17,-54,117,118,-4,-57,-53,-5,-3,-55,-51,-2,-47,]),'CLBR':([5,7,8,9,10,11,15,39,40,41,42,61,68,69,84,85,101,102,103,122,123,129,130,135,136,142,143,],[-6,-10,-11,-12,-13,-14,-18,-9,-15,-16,-17,-54,102,-8,-56,-52,129,-4,-7,-57,-53,-5,-3,-55,-51,-2,-47,]),'ASSIGN':([17,],[44,]),'OPSQBR':([17,28,29,30,31,62,88,108,],[45,63,64,65,66,96,45,45,]),'NOT':([22,23,32,36,44,52,53,56,57,58,59,71,76,77,78,82,83,86,87,89,90,91,105,106,107,108,109,110,111,113,119,120,121,131,132,133,134,],[52,52,-64,-65,52,52,52,-43,-44,-32,-33,-29,-70,-70,-31,52,52,-38,-39,52,-45,-46,52,-34,-35,-29,52,-28,-30,-48,-40,-41,-42,-36,-26,-37,-27,]),'OR':([22,23,32,36,44,52,53,56,57,58,59,71,76,77,78,82,83,86,87,89,90,91,105,106,107,108,109,110,111,113,119,120,121,131,132,133,134,],[53,53,-64,-65,53,53,53,-43,-44,-32,-33,-29,-70,-70,-31,53,53,-38,-39,53,-45,-46,53,-34,-35,-29,53,-28,-30,-48,-40,-41,-42,-36,-26,-37,-27,]),'GT':([22,23,32,36,44,52,53,56,57,58,59,71,76,77,78,82,83,86,87,89,90,91,105,106,107,108,109,110,111,113,119,120,121,131,132,133,134,],[54,54,-64,-65,54,54,54,-43,-44,-32,-33,-29,-70,-70,-31,54,54,-38,-39,54,-45,-46,54,-34,-35,-29,54,-28,-30,-48,-40,-41,-42,-36,-26,-37,-27,]),'LT':([22,23,32,36,44,52,53,56,57,58,59,71,76,77,78,82,83,86,87,89,90,91,105,106,107,108,109,110,111,113,119,120,121,131,132,133,134,],[55,55,-64,-65,55,55,55,-43,-44,-32,-33,-29,-70,-70,-31,55,55,-38,-39,55,-45,-46,55,-34,-35,-29,55,-28,-30,-48,-40,-41,-42,-36,-26,-37,-27,]),'TRUE':([22,23,32,36,44,52,53,56,57,58,59,71,76,77,78,82,83,86,87,89,90,91,105,106,107,108,109,110,111,113,119,120,121,131,132,133,134,],[58,58,-64,-65,58,58,58,-43,-44,-32,-33,-29,-70,-70,-31,58,58,-38,-39,58,-45,-46,58,-34,-35,-29,58,-28,-30,-48,-40,-41,-42,-36,-26,-37,-27,]),'FALSE':([22,23,32,36,44,52,53,56,57,58,59,71,76,77,78,82,83,86,87,89,90,91,105,106,107,108,109,110,111,113,119,120,121,131,132,133,134,],[59,59,-64,-65,59,59,59,-43,-44,-32,-33,-29,-70,-70,-31,59,59,-38,-39,59,-45,-46,59,-34,-35,-29,59,-28,-30,-48,-40,-41,-42,-36,-26,-37,-27,]),'DO':([32,36,56,57,58,59,60,61,71,76,77,78,86,87,90,91,106,107,108,110,111,113,119,120,121,131,132,133,134,],[-64,-65,-43,-44,-32,-33,94,95,-29,-70,-70,-31,-38,-39,-45,-46,-34,-35,-29,-28,-30,-48,-40,-41,-42,-36,-26,-37,-27,]),'INC':([32,36,44,54,55,56,57,58,59,70,71,74,75,76,77,78,81,86,87,90,91,92,93,105,106,107,108,109,110,111,113,119,120,121,125,126,127,128,131,132,133,134,138,139,140,141,],[-64,-65,74,74,74,-43,-44,-32,-33,74,-29,74,74,-70,-70,-31,74,-38,-39,-45,-46,74,74,74,-34,-35,-29,74,-28,-30,-48,-40,-41,-42,74,74,74,74,-36,-26,-37,-27,74,74,74,74,]),'DEC':([32,36,44,54,55,56,57,58,59,70,71,74,75,76,77,78,81,86,87,90,91,92,93,105,106,107,108,109,110,111,113,119,120,121,125,126,127,128,131,132,133,134,138,139,140,141,],[-64,-65,75,75,75,-43,-44,-32,-33,75,-29,75,75,-70,-70,-31,75,-38,-39,-45,-46,75,75,75,-34,-35,-29,75,-28,-30,-48,-40,-41,-42,75,75,75,75,-36,-26,-37,-27,75,75,75,75,]),'NUM':([32,36,44,54,55,56,57,58,59,70,71,74,75,76,77,78,81,86,87,90,91,92,93,105,106,107,108,109,110,111,113,119,120,121,125,126,127,128,131,132,133,134,138,139,140,141,],[-64,-65,78,78,78,-43,-44,-32,-33,78,-29,78,78,-70,-70,-31,78,-38,-39,-45,-46,78,78,78,-34,-35,-29,78,-28,-30,-48,-40,-41,-42,78,78,78,78,-36,-26,-37,-27,78,78,78,78,]),'CLSQBR':([32,36,56,57,58,59,71,76,77,78,79,80,86,87,90,91,106,107,108,110,111,112,113,119,120,121,124,131,132,133,134,144,145,146,147,],[-64,-65,-43,-44,-32,-33,-29,-70,-70,-31,-50,113,-38,-39,-45,-46,-34,-35,-29,-28,-30,-49,-48,-40,-41,-42,137,-36,-26,-37,-27,148,149,150,151,]),'EQUAL':([43,46,47,48,],[70,81,82,83,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'sentence_groups':([0,50,51,94,95,117,118,137,],[2,84,85,122,123,135,136,143,]),'sentence':([0,38,50,51,67,68,94,95,101,117,118,137,],[5,69,5,5,69,103,5,5,103,5,5,5,]),'definition':([0,38,50,51,67,68,94,95,101,117,118,137,],[6,6,6,6,6,6,6,6,6,6,6,6,]),'if':([0,38,50,51,67,68,94,95,101,117,118,137,],[7,7,7,7,7,7,7,7,7,7,7,7,]),'while':([0,38,50,51,67,68,94,95,101,117,118,137,],[8,8,8,8,8,8,8,8,8,8,8,8,]),'if_err':([0,38,50,51,67,68,94,95,101,117,118,137,],[9,9,9,9,9,9,9,9,9,9,9,9,]),'while_err':([0,38,50,51,67,68,94,95,101,117,118,137,],[10,10,10,10,10,10,10,10,10,10,10,10,]),'procedure':([0,38,50,51,67,68,94,95,101,117,118,137,],[11,11,11,11,11,11,11,11,11,11,11,11,]),'call_procedure':([0,38,50,51,52,53,67,68,74,75,89,94,95,101,105,109,117,118,137,],[12,12,12,12,87,91,12,12,107,107,91,12,12,12,107,107,12,12,12,]),'robot_command':([0,38,50,51,67,68,94,95,101,117,118,137,],[13,13,13,13,13,13,13,13,13,13,13,13,]),'map_setting':([0,38,50,51,67,68,94,95,101,117,118,137,],[14,14,14,14,14,14,14,14,14,14,14,14,]),'logic_cmd':([0,22,23,38,44,50,51,52,53,67,68,82,83,89,94,95,101,105,109,117,118,137,],[25,56,56,25,56,25,25,56,56,25,25,56,56,56,25,25,25,56,56,25,25,25,]),'rot_dir':([0,38,50,51,67,68,94,95,101,117,118,137,],[26,26,26,26,26,26,26,26,26,26,26,26,]),'math_cmd':([0,38,44,50,51,54,55,67,68,70,74,75,81,92,93,94,95,101,105,109,117,118,125,126,127,128,137,138,139,140,141,],[27,27,76,27,27,76,76,27,27,76,76,76,76,76,76,27,27,27,76,76,27,27,76,76,76,76,27,76,76,76,76,]),'logic_expr':([22,23,44,52,53,82,83,89,105,109,],[50,60,73,86,90,115,116,90,133,133,]),'bool':([22,23,44,52,53,82,83,89,105,109,],[57,57,57,57,57,57,57,57,57,57,]),'sentence_group':([38,67,],[68,101,]),'math_expr':([44,54,55,70,74,75,81,92,93,105,109,125,126,127,128,138,139,140,141,],[72,92,93,104,106,106,114,120,121,106,106,138,139,140,141,144,145,146,147,]),'number':([44,54,55,70,74,75,81,92,93,105,109,125,126,127,128,138,139,140,141,],[77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,]),'varlist':([45,96,],[80,124,]),'or_elem':([53,89,],[89,119,]),'math_first':([74,75,105,109,],[105,109,131,131,]),'empty':([76,77,],[110,111,]),'math_second':([105,109,],[132,134,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> sentence_groups','program',1,'p_program','parser.py',22),
  ('sentence_groups -> EOS OPBR EOS sentence_group CLBR EOS','sentence_groups',6,'p_sentence_groups','parser.py',27),
  ('sentence_groups -> OPBR EOS sentence_group CLBR EOS','sentence_groups',5,'p_sentence_groups','parser.py',28),
  ('sentence_groups -> OPBR EOS sentence_group CLBR','sentence_groups',4,'p_sentence_groups','parser.py',29),
  ('sentence_groups -> EOS OPBR EOS sentence_group CLBR','sentence_groups',5,'p_sentence_groups','parser.py',30),
  ('sentence_groups -> sentence','sentence_groups',1,'p_sentence_groups','parser.py',31),
  ('sentence_group -> sentence_group sentence','sentence_group',2,'p_sentence_group','parser.py',41),
  ('sentence_group -> sentence','sentence_group',1,'p_sentence_group','parser.py',42),
  ('sentence -> definition EOS','sentence',2,'p_sentence','parser.py',50),
  ('sentence -> if','sentence',1,'p_sentence','parser.py',51),
  ('sentence -> while','sentence',1,'p_sentence','parser.py',52),
  ('sentence -> if_err','sentence',1,'p_sentence','parser.py',53),
  ('sentence -> while_err','sentence',1,'p_sentence','parser.py',54),
  ('sentence -> procedure','sentence',1,'p_sentence','parser.py',55),
  ('sentence -> call_procedure EOS','sentence',2,'p_sentence','parser.py',56),
  ('sentence -> robot_command EOS','sentence',2,'p_sentence','parser.py',57),
  ('sentence -> map_setting EOS','sentence',2,'p_sentence','parser.py',58),
  ('sentence -> error','sentence',1,'p_sentence','parser.py',59),
  ('definition -> INT VARIABLE EQUAL math_expr','definition',4,'p_definition','parser.py',64),
  ('definition -> CINT VARIABLE EQUAL math_expr','definition',4,'p_definition','parser.py',65),
  ('definition -> BOOLEAN VARIABLE EQUAL logic_expr','definition',4,'p_definition','parser.py',66),
  ('definition -> CBOOLEAN VARIABLE EQUAL logic_expr','definition',4,'p_definition','parser.py',67),
  ('definition -> VARIABLE ASSIGN math_expr','definition',3,'p_definition','parser.py',68),
  ('definition -> VARIABLE ASSIGN logic_expr','definition',3,'p_definition','parser.py',69),
  ('definition -> MAP VARIABLE','definition',2,'p_definition','parser.py',70),
  ('math_expr -> INC math_first math_second','math_expr',3,'p_math_expr','parser.py',83),
  ('math_expr -> DEC math_first math_second','math_expr',3,'p_math_expr','parser.py',84),
  ('math_expr -> math_cmd empty','math_expr',2,'p_math_expr','parser.py',85),
  ('math_expr -> VARIABLE','math_expr',1,'p_math_expr','parser.py',86),
  ('math_expr -> number empty','math_expr',2,'p_math_expr','parser.py',87),
  ('number -> NUM','number',1,'p_number','parser.py',97),
  ('bool -> TRUE','bool',1,'p_bool','parser.py',102),
  ('bool -> FALSE','bool',1,'p_bool','parser.py',103),
  ('math_first -> math_expr','math_first',1,'p_math_first','parser.py',108),
  ('math_first -> call_procedure','math_first',1,'p_math_first','parser.py',109),
  ('math_second -> math_first','math_second',1,'p_math_second','parser.py',114),
  ('math_second -> logic_expr','math_second',1,'p_math_second','parser.py',115),
  ('logic_expr -> NOT logic_expr','logic_expr',2,'p_logic_expr','parser.py',120),
  ('logic_expr -> NOT call_procedure','logic_expr',2,'p_logic_expr','parser.py',121),
  ('logic_expr -> OR or_elem or_elem','logic_expr',3,'p_logic_expr','parser.py',122),
  ('logic_expr -> GT math_expr math_expr','logic_expr',3,'p_logic_expr','parser.py',123),
  ('logic_expr -> LT math_expr math_expr','logic_expr',3,'p_logic_expr','parser.py',124),
  ('logic_expr -> logic_cmd','logic_expr',1,'p_logic_expr','parser.py',125),
  ('logic_expr -> bool','logic_expr',1,'p_logic_expr','parser.py',126),
  ('or_elem -> logic_expr','or_elem',1,'p_or_elem','parser.py',136),
  ('or_elem -> call_procedure','or_elem',1,'p_or_elem','parser.py',137),
  ('procedure -> PROC VARIABLE OPSQBR varlist CLSQBR sentence_groups','procedure',6,'p_procedure','parser.py',142),
  ('call_procedure -> VARIABLE OPSQBR varlist CLSQBR','call_procedure',4,'p_call_procedure','parser.py',151),
  ('varlist -> varlist VARIABLE','varlist',2,'p_varlist','parser.py',158),
  ('varlist -> VARIABLE','varlist',1,'p_varlist','parser.py',159),
  ('if_err -> IF error sentence_groups ELSE sentence_groups','if_err',5,'p_if_err','parser.py',168),
  ('if_err -> IF error sentence_groups','if_err',3,'p_if_err','parser.py',169),
  ('while_err -> WHILE error DO sentence_groups','while_err',4,'p_while_err','parser.py',177),
  ('while_err -> WHILE error','while_err',2,'p_while_err','parser.py',178),
  ('if -> IF logic_expr sentence_groups ELSE sentence_groups','if',5,'p_if','parser.py',187),
  ('if -> IF logic_expr sentence_groups','if',3,'p_if','parser.py',188),
  ('while -> WHILE logic_expr DO sentence_groups','while',4,'p_while','parser.py',196),
  ('robot_command -> logic_cmd','robot_command',1,'p_robot_command','parser.py',201),
  ('robot_command -> rot_dir','robot_command',1,'p_robot_command','parser.py',202),
  ('robot_command -> math_cmd','robot_command',1,'p_robot_command','parser.py',203),
  ('rot_dir -> BACK','rot_dir',1,'p_rot_dir','parser.py',208),
  ('rot_dir -> RIGHT','rot_dir',1,'p_rot_dir','parser.py',209),
  ('rot_dir -> LEFT','rot_dir',1,'p_rot_dir','parser.py',210),
  ('logic_cmd -> STEP','logic_cmd',1,'p_logic_cmd','parser.py',215),
  ('math_cmd -> LOOK','math_cmd',1,'p_math_cmd','parser.py',220),
  ('map_setting -> BAR OPSQBR VARIABLE VARIABLE math_expr math_expr CLSQBR','map_setting',7,'p_map_setting','parser.py',225),
  ('map_setting -> EMP OPSQBR VARIABLE VARIABLE math_expr math_expr CLSQBR','map_setting',7,'p_map_setting','parser.py',226),
  ('map_setting -> SET OPSQBR VARIABLE VARIABLE math_expr math_expr CLSQBR','map_setting',7,'p_map_setting','parser.py',227),
  ('map_setting -> CLR OPSQBR VARIABLE VARIABLE math_expr math_expr CLSQBR','map_setting',7,'p_map_setting','parser.py',228),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',235),
]
