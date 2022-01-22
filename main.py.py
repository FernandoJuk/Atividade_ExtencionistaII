from busca_placa import BuscaPlaca

print('------------------------------')
print('*      Digite a placa        *')
print('------------------------------')
print('*** EX: AAA-0000  AAA-0A00 ***')
print('------------------------------')
placa = input()
objeto_placa = BuscaPlaca(placa)
ano,anoModelo,chassi,cor,modelo,placa,situacao,uf = objeto_placa.acessa_via_placa()

print(
    "\nModelo:",modelo,
    "\nAno:",ano,"/",anoModelo,
    "\nChassi:",chassi,
    "\nCor:",cor,
    "\nPlaca:",placa,
    "\nsituacao:",situacao,
    "\nuf:",uf
    )