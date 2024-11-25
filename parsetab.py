
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'programrightASSIGNleftEQNEleftLTLEGTGEleftPLUSMINUSleftTIMESDIVIDEASSIGN BOOLEAN DIVIDE ELSE EQ FOR GE GT IF LBRACE LE LPAREN LT MINUS NAME NE NUMBER PLUS PRINT RBRACE RPAREN SEMICOLON STRING TIMES WHILEprogram : statementsstatements : statements statementstatements : statement\n    statement : assignment SEMICOLON\n              | if_statement\n              | for_statement\n              | while_statement\n              | block_statement\n              | print_statement SEMICOLON\n    for_statement : FOR LPAREN expression_opt SEMICOLON expression_opt RPAREN block_statementwhile_statement : WHILE LPAREN expression RPAREN block_statementassignment : NAME ASSIGN expression\n    expression_opt : expression\n                   | empty\n    empty :\n    if_statement : IF LPAREN expression RPAREN block_statement\n                 | IF LPAREN expression RPAREN block_statement ELSE block_statement\n    block_statement : LBRACE statements RBRACEprint_statement : PRINT LPAREN expression RPAREN\n    expression : expression PLUS expression\n               | expression MINUS expression\n               | expression TIMES expression\n               | expression DIVIDE expression\n               | expression EQ expression\n               | expression NE expression\n               | expression LT expression\n               | expression LE expression\n               | expression GT expression\n               | expression GE expression\n    expression : NAME ASSIGN expressionexpression : factorfactor : BOOLEANfactor : NUMBERfactor : NAMEfactor : STRINGfactor : LPAREN expression RPARENfactor : MINUS factor'
    
