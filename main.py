import ast
from PyQt5 import QtWidgets, uic
import sys

class Main:
    D = ""
    testing_switch = ""
    results_list = []
    def nombreArchivo(self,name):
      self.filename= name


    def read_file(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                if "automata" in filename:
                    content = file.read()
                    AFD = ast.literal_eval(content)
                    self.D = AFD
                    return True
                content = file.read()
                cadena = ""
                switch = []
                for c in content:
                    if c != '\n' and c != ' ':
                        cadena = cadena + c
                switch.append(cadena)
                return switch
        except Exception as e:
            print(e)
            print(f"El archivo '{filename}' no existe.")

    def open_txt_test(self, interfaz):
      filename = QtWidgets.QFileDialog.getOpenFileName(None, "Abrir archivo", "", "Text files (*.txt)")
      print(filename)
      self.testing_switchs = self.read_file(filename[0])
      print(interfaz)
      self.evaluate(interfaz)

    def step_afd(self,D,q,a):
      try:
         assert(a in D["Sigma"])
         assert(q in D["Q"])
         return D["Delta"][(q,a)]
      except:
         return False

    def run_afd(self,D,w):
      curstate = D["q0"]
      if w == "":
         return curstate
      else:
         return self.run_afd_h(D,w[1:], self.step_afd(D,curstate,w[0]))

    def run_afd_h(self,D,w,q):
      if w == "":
         return q
      else:
         return self.run_afd_h(D,w[1:], self.step_afd(D,q,w[0]))

    def accepts_afd(self,D,w):
      return self.run_afd(D,w) in D["F"]

    def evaluate(self,interfaz):
      for character in self.testing_switchs:
         if self.accepts_afd(self.D, character):
            self.results_list.append(f"La sentencia: '{character}' es aceptada ")
         else:
            self.results_list.append(f"La sentencia: ' {character} es rechazada")
      interfaz.list_result.addItems(self.results_list)
    

if __name__ == '__main__' :
   app = QtWidgets.QApplication(sys.argv)
   
   main = Main()
   main.read_file('automata.txt')


   interfaz = uic.loadUi("interfaz.ui")
   interfaz.show()
   

   interfaz.select_test.clicked.connect(lambda: main.open_txt_test(interfaz))
   
   sys.exit(app.exec_())