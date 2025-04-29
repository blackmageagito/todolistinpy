import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit,
    QListWidget, QMessageBox
)
from PyQt5.QtCore import Qt

class TaskManager:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, nome):
        if nome:
            self.tarefas.append((nome, "pendente"))
        else:
            raise ValueError("Nome da tarefa não pode ser vazio.")

    def remover_tarefa(self, nome):
        self.tarefas = [t for t in self.tarefas if t[0] != nome]

    def marcar_concluida(self, nome):
        self.tarefas = [(t[0], "concluida") if t[0] == nome else t for t in self.tarefas]

    def limpar_tarefas(self):
        self.tarefas.clear()

    def filtrar_tarefas(self, status):
        return [t for t in self.tarefas if t[1] == status]

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("To-Do List")
        self.setGeometry(300, 200, 400, 400)

        self.manager = TaskManager()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.entrada = QLineEdit()
        self.entrada.setPlaceholderText("Digite uma tarefa")
        layout.addWidget(self.entrada)

        btn_layout = QHBoxLayout()
        btn_add = QPushButton("Adicionar")
        btn_concluir = QPushButton("Concluir")
        btn_remover = QPushButton("Remover")
        btn_limpar = QPushButton("Limpar tudo")
        btn_mostrar = QPushButton("Mostrar tarefas")

        btn_add.clicked.connect(self.adicionar_tarefa)
        btn_concluir.clicked.connect(self.concluir_tarefa)
        btn_remover.clicked.connect(self.remover_tarefa)
        btn_limpar.clicked.connect(self.limpar_tarefas)
        btn_mostrar.clicked.connect(self.mostrar_tarefas)

        for btn in [btn_add, btn_concluir, btn_remover, btn_limpar, btn_mostrar]:
            btn_layout.addWidget(btn)

        layout.addLayout(btn_layout)

        self.lista = QListWidget()
        layout.addWidget(self.lista)

        self.setLayout(layout)

    def adicionar_tarefa(self):
        nome = self.entrada.text()
        try:
            self.manager.adicionar_tarefa(nome)
            self.entrada.clear()
            self.mostrar_tarefas()
        except ValueError as e:
            QMessageBox.critical(self, "Erro", str(e))

    def concluir_tarefa(self):
        item = self.lista.currentItem()
        if item:
            nome = item.text().split(" [")[0]
            self.manager.marcar_concluida(nome)
            self.mostrar_tarefas()

    def remover_tarefa(self):
        item = self.lista.currentItem()
        if item:
            nome = item.text().split(" [")[0]
            self.manager.remover_tarefa(nome)
            self.mostrar_tarefas()

    def limpar_tarefas(self):
        #parte crítica: confirmação para ação destrutiva
        confirm = QMessageBox.question(
            self, "Confirmar", "Deseja apagar todas as tarefas?",
            QMessageBox.Yes | QMessageBox.No
        )
        if confirm == QMessageBox.Yes:
            self.manager.limpar_tarefas()
            self.mostrar_tarefas()

    def mostrar_tarefas(self):
        self.lista.clear()
        for tarefa in self.manager.tarefas:
            status_formatado = self.get_status(tarefa[1])
            self.lista.addItem(f"{tarefa[0]} [{status_formatado}]") 

    def get_status(self, status):
        #Parte crítica: simulação de switch-case com match
        match status:
            case "pendente":
                return "🕓 Pendente"
            case "concluida":
                return "✅ Concluída"
            case _:
                return "❓ Desconhecido"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())
    
