class pedido:
  def __init__(self, nome, produto, quantidade, preco_unitario, cupom):
    self.nome = nome
    self.produto = produto
    self.quantidade = quantidade
    self.preco_unitario = preco_unitario
    self.cupom = cupom.lower()

def calcular_subtotal(self):
    """
    Retorna o Subtotal numérico.
    """
    subtotal = quantidade*preco_unitario
    return subtotal

def calcular_desconto(self, subtotal, cupom):
    """
    Recebe cupom já padronizado e retorna o valor número do desconto.
    """
    if cupom == "sim":
      desconto = subtotal * 0.10
    else:
      desconto = 0
    return desconto

def classificar_pedido(self, subtotal):
    """
    Retorna uma das três classificações da página anterior.
    """
    if subtotal <= 30:
      classificação_do_pedido = "Pedido Pequeno"
    elif 30 < subtotal <= 100:
      classificação_do_pedido = "Pedido médio"
    else:
      classificação_do_pedido = "Pedido Grande"
    return classificação_do_pedido