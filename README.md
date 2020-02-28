# Introdução 

Este repositório se refere à pesquisa elaborada para artigo científico sobre governança de migração no Brasil, escrito por Vítor Eduardo Alessandri Ribeiro em coautoria com Roberto Rodolfo Georg Uebel e Eveline Vieira Brígido. 

A pesquisa empírica reflete uma análise feita sobre o corpus de texto de 2404 tweets com a *hashtag* "foravenezuelanos". 

A captura dos dados foi feita empregando o script elaborado por Jefferson Henrique, em seu projeto intitulado "GetOldTweets-python", disponível no repositório [GitHub](https://github.com/Jefferson-Henrique/GetOldTweets-python)

# Observação: 

Para a execução correta do script de captura dos dados do Twitter segundo a API desenvolvida por Jefferson Henrique, é necessário clonar o repositório e suas dependências. Para detalhes, ler [GitHub](https://github.com/Jefferson-Henrique/GetOldTweets-python/blob/master/README.md)

Os dados foram salvos em formato .csv e estão disponíveis nos diretórios **input** e **output** do mesmo repositório. Utilize a opção **git clone** para copiar todo o conteúdo ou utilize a opção de download. 

Como forma de buscar a reprodutibilidade dessa pesquisa, os parâmetros de linha de comando empregados para execução de captura dos tweets empregando o script em python escrito por Jefferson Henrique são os seguintes:

python Exporter.py --querysearch "fora venezuelanos" --since 2016-01-01 --until 2020-02-22 


# Sobre a pesquisa 

Os sucessivos tratamentos efetuados sobre o material coletado estão salvos em formato .ipynb 

Para acessá-los, recomenda-se a instalação das bibliotecas que são dependências necessárias para o correto acesso e uso dos documentos com extensão .ipynb 

# Instalação das dependências 

Para instalar use o comando no terminal (Linux e Mac OS) ou no commando do prompt (Windows):

pip3 install -r requirements.txt 

# Suporte 

Se desejar entrar em contato com o autor da pesquisa empírica, utilize o e-mail abaixo:

+ email: vealessandri@gmail.com

# Licença 

MIT License

Copyright (c) [year] [fullname]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.



