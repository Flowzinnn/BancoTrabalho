from abc import ABC, abstractmethod

class Autenticavel(ABC):
    
    @abstractmethod
    def autenticar(self, senha: str) -> bool:
        pass

class Tributavel(ABC):
    
    @abstractmethod
    def get_valor_imposto(self) -> float:
        pass
    
class Rentavel(ABC):
    
    @abstractmethod
    def get_rendimento(self) -> float:
        pass
