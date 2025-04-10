# imagem do Python
FROM python:3.10

# Define o diretório de trabalho dentro do container. Esse precisa ser o nome da pasta que você está trabalhando
WORKDIR /ENTREGA02-API

# Copia os arquivos do projeto para o container
COPY . .

# Instala as dependências
RUN pip install flask

#NOTA: Colocar o arquivo requimentents e dar o pip install para intalar as bibliotecas

# Expõe a porta que a aplicação vai usar. Se mudar a porta aqui, tem que mudar no app.py e config
EXPOSE 5036

# Comando para iniciar o app
CMD ["python", "app.py"]