_lr_action_items = {'NAME':([0,2,3,5,6,7,8,14,16,17,18,19,20,21,22,23,24,27,32,38,40,41,42,43,44,45,46,47,48,49,50,55,70,72,75,76,],[10,10,-3,-5,-6,-7,-8,10,-2,-4,-9,25,25,25,25,10,25,52,25,-18,25,25,25,25,25,25,25,25,25,25,25,25,-16,-11,-17,-10,]),'IF':([0,2,3,5,6,7,8,14,16,17,18,23,38,70,72,75,76,],[11,11,-3,-5,-6,-7,-8,11,-2,-4,-9,11,-18,-16,-11,-17,-10,]),'FOR':([0,2,3,5,6,7,8,14,16,17,18,23,38,70,72,75,76,],[12,12,-3,-5,-6,-7,-8,12,-2,-4,-9,12,-18,-16,-11,-17,-10,]),'WHILE':([0,2,3,5,6,7,8,14,16,17,18,23,38,70,72,75,76,],[13,13,-3,-5,-6,-7,-8,13,-2,-4,-9,13,-18,-16,-11,-17,-10,]),'LBRACE':([0,2,3,5,6,7,8,14,16,17,18,23,38,54,56,70,72,73,74,75,76,],[14,14,-3,-5,-6,-7,-8,14,-2,-4,-9,14,-18,14,14,-16,-11,14,14,-17,-10,]),'PRINT':([0,2,3,5,6,7,8,14,16,17,18,23,38,70,72,75,76,],[15,15,-3,-5,-6,-7,-8,15,-2,-4,-9,15,-18,-16,-11,-17,-10,]),'$end':([1,2,3,5,6,7,8,16,17,18,38,70,72,75,76,],[0,-1,-3,-5,-6,-7,-8,-2,-4,-9,-18,-16,-11,-17,-10,]),'RBRACE':([3,5,6,7,8,16,17,18,23,38,70,72,75,76,],[-3,-5,-6,-7,-8,-2,-4,-9,38,-18,-16,-11,-17,-10,]),'SEMICOLON':([4,9,21,25,26,28,29,30,31,34,35,36,51,52,57,58,59,60,61,62,63,64,65,66,67,68,69,],[17,18,-15,-34,-12,-31,-32,-33,-35,55,-13,-14,-37,-34,-19,-30,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-36,]),'ASSIGN':([10,25,],[19,40,]),'LPAREN':([11,12,13,15,19,20,21,22,24,27,32,40,41,42,43,44,45,46,47,48,49,50,55,],[20,21,22,24,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'BOOLEAN':([19,20,21,22,24,27,32,40,41,42,43,44,45,46,47,48,49,50,55,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'NUMBER':([19,20,21,22,24,27,32,40,41,42,43,44,45,46,47,48,49,50,55,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'STRING':([19,20,21,22,24,27,32,40,41,42,43,44,45,46,47,48,49,50,55,],[31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'MINUS':([19,20,21,22,24,25,26,27,28,29,30,31,32,33,35,37,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,55,58,59,60,61,62,63,64,65,66,67,68,69,],[27,27,27,27,27,-34,42,27,-31,-32,-33,-35,27,42,42,42,42,27,27,27,27,27,27,27,27,27,27,27,-37,-34,42,27,42,-20,-21,-22,-23,42,42,42,42,42,42,-36,]),'PLUS':([25,26,28,29,30,31,33,35,37,39,51,52,53,58,59,60,61,62,63,64,65,66,67,68,69,],[-34,41,-31,-32,-33,-35,41,41,41,41,-37,-34,41,41,-20,-21,-22,-23,41,41,41,41,41,41,-36,]),'TIMES':([25,26,28,29,30,31,33,35,37,39,51,52,53,58,59,60,61,62,63,64,65,66,67,68,69,],[-34,43,-31,-32,-33,-35,43,43,43,43,-37,-34,43,43,43,43,-22,-23,43,43,43,43,43,43,-36,]),'DIVIDE':([25,26,28,29,30,31,33,35,37,39,51,52,53,58,59,60,61,62,63,64,65,66,67,68,69,],[-34,44,-31,-32,-33,-35,44,44,44,44,-37,-34,44,44,44,44,-22,-23,44,44,44,44,44,44,-36,]),'EQ':([25,26,28,29,30,31,33,35,37,39,51,52,53,58,59,60,61,62,63,64,65,66,67,68,69,],[-34,45,-31,-32,-33,-35,45,45,45,45,-37,-34,45,45,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-36,]),'NE':([25,26,28,29,30,31,33,35,37,39,51,52,53,58,59,60,61,62,63,64,65,66,67,68,69,],[-34,46,-31,-32,-33,-35,46,46,46,46,-37,-34,46,46,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-36,]),'LT':([25,26,28,29,30,31,33,35,37,39,51,52,53,58,59,60,61,62,63,64,65,66,67,68,69,],[-34,47,-31,-32,-33,-35,47,47,47,47,-37,-34,47,47,-20,-21,-22,-23,47,47,-26,-27,-28,-29,-36,]),'LE':([25,26,28,29,30,31,33,35,37,39,51,52,53,58,59,60,61,62,63,64,65,66,67,68,69,],[-34,48,-31,-32,-33,-35,48,48,48,48,-37,-34,48,48,-20,-21,-22,-23,48,48,-26,-27,-28,-29,-36,]),'GT':([25,26,28,29,30,31,33,35,37,39,51,52,53,58,59,60,61,62,63,64,65,66,67,68,69,],[-34,49,-31,-32,-33,-35,49,49,49,49,-37,-34,49,49,-20,-21,-22,-23,49,49,-26,-27,-28,-29,-36,]),'GE':([25,26,28,29,30,31,33,35,37,39,51,52,53,58,59,60,61,62,63,64,65,66,67,68,69,],[-34,50,-31,-32,-33,-35,50,50,50,50,-37,-34,50,50,-20,-21,-22,-23,50,50,-26,-27,-28,-29,-36,]),'RPAREN':([25,28,29,30,31,33,35,36,37,39,51,52,53,55,58,59,60,61,62,63,64,65,66,67,68,69,71,],[-34,-31,-32,-33,-35,54,-13,-14,56,57,-37,-34,69,-15,-30,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-36,74,]),'ELSE':([38,70,],[-18,73,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statements':([0,14,],[2,23,]),'statement':([0,2,14,23,],[3,16,3,16,]),'assignment':([0,2,14,23,],[4,4,4,4,]),'if_statement':([0,2,14,23,],[5,5,5,5,]),'for_statement':([0,2,14,23,],[6,6,6,6,]),'while_statement':([0,2,14,23,],[7,7,7,7,]),'block_statement':([0,2,14,23,54,56,73,74,],[8,8,8,8,70,72,75,76,]),'print_statement':([0,2,14,23,],[9,9,9,9,]),'expression':([19,20,21,22,24,32,40,41,42,43,44,45,46,47,48,49,50,55,],[26,33,35,37,39,53,58,59,60,61,62,63,64,65,66,67,68,35,]),'factor':([19,20,21,22,24,27,32,40,41,42,43,44,45,46,47,48,49,50,55,],[28,28,28,28,28,51,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'expression_opt':([21,55,],[34,71,]),'empty':([21,55,],[36,36,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statements','program',1,'p_program','parser.py',107),
  ('statements -> statements statement','statements',2,'p_statements_multiple','parser.py',112),
  ('statements -> statement','statements',1,'p_statements_single','parser.py',117),
  ('statement -> assignment SEMICOLON','statement',2,'p_statement','parser.py',123),
  ('statement -> if_statement','statement',1,'p_statement','parser.py',124),
  ('statement -> for_statement','statement',1,'p_statement','parser.py',125),
  ('statement -> while_statement','statement',1,'p_statement','parser.py',126),
  ('statement -> block_statement','statement',1,'p_statement','parser.py',127),
  ('statement -> print_statement SEMICOLON','statement',2,'p_statement','parser.py',128),
  ('for_statement -> FOR LPAREN expression_opt SEMICOLON expression_opt RPAREN block_statement','for_statement',7,'p_for_statement','parser.py',134),
  ('while_statement -> WHILE LPAREN expression RPAREN block_statement','while_statement',5,'p_while_statement','parser.py',150),
  ('assignment -> NAME ASSIGN expression','assignment',3,'p_assignment','parser.py',156),
  ('expression_opt -> expression','expression_opt',1,'p_expression_opt','parser.py',162),
  ('expression_opt -> empty','expression_opt',1,'p_expression_opt','parser.py',163),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',169),
  ('if_statement -> IF LPAREN expression RPAREN block_statement','if_statement',5,'p_if_statement','parser.py',175),
  ('if_statement -> IF LPAREN expression RPAREN block_statement ELSE block_statement','if_statement',7,'p_if_statement','parser.py',176),
  ('block_statement -> LBRACE statements RBRACE','block_statement',3,'p_block_statement','parser.py',188),
  ('print_statement -> PRINT LPAREN expression RPAREN','print_statement',4,'p_print_statement','parser.py',193),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','parser.py',199),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','parser.py',200),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','parser.py',201),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','parser.py',202),
  ('expression -> expression EQ expression','expression',3,'p_expression_binop','parser.py',203),
  ('expression -> expression NE expression','expression',3,'p_expression_binop','parser.py',204),
  ('expression -> expression LT expression','expression',3,'p_expression_binop','parser.py',205),
  ('expression -> expression LE expression','expression',3,'p_expression_binop','parser.py',206),
  ('expression -> expression GT expression','expression',3,'p_expression_binop','parser.py',207),
  ('expression -> expression GE expression','expression',3,'p_expression_binop','parser.py',208),
  ('expression -> NAME ASSIGN expression','expression',3,'p_expression_assignment','parser.py',214),
  ('expression -> factor','expression',1,'p_expression_factor','parser.py',219),
  ('factor -> BOOLEAN','factor',1,'p_factor_boolean','parser.py',224),
  ('factor -> NUMBER','factor',1,'p_factor_number','parser.py',229),
  ('factor -> NAME','factor',1,'p_factor_name','parser.py',234),
  ('factor -> STRING','factor',1,'p_factor_string','parser.py',239),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor_grouped','parser.py',244),
  ('factor -> MINUS factor','factor',2,'p_factor_unary','parser.py',249),
]
