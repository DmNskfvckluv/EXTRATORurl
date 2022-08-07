import re


class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):

        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if self.url == "":
            raise ValueError("A URL esta vazia")
        padrao_url = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError("A URL nao eh valida!")
    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return f'URL:{self.url}\nURL base: {self.get_url_base()}\nParametros: {self.get_url_parametros()}'

    def __eq__(self, other):
        return self.url == other.url


extrator_url = ExtratorURL('bytebank.com/cambio?quantidade=100&moedaOrigem=dolar&moedaDestino=real')
print(extrator_url.get_valor_parametro('moedaOrigem'))
print(f'tamanho da URL eh:{len(extrator_url)}')
print(extrator_url)
extrator_url2 = ExtratorURL('bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar')
print(extrator_url == extrator_url2)


VALOR_DOLAR = 5.50  # 1 dólar = 5.50 reais
moeda_origem = extrator_url.get_valor_parametro("moedaOrigem")
moeda_destino = extrator_url.get_valor_parametro("moedaDestino")
quantidade = extrator_url.get_valor_parametro("quantidade")
if moeda_origem == 'real':
    total = int(quantidade) * VALOR_DOLAR
else:
    total = int(quantidade) / VALOR_DOLAR
print(total)
