class Restaurante:
   def __init__(self, nome, categoria):
      self.nome = ""
      self.categoria = ""
      self.ativo = False
   
   def __str__():
      return f'{self.nome} | {self.categoria}'

restaurante_praca = Restaurante("Praça","Gourmet")
restaurante_pizza = Restaurante("Pizza Express","Italiana")

restaurantes = [restaurante_praca, restaurante_pizza]

print(restaurante_praca)
print(restaurante_pizza)