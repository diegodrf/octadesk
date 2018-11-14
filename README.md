## Classe para contectar-se na API da ferramenta de chamados Octadesk

* Exemplo 

`var = Octadesk('usuario@email.com', 'APItoken')`

`var.login()`

`var.ticketCreate(title='Ticket de teste', body='Mensagem do ticket', tags=['Monitoramento'], toEmail='cliente@email.com', toDomain='empresa')`

_É retornornado o número do ticket criado._ 
