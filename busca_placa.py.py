import requests
import re

class BuscaPlaca:

    def __init__(self, placa):
        placa = str(placa)
        if self.placa_eh_Valido(placa):
            self.placa = placa.upper()
        else:
            raise ValueError("Placa inválida!")

    def __str__(self):
        return self.format_placa()

    def placa_eh_Valido(self, placa):
        if ((len(placa) == 7 ) or (len(placa) == 8 and placa[3] == '-')):
            # Expressão regulares / padrão de uma placa
            padrao = "[A-Z]{3}-?[0-9]\w[0-9]{2}"
            # transforma toda a string em caixa alta, ou seja, em maiuscula
            texto_placa = placa.upper()
            # testa se cotem um padrão de placa no texto exemplo: AAA0X00 ou AAA-9999
            resposta = re.findall(padrao, texto_placa)

            if resposta :
                return True
            else:
                return False
        else:
            return False

    def format_placa(self):
        # Message": favor usar o formato AAA0X00 ou AAA9999 "
        if len(self.placa) == 8:
            return "{}{}".format(self.placa[:3],self.placa[4:])
        else:
            return"{}".format(self.placa[0:7])

    def acessa_via_placa(self):
        placa = "https://apicarros.com/v1/consulta/{}/json".format(self.format_placa())
        r = requests.get(placa)
        dados = r.json()
        return (
            dados['ano'],
            dados['anoModelo'],
            dados['chassi'],
            dados['cor'],
            dados['modelo'],
            dados['placa'],
            dados['situacao'],
            dados["uf"]
        )
