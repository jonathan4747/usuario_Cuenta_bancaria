class  Cuenta:
    listabalance=[]
    def __init__(self,balance=0,taza_interes=0.01):
        self.balance = balance
        self.taza_interes = taza_interes
        Cuenta.listabalance.append(self)
    
    def Deposito(self,mount):
        self.balance = self.balance + mount
        return self
    
    def Retiro(self,mount):
        if self.balance > mount:
            self.balance = self.balance - mount
        else: 
            self.balance = self.balance - 5
            print("Saldo insuficiente:cobrando una tarifa de $5")
        return self  
      
    def imprimirBalance(self):
        print(str(self.balance))
        return self
    
    def Intereses(self):
        self.balance=self.balance*self.taza_interes + self.balance
        return self
    
    @classmethod
    def imprimirtodoslosBalance(cls):
        for lista in cls.listabalance:
            lista.imprimirBalance()
        

class Usuario:
    listaCuenta=[]
    def __init__(self, nombre="N/A",email="N/A"):
        self.nombre= nombre
        self.email = email
        self.cuenta= Cuenta(balance=0,taza_interes=0.01)
    def deposito_usuario(self,mount):
        self.cuenta.Deposito(mount)
        return self
    def retiro_usuario(self,mount):
        self.cuenta.Retiro(mount)
        return self
    def imprimir_usuario(self):
        print(self.nombre,end=" ")
        self.cuenta.imprimirBalance()
        return self
        
        