# Automação Instagram com Selenium
Este projeto utiliza a biblioteca Selenium para automatizar interações no Instagram. O script realiza login, navega até um perfil específico e curte publicações que ainda não foram curtidas. Ele é executado em um loop, repetindo o processo a cada 24 horas.

## Funcionalidades
- Acesso ao Instagram: O script abre o navegador e acessa a página inicial do Instagram.

- Login Automático: Realiza o login na conta do usuário, preenchendo automaticamente os campos de usuário e senha.

- Navegação Personalizada: Direciona até uma página escolhida pelo usuário (por exemplo, o perfil da Nike).

- Curtir Publicação: Verifica se a publicação está ou não curtida e, caso não esteja, realiza a ação de curtir.

- Loop de Execução: O script é executado em um loop infinito, com um intervalo de 24 horas entre cada execução.

## Tecnologias Utilizadas
Selenium: Para automatizar a interação com o navegador e a plataforma do Instagram.

WebDriverWait: Para gerenciar a espera por elementos na página.

Time (Sleep): Para gerenciar pausas e intervalos durante a execução do script.

## Como Usar
- Instalação das Dependências: 

Certifique-se de ter o Selenium instalado. Caso não tenha, instale usando o comando:

```bash
pip install selenium
```

## Funcionamento:

- O script abrirá o navegador, fará login no Instagram e navegará até o perfil especificado.

- Ele verificará a primeira publicação e a curtirá, caso ainda não esteja curtida.

- O script entrará em um loop, repetindo o processo a cada 24 horas.

## Estrutura do Script
O script está organizado da seguinte forma:

Inicialização do WebDriver:
Configura o navegador Chrome com opções personalizadas, como modo anônimo, tamanho da janela e idioma.

Login no Instagram:
Preenche os campos de usuário e senha e clica no botão "Entrar" (Deixe configurado suas configurações nas linhas 59 e 63).

Pagina desejada:
Caso queira alterar a página de verificação de curtida basta alterar o link na linha 72.

## Loop Infinito:
O script repete o processo a cada 24 horas.