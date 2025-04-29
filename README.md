# todolistinpy
To do list made in Python with PyQt5

📋 To-Do List
Alunos:
Henrique Maia
Ricardo Gabriel
Nicolas Borges

📝 Descrição do Projeto
O To-Do List é um gerenciador de tarefas com interface gráfica (GUI) desenvolvida em PyQt5. Ele permite adicionar, concluir, remover e listar tarefas de forma prática e intuitiva.

✅ Funcionalidades
Adicionar nova tarefa.
Marcar uma tarefa como concluída.
Remover uma tarefa específica.
Limpar todas as tarefas (com confirmação).
Exibir a lista de tarefas com indicação de status: "Pendente" ou "Concluída".

⚙️ Regras de Negócio
Não é permitido adicionar tarefas sem nome.
A remoção de todas as tarefas exige confirmação do usuário.
Cada tarefa possui um status: Pendente ou Concluída.

🧪 Plano de Testes

Caso	Ação	Entrada	Resultado Esperado
01	Adicionar tarefa	"Estudar para prova"	A tarefa é adicionada como "Pendente".
02	Concluir tarefa	Selecionar "Estudar para prova"	A tarefa é marcada como "Concluída".
03	Remover tarefa	Selecionar "Estudar para prova"	A tarefa é removida da lista.
04	Tentar adicionar tarefa vazia	"" (campo vazio)	Uma mensagem de erro é exibida.
05	Limpar todas as tarefas	Confirmar "Sim"	Todas as tarefas são apagadas.

🧱 Estrutura do Projeto

🧠 Classes
TaskManager: responsável pela lógica e gerenciamento das tarefas.
App: responsável pela interface gráfica e interação com o usuário.

🔧 Principais Métodos
adicionar_tarefa()

remover_tarefa()

marcar_concluida()

limpar_tarefas()

filtrar_tarefas()

mostrar_tarefas()

get_status() (simula um switch-case com match)

🔁 Controles de Fluxo
if: Validação de entrada e confirmação de ações.
match-case: Mapeamento dos status das tarefas.
for: Listagem de tarefas na interface.

🛠️ Tecnologias Utilizadas
Python 3
PyQt5

⚠️ Comentários Críticos
O código contém comentários alertando sobre validações essenciais, como a proibição de adicionar tarefas vazias.
Também há avisos sobre ações destrutivas, como a exclusão total da lista de tarefas.

📌 Observações Finais
Este projeto tem como objetivo o aprendizado e aplicação prática de conceitos de programação orientada a objetos, interfaces gráficas e validação de entradas no contexto de desenvolvimento em Python com PyQt5.

