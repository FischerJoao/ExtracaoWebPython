# Projeto extração de dados do MAGALU com Python e Selenium

## Funcionalidades

- **Abrir Navegador**: Abre o navegador e acessa o site da Magazine Luiza.
- **Aceitar Cookies**: Aceita os cookies do site.
- **Pesquisar Notebooks**: Realiza a pesquisa por notebooks no site.
- **Coletar Dados**: Coleta os dados dos notebooks, incluindo nome, avaliação e link.
- **Processar Dados**: Processa os dados coletados e salva em um arquivo Excel.
- **Enviar Email**: Envia o arquivo Excel por email.

## Como Executar

1. Instale as dependências:

   ```sh
   pip install -r requirements.txt
   ```

2. Configure seu email e senha temporária no arquivo [enviarEmail.py].

3. Execute o script principal:
   ```sh
   python main.py
   ```

## Dependências

- Python 3.x
- Selenium
- Pandas
- Openpyxl

**Nota**: Este projeto é apenas para fins educacionais. Use-o com responsabilidade e respeite os termos de uso dos sites que você acessa.
