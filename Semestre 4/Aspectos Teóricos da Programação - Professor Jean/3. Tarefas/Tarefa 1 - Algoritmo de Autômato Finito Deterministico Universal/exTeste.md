EXEMPLO PRÁTICO

===================================================================

///////////////////
SISTEMA :

Defina os estados (Separe os componentes com ',')

(Exemplo: q0, q1)
-----------------------

///////////////////
RESPOSTA DO USUÁRIO: q0, q1, q2 
///////////////////
___________________________________________________________________

///////////////////
SISTEMA:

Defina o alfabeto (Separe os componentes com ',')

(Exemplo: 0, 1)
-----------------------

///////////////////
RESPOSTA DO USUÁRIO: 0, 1
///////////////////
___________________________________________________________________

///////////////////
SISTEMA:

Defina as transições a seguir

(Exemplo: q0 : '0' = q1)
-----------------------

///////////////////
RESPOSTA DO USUÁRIO: q0 : '0' = q1
RESPOSTA DO USUÁRIO: q0 : '1' = q2
RESPOSTA DO USUÁRIO: q1 : '0' = q1
RESPOSTA DO USUÁRIO: q1 : '1' = q2
RESPOSTA DO USUÁRIO: q2 : '0' = q2
RESPOSTA DO USUÁRIO: q2 : '1' = q0
/////////////////// 
___________________________________________________________________

///////////////////
SISTEMA:

Defina o estado inicial

(Exemplo: q0)
-----------------------

///////////////////
RESPOSTA DO USUÁRIO: q0
///////////////////
___________________________________________________________________

///////////////////
SISTEMA:

Defina o conjunto de estados finais (Separe os componentes com ',')

(Exemplo: q0, q1)
-----------------------

///////////////////
RESPOSTA DO USUÁRIO: q2
///////////////////
___________________________________________________________________

///////////////////
SISTEMA:

Q : ['q0', 'q1', 'q2']
Σ : ['0', '1']
δ : {'q0': {'0': 'q1', '1': 'q2'}, 'q1': {'0': 'q1', '1': 'q2'}, 'q2': {'0': 'q2', '1': 'q0'}}
q0: q0
Qf: {'q2'}

-----------------------

///////////////////
RESPOSTA DO USUÁRIO: Defina o que deseja ler: 00010101
///////////////////
___________________________________________________________________

///////////////////
SISTEMA:

FOI ACEITO! A entrada '00010101'

-----------------------

Deseja criar outra entrada?
s = 'Sim'
Digite qualquer coisa = 'Não'

///////////////////
RESPOSTA DO USUÁRIO: ...
///////////////////
