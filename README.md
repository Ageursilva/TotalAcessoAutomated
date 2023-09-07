
# Automação Total Acesso (Final Copa do Brasil 2023)

Este código foi feito para tentar me ajudar na compra do ingresso para final da copa do Brasil, entre São Paulo x Flamengo, visto que o São Paulo usa uma porcaria de site. O exemplo foi projetado para um jogo em especifico mas pode ser adaptado para outros jogos, alterando a URL e os seletores de elementos conforme necessário.

## Requisitos

Antes de executar o projeto, certifique-se de que você tenha as seguintes dependências instaladas:

-   **Python**: Verifique se o Python está instalado em seu sistema. Você pode baixá-lo em [python.org](https://www.python.org/downloads/).
    
-   **Selenium**: Instale a biblioteca Selenium usando o `pip`:
    

    
    `pip install selenium` 
    
-   **Navegador**: Este projeto utiliza o driver do Firefox para interagir com o navegador. Certifique-se de ter o Firefox instalado. Você pode baixá-lo em [mozilla.org](https://www.mozilla.org/firefox/).
    
-   **Geckodriver**: Você também precisa do driver do Firefox, chamado Geckodriver. Certifique-se de baixar a versão adequada para o seu sistema operacional em [geckodriver releases](https://github.com/mozilla/geckodriver/releases) e adicionar o local do arquivo ao seu PATH.
    

## Como Usar

Siga estas etapas para executar o projeto:

1.  Clone este repositório para o seu computador ou faça o download do código.
    
2.  Abra o arquivo `main.py` em um editor de código e edite a variável `cpf_value` com o CPF que deseja inserir no campo da página.
    
3.  Abra um terminal na pasta do projeto.
    
4.  Execute o projeto com o seguinte comando:
          
    `python main.py` 
    
5.  Uma janela será aberta com os botões "Pausar" e "Continuar". Você pode pausar e continuar a execução do script conforme necessário.
    
6.  O script preencherá automaticamente o campo com o CPF e clicará no botão na página especificada a cada 20 segundos (você pode ajustar esse intervalo de tempo no código).
    
7.  O script também inclui um limite de cliques no botão. Após um número definido de cliques (configurado na variável `limite_de_cliques`), ele recarregará a página para evitar problemas de "elemento não encontrado".
    
8.  Para encerrar o script, pressione `Ctrl + C` no terminal.
    
9.  Após a conclusão do script, o navegador será fechado automaticamente.
    

## Personalização

Este é um exemplo básico e pode não funcionar em todas as páginas da web. Você pode precisar ajustar o código para lidar com as características específicas da página que deseja automatizar. Aqui estão algumas sugestões de personalização:
-   **Trocar página do ingresso**: Você pode alterar o link do ingresso no código, no trecho `driver.get("COLOQUE O LINK AQUI")`, basta trocar a URL, no código ele já esta setado para o ingresso da final.

-   **Localização de Elementos**: Use as ferramentas de desenvolvedor do navegador para inspecionar os elementos da página e ajuste os seletores CSS no código (por exemplo, `By.CSS_SELECTOR`) para localizar corretamente os campos e botões relevantes.
    
-   **Comportamento de Recarregamento**: Ajuste o número de cliques permitidos antes de recarregar a página (variável `limite_de_cliques`) para se adequar à página que você está automatizando.
    
-   **Intervalo de Atualização**: Altere o intervalo de tempo entre as ações automatizadas (variável `intervalo`) conforme necessário.
    

## Notas Importantes

-   Este é uma automação **BÁSICA** com Selenium em Python. Você pode melhorar de acordo com sua necessidade.
  -  Este script serve unicamente para fazer colocar seu CPF e atualizar a página depois de algum tempo, ele ***NÃO VAI PROSSEGUIR COM SUA COMPRA***
- Ao ver que o ingresso que você deseja esta liberado, **PAUSE** o script e faça a compra do mesmo.
- Caso de algum erro na venda, volte até a página do ingresso onde você insere o seu CPF e clique em **CONTINUAR**, desta forma o script vai continuar rodando.
- Este script roda localmente, ou seja, o seu CPF não vai ser enviado para nenhum lugar.

